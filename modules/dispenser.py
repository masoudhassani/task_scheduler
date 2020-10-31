class Dispenser:
    def __init__(self, cooking_machines):
        self.num_machines = len(cooking_machines)
        self.machines = cooking_machines
            
    def schedule(self):
        advantage = [0]*self.num_machines
        for i in range(self.num_machines):
            if self.machines[i].is_active:
                self.machines[i].find_next_cooking()
                advantage[i] = self.machines[i].advantage
                
        selected_machine = advantage.index(max(advantage))
        
        return selected_machine