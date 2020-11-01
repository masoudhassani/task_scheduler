class CookingMachine:
    def __init__(self, recipe=None):
        self.remaining_time = 0
        self.next_task = 0
        self.current_step = 0    # step number in recipe starting from 0
        self.current_task = ('i', 0)   # (task_type, remaining time)
        self.elapsed_time = 0
        self.ideal_cooking_time = 0
        self.current_step = 0
        self.current_state = 0  #idle:0, ing:1, cook:2
        self.recipe = recipe            
        self.processed_recipe = []
        self.next_cooking_duration = 0
        self.time_to_next_cooking = 0
        self.advantage = 0   # next_cooking_duration-time_to_next_cooking
        if recipe != None:
            self.recipe_name = self.recipe[0][0]
            self.is_active = True 
            self.process_recipe()
        else:
            self.recipe_name = None
            self.num_steps = 0
            self.is_active = False        
        

    '''
    read the order and assign it to cooking machines.
    combine cooking steps together
    '''        
    def process_recipe(self):
        # find the total time to cook a recipe assuming all steps are done without delay
        n = len(self.recipe)
        for i in range(n):
            self.ideal_cooking_time += self.recipe[i][1]
            
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
        self.current_task = (self.processed_recipe[self.current_step][0], 
                             self.processed_recipe[self.current_step][1])
          
    '''
    finds the duration of the next cooking task
    finds the time needed to the next cooking task
    '''                            
    def find_next_cooking(self):
        t = 0
        next_cooking_found = False
        if self.is_active:
            for j in range(self.current_step, self.num_steps):
                if self.processed_recipe[j][0] == 'i':
                    t += self.processed_recipe[j][1]
                else:
                    self.next_cooking_period = self.processed_recipe[j][1]
                    self.time_to_next_cooking = t
                    next_cooking_found = True 
                if next_cooking_found:
                    break
            
            self.advantage = self.next_cooking_period - self.time_to_next_cooking   
        
    
    
    
    