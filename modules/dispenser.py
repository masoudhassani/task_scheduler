class Dispenser:
    def __init__(self, cooking_machines):
        self.num_machines = len(cooking_machines)
        self.machines = cooking_machines
        self.ideal_cooking_times = [0]*self.num_machines
        self.max_ideal_cooking_time = 0   # sum of all cooking steps for a machine
        self.ref_machine = None  # reference machine is the one that has the max ideal cooking time
        self.current_machine = None # the cooking machine that is doing the current task
        self.find_max_ideal_cooking_time()
        self.done = False
            
    def find_max_ideal_cooking_time(self):
        for i in range(self.num_machines):
            if self.machines[i].has_order:
                self.ideal_cooking_times[i] = self.machines[i].ideal_cooking_time
            
        self.max_ideal_cooking_time = max(self.ideal_cooking_times)
        idx = self.ideal_cooking_times.index(self.max_ideal_cooking_time)
        self.ref_machine = self.machines[idx]
        self.current_machine = self.machines[idx]

    def select_machine(self):        
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
            print(temp)
            if len(temp) > 0:
                max_rem = 0
                for i in temp:
                    if self.machines[i].remaining_time - self.machines[i].current_task[1] > max_rem:
                        max_rem = self.machines[i].remaining_time - self.machines[i].current_task[1]
                        self.current_machine = self.machines[i]
        
            # if no other machine has ingredient step, selecet min_idx machine 
            else:             
                self.current_machine = self.machines[min_idx] 
        
    def operate(self): 
        print('select ->', self.current_machine.index)
        for i in range(self.num_machines):
            if self.machines[i].has_order:
                print(i, self.machines[i].current_task, 
                        self.machines[i].remaining_time,
                        self.machines[i].task_start_time)
        print('-------------------------------')
        
        # select a machine 
        self.select_machine()
           
        # update the task of current machine 
        reduction = self.current_machine.current_task[1] 
        ref_remaining_time = self.ref_machine.remaining_time 
        self.current_machine.update_current_task(
                                        reduction=reduction , time=ref_remaining_time)
        
        # update the current task of all machines
        for i in range(self.num_machines):
            # only check machines that have active orders
            if self.machines[i].is_active and self.machines[i].has_order:
                # if the machines other than the current machine have cooking step, do it
                # otherwise do not do it
                if i != self.current_machine.index and self.machines[i].current_task[0] == 'c':
                    self.machines[i].update_current_task(reduction=reduction, time=ref_remaining_time)                        
        
        return self.done
           
    def schedule(self):
        advantage = [0]*self.num_machines
        for i in range(self.num_machines):
            if self.machines[i].is_active:
                self.machines[i].find_next_cooking()
                advantage[i] = self.machines[i].advantage
                
        selected_machine = advantage.index(max(advantage))
        
        return selected_machine