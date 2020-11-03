# Task Scheduler
A task scheduler platform to assign tasks to multiple robots with limited resources. The specific problem solved by this code is as following:
- We have multiple cooking machines which can receive ingredients, cook them or stay in idle mode
- There is a single dispenser robot which is responsible for delivering ingredients to cooking machines. 
- The dispenser robot can deliver only to one cooking machine at a time. 
- The whole cooking system receives an order such as:  
[food A, food B, food A, food D, 0 ] where '0' means that the correcponsing cooking machine does not have an order.  
- Each cooking machine receives an order which includes the sequential steps to cook a food. Each step includes the recipe name, step number, step type and time it takes to finish it. A recipe looks like this:  
(chocolate_ice_cream, 1, i,3.5)  
(chocolate_ice_cream, 2, c,40)  
(chocolate_ice_cream, 3, i,1.5)  
(chocolate_ice_cream, 4, i,23)  
(chocolate_ice_cream, 5, i,1)  
(chocolate_ice_cream, 6, c,100)  
- The dispenser robot is responsible for 'i' or ingredient tasks and the cooking machines do the 'c' or cooking tasks.
- We want to schedule the dispenser and the cooking machines to achieve a minimum cooking time. We also want to schedule the robots to achieve an expected completion time for each recipe.

## Installation
```
python3 -m pip install -r requirements.txt 
```

## Run
Open main.py then modify the 'order' and 'num_machines' variables. If the order includes completion time for rach recipe, change 'include_time' to True. Then: 
```
python3 main.py
```
