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

#detroit = df_i.loc[['DET'],['PPT']]  note - how to select just the PPT values for a specific team - ex. DET

# Initialize the FacetGrid object
pal = sns.cubehelix_palette(n_colors=31, rot=-.25, light=.7)

g = sns.FacetGrid(df, row='Team', hue='Team', aspect=8.5, height=0.5, palette=pal)

# Draw the densities in a few steps
g.map(sns.kdeplot, 'PPT', clip_on=False, shade=True, alpha=1, lw=1.5, bw=.2)
g.map(sns.kdeplot, 'PPT', clip_on=False, color="w", lw=2, bw=.2)
g.map(plt.axhline, y=0, lw=2, clip_on=False)

# Define and use a simple function to label the plot in axes coordinates
def label(x, color, label):
    ax = plt.gca()
    ax.text(0, .2, label, fontweight="bold", color=color,
            ha="left", va="center", transform=ax.transAxes)
g.map(label,'PPT')

# Set the subplots to overlap
g.fig.subplots_adjust(hspace=-.01, right=0.9)

# Remove axes details that don't play well with overlap
g.set_titles("")
g.set(yticks=[])
g.despine(bottom=True, left=True, top=True, right=True, offset=5)
#set x axis limits
g.set(xlim=(-0.15,.15))

# launch the plot
g.savefig('ppt_0to09_12.png')