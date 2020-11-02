def read_recipes(recipes):
    pass

def gantt_chart(tasks):
    # tasks is [machine_idx, recipe name, start time, task type, task time]
    import plotly.express as px
    import pandas as pd 
    
    df = pd.DataFrame(columns=['Task', 'Start', 'Finish', 'Resource'])
    
    for i, row in enumerate(tasks):
        if row[3] == 'i':
            d = {'Task':row[0], 'Start':row[2], 'Finish':row[2]+row[4], 'Resource':'Ingredient'}
        else:
            d = {'Task':row[0], 'Start':row[2], 'Finish':row[2]+row[4], 'Resource':'Cooking'}
            
        df = df.append(d, ignore_index=True)
        
    fig = px.timeline(df, x_start='Start', x_end='Finish', y='Task', color='Resource')
    fig.update_yaxes(autorange="reversed")
    fig.show()