#A kernel density estimate (KDE) plot is a method for visualizing the distribution of observations in a dataset,analogous to a histogram. 
#KDE represents the data using a continuous probability density curve in one or more dimensions.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 

supermarket_df = pd.read_excel("supermarket_sales.xlsx")

sns.kdeplot(data=supermarket_df, x='Total') # To plot basic kdeplot
plt.title("KDE PLOT Basic")
plt.show()

sns.kdeplot(data=supermarket_df, warn_singular=False) # kde plot for all numeric value in dataframe 
plt.title("KDE PLOT for All numeric value")
plt.show()

sns.kdeplot(data=supermarket_df, x='Total', hue='Gender')#kdeplot to group it with total & gender 
plt.title("kdeplot with Total & Gender")
plt.show()

sns.kdeplot(data=supermarket_df, x='Total', hue='Gender', multiple='stack', alpha=0.2) 
#To plot gender on each other using multiple as 'stack' more options are "layer","stack","fill" 
plt.title("kdeplot with Total & Gender with Stack")
plt.show()