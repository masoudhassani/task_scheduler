from modules import CookingMachine, Dispenser
from modules import gantt_chart, return_recipes

'''
function to instanciate cooking machines and the dispenser robot
return the task schedule
'''
def create_task_schedule(num_machines, recipes, order):
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
        done = dispenser.schedule()

    # print some stuff
    for i in range(num_machines):
        if cooking_machines[i].has_order:
            print(i, cooking_machines[i].task_start_time)
    print('-------------------------------')    
    print('scheduling completed')
    
    return dispenser.task_schedule

num_machines = 5
recipes = return_recipes()
order = ['asparagus_soup', 'carrot_soup', 'sabayon', 'sabayon', 'mushroom_risotto']
# order = ['test1', 0, 'test2', 0, 'test3']

# generate the task schedule
task_schedule = create_task_schedule(num_machines, recipes, order)

# plot the gantt chart
gantt_chart(task_schedule)



   
                       