from modules import CookingMachine, Dispenser

num_machines = 5
recipes = {
          'asparagus_soup': (('i',11),
                            ('i',5),
                            ('c',15),
                            ('c',200),
                            ('i',50),
                            ('i',1),
                            ('c',30),
                            ('i',40),
                            ('c',900),
                            ('c',60),
                            ('i',10),
                            ('c',20)),
           'chili_con_carne':   (('i',11),
                                ('c',15),
                                ('i',1),
                                ('c',180),
                                ('i',2),
                                ('c',120),
                                ('i',40),
                                ('c',20),
                                ('i',84),
                                ('c',600)),
           'sabayon': (('i',12),
                       ('i',6),
                       ('i',6),
                       ('c',540)),
           'test1':   (('i', 30),
                       ('c', 50),
                       ('i', 10),
                       ('c', 300)),
           'test2':   (('i', 20),
                       ('c', 200),
                       ('i', 30),
                       ('c', 100),
                       ('i', 70),
                       ('c', 50),
                       ('i', 30),
                       ('c', 20)),
           'test3':   (('i', 10),
                       ('c', 100),
                       ('i', 60),
                       ('c', 50),
                       ('i', 10),
                       ('c', 100))                      
}

order = ['test1', 0, 'test2', 0, 'test3']

cooking_machines = [None]*num_machines
for i in range(num_machines):
    if order[i] != 0:
        cooking_machines[i] = CookingMachine(recipe=recipes[order[i]])
        cooking_machines[i].find_next_cooking()
        print(cooking_machines[i].current_step)
        print(cooking_machines[i].current_task)
    else:
        cooking_machines[i] = CookingMachine(recipe=None)
        
    

dispenser = Dispenser(cooking_machines) 
print(dispenser.max_ideal_cooking_time, dispenser.ref_machine)
   
                       