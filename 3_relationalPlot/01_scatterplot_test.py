#A diagram which shows the relationship between two variables by plotting the points/dots
#Draw a scatter plot with possibility of several semantic groupings.
#"The relationship between x and y can be shown for different subsets of the data using the hue, size, and style parameters. 
#These parameters control what visual semantics are used to identify the different subsets"
import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt

train_df = pd.read_excel("train.xlsx")

sns.scatterplot(data=train_df, x='Item_MRP',y='Sales') #To create basic scatter plot
plt.title("Basic scatterplot")
plt.show()

sns.scatterplot(data=train_df, x='Item_MRP', y='Sales', hue='Outlet_Location_Type') 
#hue - Grouping variable that will produce points with different colors
plt.title("scatterplot using hue")
plt.show()

sns.scatterplot(data=train_df, x='Item_MRP', y='Sales', style='Outlet_Location_Type') 
#style - Grouping variable that will produce points with different markers
plt.title("scatterplot using style")
plt.show()

sns.scatterplot(data=train_df, x='Item_MRP', y='Sales', size='Outlet_Location_Type') 
#size - Grouping variable that will produce points with different sizes
plt.title("scatterplot using size")
plt.show()
