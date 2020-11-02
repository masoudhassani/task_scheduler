def read_recipes(recipes):
    pass

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
