num_machines = 5
machine = [None]*num_machines
current_state = [None]*num_machines  #idle:0, ing:1, cook:2
current_step = [None]*num_machines
time_elapsed = 0
time_elapsed_on_food = [None]*num_machines
time_remaining = [None]*num_machines
next_cooking_period = [None]*num_machines
time_to_next_cooking = [None]*num_machines
branch_score = [None]*num_machines
current_step = [0,None,0,0,0]
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

'''
read the order and assign it to cooking machines.
combine cooking steps together
'''
def process_order():
    for i in range(num_machines):
        # if the machine has an order
        if order[i] != 0:
            current_state[i] = 0
            lst = []
            r = recipes[order[i]]
            j = 0
            
            # combine cooking steps
            while j < len(r):
                if r[j][0] == 'i':
                    lst.append(r[j])
                    j += 1
                else:
                    if j == len(r)-1:
                        lst.append(r[j])
                        break 
                    
                    else:                       
                        if r[j+1][0] == 'i':
                            lst.append(r[j])
                            j += 1
                        else:
                            lst.append(('c', r[j+1][1]+r[j][1]))
                            j += 2
                        
            machine[i] = lst
            
def find_next_cooking():
    for i in range(num_machines):
        t = 0
        next_cooking_found = False
        if machine[i] != None:
            for j in range(current_step[i], len(machine[i])):
                if machine[i][j][0] == 'i':
                    t += machine[i][j][1]
                else:
                    next_cooking_period[i] = machine[i][j][1]
                    time_to_next_cooking[i] = t
                    next_cooking_found = True 
                if next_cooking_found:
                    break
            
            branch_score[i] = next_cooking_period[i] - time_to_next_cooking[i]
                    
def schedule():
    find_next_cooking()
    selected_machine = branch_score.index(max(branch_score))
    
    if machine[selected_machine][current_step[selected_machine]][0] == 'i':
        current_state[selected_machine] = 1 
    else:
        current_state[selected_machine] = 2

                        
                
            
        
process_order()
find_next_cooking()
schedule()
print(machine)
#min(x for x in L if x is not None)
print((next_cooking_period))
print(time_to_next_cooking)
print(branch_score)
print(current_state)