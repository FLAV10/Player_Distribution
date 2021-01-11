import numpy as np
import pandas as pd
import pprint
import json
from bson import json_util 
import matplotlib.pyplot as plt
import seaborn as sns

# read in data table
df = pd.read_csv('stats.csv', sep=',', header='infer') 

# set the dataFrame index to the 'Team' column
df_i = df.set_index('Team') 

# create a list of unique team names
unique_teams = df.Team.unique() 

#detroit = df_i.loc[['DET'],['PPT']]  how to select just the PPT values for a specific team - ex. DET
#

# Create the plot objet "distribution"
for team in unique_teams:
    distribution = sns.distplot(df_i.loc[[team],['PPT']], hist=False, label=team, rug=False)

#distribution = sns.distplot(detroit, label='detroit', rug=True)

#set the plot parameters
distribution.set(xlim=(0,0.125))
distribution.set_ylabel('Probability Density')
distribution.set_title('PPT distribution')

#launch the plot
plt.show()