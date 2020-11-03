def return_recipes():
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
            'carrot_soup': (('i',11),
                                ('i',1.5),
                                ('i',1.5),
                                ('c',20),
                                ('c',180),
                                ('i',50)),         
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
    
    return recipes 
 
def gantt_chart(tasks):
    # tasks is [machine_idx, recipe name, start time, task type, task time]
    import plotly.figure_factory as ff
    import pandas as pd 
    
    df = pd.DataFrame(columns=['Task', 'Start', 'Finish', 'Resource'])
    
    for row in tasks:
        if row[3] == 'i':
            d = {'Task':row[0], 'Start':row[2], 'Finish':(row[2]+row[4]), 'Resource':'Ingredient'}
        else:
            d = {'Task':row[0], 'Start':row[2], 'Finish':(row[2]+row[4]), 'Resource':'Cooking'}
            
        df = df.append(d, ignore_index=True)

    colors = {'Ingredient': 'rgb(220, 0, 0)',
             'Cooking': 'rgb(0, 255, 100)'}

    fig = ff.create_gantt(df, colors=colors, index_col='Resource', show_colorbar=True,
                      group_tasks=True)
    fig.update_xaxes(type=None)                        
    fig.show()
