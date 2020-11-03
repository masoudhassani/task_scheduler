from modules import CookingMachine, Dispenser
from modules import gantt_chart, return_recipes

'''
function to instanciate cooking machines and the dispenser robot
return the task schedule
'''
def create_task_schedule(num_machines, recipes, order, include_time=True):
    # initialize cooking machines
    cooking_machines = [None]*num_machines
    for i in range(num_machines):
        # if order includes completion time
        if include_time:
            if order[i] != 0:
                cooking_machines[i] = CookingMachine(recipe=recipes[order[i][0]], 
                                                    index=i, name=order[i][0],
                                                    finish_time=order[i][1])

            else:
                cooking_machines[i] = CookingMachine(recipe=None)
        
        # if order does not include completion time
        else:
            if order[i] != 0:
                cooking_machines[i] = CookingMachine(recipe=recipes[order[i]], 
                                                    index=i, name=order[i],
                                                    finish_time=order[i])

            else:
                cooking_machines[i] = CookingMachine(recipe=None)            

    # initialize the dispenser         
    dispenser = Dispenser(cooking_machines, include_time) 

    # go throught the order from the end to the start 
    done = False 
    while not done:
        done = dispenser.schedule()

    # print some stuff
    for i in range(num_machines):
        if cooking_machines[i].has_order:
            print(i, cooking_machines[i].task_start_time)
    print('-------------------------------')    
    print('scheduling completed')
    
    return dispenser.task_schedule

# ####################################
# parameters
num_machines = 5
include_time = True
recipes = return_recipes()
# order = ['asparagus_soup', 'carrot_soup', 'sabayon', 0, 'mushroom_risotto']
order = [('asparagus_soup',600), ('carrot_soup',1200), ('sabayon',1200)
         , ('sabayon',1800), ('mushroom_risotto',400)]
# order = [('asparagus_soup',600), ('carrot_soup',1200), 0, ('sabayon',1800), 0]
# order = ['test1', 0, 'test2', 0, 'test3']

# generate the task schedule
task_schedule = create_task_schedule(num_machines, recipes, order, include_time)

# plot the gantt chart
gantt_chart(task_schedule)



   
                       