#catplot() is used to plot different category of plot. kind parameter used to generate different plot
#kind - “strip”, “swarm”, “box”, “violin”, “boxen”, “point”, “bar”, “count”
#Also we can provide x-axis, y-axis, row, col parameter to divide figure based on different values of rows & columns in dataframe

import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd 

supermarket_df = pd.read_excel("supermarket_sales.xlsx")

sns.catplot(data=supermarket_df, y='Total', x='Payment') #Kind - default is 'strip' so it will generate strip plot
plt.title("catplot default strip")
plt.show()

sns.catplot(data=supermarket_df, y='Total', x='Payment', kind='box') #kind is 'box' so it will generate box plot
plt.title("catplot kind box")
plt.show()

sns.catplot(data=supermarket_df, y='Total', x='Payment', kind='violin') #kind is 'violin' so it will generate violin plot
plt.title("catplot kind violin")
plt.show()

sns.catplot(data=supermarket_df, y='Total', x='Payment', kind='violin', hue='Gender') #kind is 'violin' so it will generate violin plot
plt.title("catplot kind violin based on Gender")
plt.show()

sns.catplot(data=supermarket_df, y='Total', x='Payment', kind='violin', col='Gender') #kind is 'violin' so it will generate violin plot
#As col is gender it will divide figure in two column each for gender
plt.title("catplot kind different violin based on Gender")
plt.show()

sns.catplot(data=supermarket_df, y='Total', x='Payment', row='Customer type', col='Gender', kind='box') #kind is 'box' so it will generate box plot
#as row & col is provided so it will divide entrire figure in rows & column based on different value found in "Customer type" & "Gender" 
plt.title("catplot kind box based customer type & gender")
plt.show()
