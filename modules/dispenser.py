class Dispenser:
    def __init__(self, cooking_machines):
        self.num_machines = len(cooking_machines)
        self.machines = cooking_machines
        self.ideal_cooking_times = [0]*self.num_machines
        self.max_ideal_cooking_time = 0   # sum of all cooking steps for a machine
        self.ref_machine = 0  # reference machine is the one that has the max ideal cooking time
        
        self.find_max_ideal_cooking_time()
            
    def find_max_ideal_cooking_time(self):
        for i in range(self.num_machines):
            if self.machines[i].is_active:
                self.ideal_cooking_times[i] = self.machines[i].ideal_cooking_time
            
        self.max_ideal_cooking_time = max(self.ideal_cooking_times)
        self.ref_machine = self.ideal_cooking_times.index(self.max_ideal_cooking_time)

    def select_machine(self):
        lst = [None]*self.num_machines
        for i in range(self.num_machines):
            if self.machines[i].is_active:
                # lst[i] = self.machines[i].
                pass
                        
           
    def schedule(self):
        advantage = [0]*self.num_machines
        for i in range(self.num_machines):
            if self.machines[i].is_active:
                self.machines[i].find_next_cooking()
                advantage[i] = self.machines[i].advantage
                
        selected_machine = advantage.index(max(advantage))
        
        return selected_machine