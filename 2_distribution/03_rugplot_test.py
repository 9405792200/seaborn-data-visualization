#rugplot is marginal distributions by drawing ticks along the x and y axes
#This function is intended to combine with other plots by showing the location of individual observations in an unobtrusive way
#We can combine rugplot with histplot() kdeplot() & others plot as well 

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 

supermarket_df = pd.read_excel("supermarket_sales.xlsx")

sns.rugplot(data=supermarket_df, x='Total') #To plot basic rugplot()
plt.title("Basic rugplot")
plt.show()

sns.rugplot(data=supermarket_df, x='Total', y='Unit price') #rugplot with two variable
plt.title("rugplot with two variable")
plt.show()

sns.rugplot(data=supermarket_df, x='Total', y='Unit price', hue='Gender') #rugplot with group by gender using hue
plt.title("rugplot with group by gender")
plt.show()

sns.rugplot(data=supermarket_df, x='Total', y='Unit price', hue='Gender', height=0.1) 
#height parameter used to change height of each rug, default 0.025
plt.title("rugplot with height parameter")
plt.show()

sns.rugplot(data=supermarket_df, x='Total', height=0.1, hue='Gender') 
sns.histplot(data=supermarket_df, x='Total', hue='Gender', multiple='stack')
plt.title("rugplot with histplot combine")
plt.show()

sns.rugplot(data=supermarket_df, x='Unit price', y='gross income', height=0.1, hue='Gender') 
sns.scatterplot(data=supermarket_df, x='Unit price', y='gross income', hue='Gender')
plt.title("rugplot with scatterplot combine")
plt.show()