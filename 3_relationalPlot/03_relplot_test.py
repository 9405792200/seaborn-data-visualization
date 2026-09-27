import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt

#Figure-level interface for drawing relational plots onto a FacetGrid
#This function provides access to several different axes-level functions that show the relationship between two variables with semantic mappings of subsets. 
#The kind parameter selects the underlying axes-level function to use:
#scatterplot() (with kind="scatter"; the default)
#lineplot() (with kind="line")

train_df = pd.read_excel("train.xlsx")

sns.relplot(data=train_df, x='Outlet_Year', y='Sales') # By default kind is scatter
plt.title("Basic relplot default scatter")
plt.show()

sns.relplot(data=train_df, x='Outlet_Year', y='Sales', kind='line', errorbar=None) # here kind parameter is line
plt.title("Basic relplot with kind line")
plt.show()

sns.relplot(data=train_df, x='Outlet_Year', y='Sales',hue='Outlet_Size') # By default kind is scatter
plt.title("Basic relplot default scatter & hue")
plt.show()

sns.relplot(data=train_df, x='Outlet_Year', y='Sales', hue='Outlet_Size', kind='line', errorbar=None) # here kind parameter is line
plt.title("Basic relplot with kind line & hue")
plt.show()

sns.relplot(data=train_df, x='Outlet_Year', y='Sales',row='Outlet_Size',col='Outlet_Location_Type',hue='Outlet_ID')
#It will plot scatter plot to show relationship between Outlet_Year & Sales.It divide entire FacetGrid into row * col based on different values of Outlet_Size & Outlet_Location_Type
plt.show()