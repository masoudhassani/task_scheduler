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
           'mushroom_risotto' : (('i',3.5),
                                ('i',0.5),
                                ('i',11),
                                ('c',8),
                                ('c',180),
                                ('i',25),
                                ('c',180),
                                ('i',10),
                                ('c',10),
                                ('i',0.5),
                                ('i',1.5),
                                ('i',0.2),
                                ('i',40),
                                ('c',900),
                                ('i',15),
                                ('c',7),
                                ('i',15),
                                ('c',180),
                                ('i',5),
                                ('c',30)),           
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

order = ['asparagus_soup', 0, 'sabayon', 'sabayon', 0]
order = ['test1', 0, 'test2', 0, 'test3']

# initialize cooking machines
cooking_machines = [None]*num_machines
for i in range(num_machines):
    if order[i] != 0:
        cooking_machines[i] = CookingMachine(recipe=recipes[order[i]], index=i, name=order[i])

    else:
        cooking_machines[i] = CookingMachine(recipe=None)

# initialize the dispenser         
dispenser = Dispenser(cooking_machines) 

# go throught the order from the end to the start 
done = False 
while not done:
    done = dispenser.operate()

# print some stuff
for i in range(num_machines):
    if cooking_machines[i].has_order:
        print(i, cooking_machines[i].task_start_time)
print('-------------------------------')    
print('scheduling completed')
   
                       