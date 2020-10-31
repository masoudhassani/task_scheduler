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
                       ('c',540))
}

order = ['asparagus_soup', 0, 'sabayon', 'chili_con_carne', 'chili_con_carne']

cooking_machines = [None]*num_machines
for i in range(num_machines):
    if order[i] != 0:
        cooking_machines[i] = CookingMachine(recipe=recipes[order[i]])
        cooking_machines[i].find_next_cooking()
        print(cooking_machines[i].processed_recipe)
    else:
        cooking_machines[i] = CookingMachine(recipe=None)
        
    print(cooking_machines[i].advantage)

dispenser = Dispenser(cooking_machines) 
idx = dispenser.schedule()
print(idx)   
                       