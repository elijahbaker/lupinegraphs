import csv

import plotly
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

#Get Average Seed Count for Nipomo Lupine in Drought and Control Conditions

lunifilename = 'luni_gen_python.csv'

# lunifilename = pd.read_csv('luni_gen_python.csv')
# lunifilename.head()

# lunifilename.shape
# lunifilename.isnull()
# dflunifilename=lunifilename.fillna(" ")


with open(lunifilename) as f:
    reader=csv.reader(f)
    header_row = next(reader)

    Y_seeds = []
    N_seeds = []
    Y_row_counter=0
    N_row_counter=0

    for row in reader:
        seed = row[3]
        drought = row[0]
        if seed.isnumeric() and drought == 'Y':
            Y_row_counter+=1
            Y_seeds.append(seed)
        elif seed.isnumeric() and drought == 'N':
            N_row_counter+=1
            N_seeds.append(seed)
        # print(str(row[3].isnumeric()) + row[3])
    # print(seeds)

    Y_seeds_total = 0
    N_seeds_total = 0
    for each in Y_seeds:
        Y_seeds_total+=int(each)
    for each in N_seeds:
        N_seeds_total+=int(each)    

    Y_luni_seed_average = Y_seeds_total/Y_row_counter
    N_luni_seed_average = N_seeds_total/N_row_counter
    print(f"Yes Luni Seed Average: {Y_luni_seed_average} No Luni Seed Average: {N_luni_seed_average}")


#Get Average Seed Count for Miniature Lupine in Drought and Control Conditions

lubifilename = 'Lubi_gen2_python.csv'

# lubifilename.head()

# lubifilename.shape
# lubifilename.isnull()
# dflubifilename=lubifilename.fillna(" ")


with open(lubifilename) as f:
    reader=csv.reader(f)
    header_row = next(reader)

    Y_seeds = []
    N_seeds = []
    Y_row_counter=0
    N_row_counter=0

    for row in reader:
        seed = row[9]
        drought = row[4]
        if seed.isnumeric() and drought == 'Y':
            Y_row_counter+=1
            Y_seeds.append(seed)
        elif seed.isnumeric() and drought == 'N':
            N_row_counter+=1
            N_seeds.append(seed)
        # print(str(row[3].isnumeric()) + row[3])
    # print(seeds)

    Y_seeds_total = 0
    N_seeds_total = 0
    for each in Y_seeds:
        Y_seeds_total+=int(each)
    for each in N_seeds:
        N_seeds_total+=int(each)    

    Y_lubi_seed_average = Y_seeds_total/Y_row_counter
    N_lubi_seed_average = N_seeds_total/N_row_counter
    print(f"Yes Lubi Seed Average: {Y_lubi_seed_average} No Lubi Seed Average: {N_lubi_seed_average}")


drought=['Control Conditions', 'Drought Conditions']


fig = go.Figure(data=[
    go.Bar(name='Nipomo Lupine', x=drought, y=[N_luni_seed_average, Y_luni_seed_average]),
    go.Bar(name='Minature Lupine', x=drought, y=[N_lubi_seed_average, Y_lubi_seed_average])
])



fig.update_layout(
    barmode='group',
    title="Adaptability of Common Lupines in Drought Conditions",
    yaxis_title="Average Seed Production",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#003366"
    )
)
fig.show()












# data = pd.read_csv('luni_gen_python.csv')
# data.head()

# data.shape
# data.isnull()
# df=data.fillna(" ")



# df_seed_mean = pd.DataFrame(df,columns=['drought','seeds','avgseedmass','leaves'])
# print (df_seed_mean) 


# seedsgraph = px.bar(df_seed_mean, x="drought", y="seeds", 
#     hover_data=['avgseedmass'],
#     color='drought', barmode='group',
#     labels={'seeds':'Total Seed Production'},
#     height=325)

# seedsgraph.show()


