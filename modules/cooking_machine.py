class CookingMachine:
    def __init__(self, recipe=None, index=None, name='', finish_time=0):
        self.index = index
        self.current_step = 0    # step number in recipe starting from 0
        self.current_task = ('i', 0)   # (task_type, remaining time of current task)
        self.ideal_cooking_time = 0
        self.recipe = recipe            
        self.processed_recipe = []
        self.done = False   # becomes true when cooking the recipe is done
        if recipe != None:
            self.recipe_name = name
            self.has_order = True    #becomes true when the machine has an order
            self.process_recipe()
        else:
            self.recipe_name = name
            self.num_steps = 0
            self.has_order = False      
        self.is_active = True   # becomes false when order is complete  
        self.finish_time = finish_time
        
    '''
    read the order and assign it to cooking machines.
    combine cooking steps together
    '''        
    def process_recipe(self):
        # find the total time to cook a recipe assuming all steps are done without delay
        n = len(self.recipe)
        for i in range(n):
            self.ideal_cooking_time += self.recipe[i][1]
            self.remaining_time = self.ideal_cooking_time    
            
        j = 0
        # combine adjacent cooking steps 
        while j < n:
            if self.recipe[j][0] == 'i':
                self.processed_recipe.append((self.recipe[j][0], self.recipe[j][1]))
                j += 1
            else:
                if j == n -1:
                    self.processed_recipe.append((self.recipe[j][0], self.recipe[j][1]))
                    break 
                
                else:                       
                    if self.recipe[j+1][0] == 'i':
                        self.processed_recipe.append((self.recipe[j][0], self.recipe[j][1]))
                        j += 1
                    else:
                        self.processed_recipe.append(('c', self.recipe[j+1][1]+self.recipe[j][1]))
                        j += 2

        self.num_steps = len(self.processed_recipe) 
        
        # we calculate the start time of each task by processing the
        # the recipe from end to start, therefore the current task
        # is the last task 
        self.current_step = self.num_steps - 1
        self.current_task = [self.processed_recipe[self.current_step][0], 
                             self.processed_recipe[self.current_step][1]]
        self.task_start_time = [0]*self.num_steps  
    
    '''
    this function is called when the order includes expected completion time
    in that case a fake step is added to the whole recipe to ensure the finsih time
    '''
    def add_fake_step(self, task):
        self.processed_recipe.append(task)  
        self.current_step = self.num_steps
        self.current_task = [task[0], task[1]]
        self.num_steps += 1
        self.task_start_time = [0]*(self.num_steps) 
        self.remaining_time += task[1]  
    
    '''
    main function to update the current task and remaining time
    '''              
    def update_current_task(self, reduction, time):
        r = self.current_task[1]
        
        # if the current step is done
        if (r - reduction) < 0.001:
            self.task_start_time[self.current_step] = round(time - reduction,1)    # update the task start time
            
            # if this is the first step of recipe which is the end of algorithm
            if self.current_step == 0:
                self.is_active = False             
                self.remaining_time = 0
                
            # if in the middle of recipe, reduce the step number and update the current task 
            else:
                self.current_step -= 1
                self.current_task = [self.processed_recipe[self.current_step][0], 
                                    self.processed_recipe[self.current_step][1]] 
                
                # update the total remaining time of recipe
                self.remaining_time -= reduction          
        
        # if the current step is not done        
        elif r - reduction > 0:
            self.current_task[1] -= reduction # update the remaining time of current task
            self.remaining_time -= reduction  # update the total remaining time of recipe 
                       
        # if reducing from the remaining time leads to negative number    
        else:
            # if this is the first step of recipe which is the end of algorithm
            if self.current_step == 0:
                self.is_active = False
                self.task_start_time[self.current_step] = 0
                self.remaining_time = 0
                
            # if in the middle of recipe 
            else:
                self.task_start_time[self.current_step] = round(time - r,1)    # update the task start time  
                self.current_step -= 1
                self.current_task = [self.processed_recipe[self.current_step][0], 
                                    self.processed_recipe[self.current_step][1]]  
                self.remaining_time -= r
                print('exeption for food {} at index {}'.format(self.recipe_name, self.index))
                
        return self.is_active
                
                
                
            
            
                
    
    
    