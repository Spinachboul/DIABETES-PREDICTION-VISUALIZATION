import matplotlib
matplotlib.use("TkAgg")
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv('diabetes.csv')

# Looking at the first 5 columns of the dataset
print(df.head())



# SHow the histogram
df.hist()
plt.tight_layout()
plt.show()


# Show density plot 
# Creating a subplot of 3x3
plt.subplots(3,3,figsize=(20,20))


# Plot a density plot for each variable
for idx, col in enumerate(df.columns):
    ax = plt.subplot(3, 3, idx+1)
    ax.yaxis.set_ticklabels([])
    sns.distplot(df.loc[df.Outcome == 0][col], hist=False, axlabel= False, kde_kws={'linestyle':'-', 'color':'black', 'label':"No Diabetes"})
    sns.distplot(df.loc[df.Outcome == 1][col], hist=False, axlabel= False, kde_kws={'linestyle':'--', 'color':'black', 'label':"Diabetes"})
    ax.set_title(col)


# Hiding the 9th subplot, since there are only 8 plots
plt.subplot(3,3,9).set_visible(False)
plt.tight_layout()
plt.show()
