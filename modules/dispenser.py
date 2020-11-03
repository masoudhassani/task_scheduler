class Dispenser:
    def __init__(self, cooking_machines, include_time=False):
        self.num_machines = len(cooking_machines)
        self.machines = cooking_machines
        self.ideal_cooking_times = [0]*self.num_machines
        self.max_ideal_cooking_time = 0   # sum of all cooking steps for a machine
        self.ref_machine = None  # reference machine is the one that has the max ideal cooking time
        self.current_machine = None # the cooking machine that is doing the current task
        self.done = False
        self.task_schedule = []
        self.include_time = include_time
        self.finish_time_offset = [0]*self.num_machines
        self.ideal_cooking_time_offset = []
        self._find_max_ideal_cooking_time()
    
    '''
    function to find the idea l cooking time of all recipes
    and find the maximum between them
    '''        
    def _find_max_ideal_cooking_time(self):
        # if the order does not include expected finish time
        if not self.include_time:
            for i in range(self.num_machines):
                if self.machines[i].has_order:
                    self.ideal_cooking_times[i] = self.machines[i].ideal_cooking_time
                
            self.max_ideal_cooking_time = max(self.ideal_cooking_times)
            idx = self.ideal_cooking_times.index(self.max_ideal_cooking_time)
            self.ref_machine = self.machines[idx]
            self.ref_remaining_time = self.machines[idx].remaining_time
            self.current_machine = self.machines[idx]
        
        # if the order includes finish time
        else:
            # find the finish time offset 
            lst = [None]*self.num_machines
            for i in range(self.num_machines):
                if self.machines[i].has_order:
                    lst[i] = self.machines[i].finish_time
                    
            max_finish_time = max(x for x in lst if x is not None)
            max_finish_time_index = lst.index(max_finish_time)

            for i in range(self.num_machines):
                if self.machines[i].has_order:
                    self.finish_time_offset[i] = (self.machines[i].finish_time - self.machines[max_finish_time_index].finish_time)
                                                    
            print(self.finish_time_offset)
            
            for i in range(self.num_machines):
                if self.machines[i].has_order:
                    self.machines[i].add_fake_step(('c',abs(self.finish_time_offset[i])))

            self.ref_machine = self.machines[max_finish_time_index]
            self.ref_remaining_time = self.machines[max_finish_time_index].remaining_time
            self.current_machine = self.machines[max_finish_time_index]            

        # print some debug info
        print('status of all active machines:')
        for i in range(self.num_machines):
            if self.machines[i].has_order:
                print(i, self.machines[i].current_task, 
                        round(self.machines[i].remaining_time, 1),
                        self.machines[i].task_start_time)
        print('-------------------------------')
        # ############################
    
    '''
    logic to prioritize a cooking machine between all active ones
    the logic is defined as:
    - select the machine with minimum remaining time of current step
    - if other machines than the selected one do not have a current ingredient step, 
        do the step of the selected machine
    - if there is ingredient step other than the selected one, choose the machine with
        max remaining time
    '''    
    def _select_machine(self):        
        lst = [None]*self.num_machines
        # update the remaining time of current task for all active machines
        for i in range(self.num_machines):
            # only check machines that have active orders
            if self.machines[i].is_active and self.machines[i].has_order:
                lst[i] = self.machines[i].current_task[1]
        
        # if no machine with order is active it means order is done
        if all(l is None for l in lst):
            self.done = True 
            
        # find the min of remaining time of current task for all active machines
        else:
            min_rem_time = min(x for x in lst if x is not None)
            min_idx = lst.index(min_rem_time)
        
            # check if other machines except for min_idx have ingredient step
            # if there are ingredient steps currently, select the one with max total remaining time
            # otherwise select min_idx
            ingredient_found = False
            temp = []
            for i in range(self.num_machines):
                # only check machines that have active orders
                if self.machines[i].is_active and self.machines[i].has_order and i != min_idx:           
                    if self.machines[i].current_task[0] == 'i':
                        #temp.append(i)
                        ingredient_found = True
                
            # if there are machines with current ingredient step    
            if ingredient_found:
                for i in range(self.num_machines):
                    if self.machines[i].is_active and self.machines[i].has_order:
                        temp.append(i)
                        
            if len(temp) > 0:
                max_rem = -10000
                for i in temp:
                    if self.machines[i].remaining_time - self.machines[i].current_task[1] > max_rem:
                        max_rem = self.machines[i].remaining_time - self.machines[i].current_task[1]
                        self.current_machine = self.machines[i]
        
            # if no other machine has ingredient step, selecet min_idx machine 
            else:             
                self.current_machine = self.machines[min_idx] 
        
    '''
    main funtion which should be called in a loop until it returns True
    - it selects the cooking machine to do the operation 
    - it updates the remaining time and current task of all cooking machines
    '''    
    def schedule(self):                         
        # select a machine 
        self._select_machine()

        # if order is done for all machines, find the smallet negative start time
        # for the first task of all machines
        if self.done:
            min_start_time = 0
            # update the current task of all machines
            for i in range(self.num_machines):
                # only check machines that have orders
                if self.machines[i].has_order and self.machines[i].task_start_time[0] < min_start_time:
                    min_start_time = self.machines[i].task_start_time[0]
            
            # offset all task start times based on min_start_time
            if min_start_time < 0:
                # update the current task of all machines
                for i in range(self.num_machines):
                    # only check machines that have orders
                    if self.machines[i].has_order:
                        for j in range(self.machines[i].num_steps):
                            self.machines[i].task_start_time[j] += abs(min_start_time)    
                            
            # create the task schedule  
            # task schedule is [machine_idx, recipe name, start time, task type, task time]       
            for i in range(self.num_machines):
                # only check machines that have orders
                if self.machines[i].has_order:
                    if self.include_time:
                        n = self.machines[i].num_steps - 1
                    else:
                        n = self.machines[i].num_steps
                    for j in range(n):
                        self.task_schedule.append([i, self.machines[i].recipe_name,
                                                   self.machines[i].task_start_time[j],
                                                   self.machines[i].processed_recipe[j][0],
                                                   self.machines[i].processed_recipe[j][1]])
            
            # sort the task schedule based on the task start time 
            self.task_schedule = sorted(self.task_schedule, key=lambda l:l[2])            
                                        
            return self.done        
        
        # update the amount of time reduction based on the task of current machine 
        reduction = self.current_machine.current_task[1]        

        # update the current task of current machine 
        self.current_machine.update_current_task(
                                        reduction=reduction , time=self.ref_remaining_time)

        self.ref_remaining_time -= reduction
 
        # print some debug stuff
        print('select ->', self.current_machine.index)
        for i in range(self.num_machines):
            if self.machines[i].has_order:
                print(i, self.machines[i].current_task, 
                        round(self.machines[i].remaining_time, 1),
                        self.machines[i].task_start_time)
        print('-------------------------------')
        #################################
         
        # update the current task of all machines but the current machine
        for i in range(self.num_machines):
            # only check machines that have active orders
            if self.machines[i].is_active and self.machines[i].has_order:
                # if the machines other than the current machine have cooking step, do it
                # otherwise do not do it
                if i != self.current_machine.index and self.machines[i].current_task[0] == 'c':
                    self.machines[i].update_current_task(reduction=reduction, time=self.ref_remaining_time)                        
        
        return self.done
           