import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Draw a line plot with possibility of several semantic groupings
#"The relationship between x and y can be shown for different subsets of the data using the hue, size, and style parameters. 
#These parameters control what visual semantics are used to identify the different subsets"

train_df = pd.read_excel("train.xlsx")

sns.lineplot(data=train_df, x='Outlet_Year', y='Sales', errorbar=None, marker='o', markersize=4) 
#It will plot line for outlet_year & sales. By default it will show mean of sales because  
plt.title("Basic lineplot")
plt.show()

sns.lineplot(data=train_df, x='Outlet_Year', y='Sales', errorbar=None, estimator=sum, marker='o', markersize=4)
#it will plot line by summing Sales for each outlet_year
plt.title("lineplot with estimator sum")
plt.show()

sns.lineplot(data=train_df, x='Outlet_Year', y='Sales', hue='Outlet_Location_Type',errorbar=None, marker='o', markersize=4)
plt.title("lineplot with hue")
plt.show()
