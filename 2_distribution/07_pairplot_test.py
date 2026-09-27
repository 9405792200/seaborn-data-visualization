#Plot pairwise relationships for each numeric variable of dataset
#By default, this function will create a grid of Axes such that each numeric variable in data will by shared across the y-axes across a single row and the x-axes across a single column. 
#The diagonal plots are treated differently: a univariate distribution plot is drawn to show the marginal distribution of the data in each column.
#It is also possible to show a subset of variables or plot different variables on the rows and columns.

import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

iris_df = pd.read_csv("iris.csv")

sns.pairplot(data=iris_df) #Basic pairplot(), by default diagonal element is histogram & non diagonal element is scatter plot
plt.show()

#diag_kind : {‘auto’, ‘hist’, ‘kde’, None} by default it is auto.The property is for diagonal element
sns.pairplot(data=iris_df, diag_kind='kde') #Basic pairplot(),with diagonal element is kde.
plt.show()

sns.pairplot(data=iris_df, diag_kind=None) #Basic pairplot(),with diagonal element as None.
plt.show()

#kind : {‘scatter’, ‘kde’, ‘hist’, ‘reg’} by default it is scatter.This property is for non diagonal element
sns.pairplot(data=iris_df, kind="reg") #basic pairplot(), with non diagonal element as regression 
plt.show()

sns.pairplot(data=iris_df, kind="kde") #basic pairplot(), with non diagonal element as kde 
plt.show()

sns.pairplot(data=iris_df, kind='hist') #basic pairplot(), with non diagonal element as histogram
plt.show()

sns.pairplot(data=iris_df, hue='species', diag_kind='hist',diag_kws=dict(multiple='stack')) 
#hue for group by & diag_kws Dictionaries of keyword arguments for diagonal element 
plt.show()

sns.pairplot(data=iris_df, x_vars=['sepal_length','sepal_width','petal_length'], 
                           y_vars=['petal_length','petal_width'])
#To plot pairplot() with specific list of variables on x-axis & y-axis using x_vars & y_vars
plt.show()

sns.pairplot(data=iris_df, diag_kws=dict(color='red', kde=True), plot_kws=dict(color='Green'))
#diag_kws Dictionaries of keyword arguments for diagonal element, plot_kws Dictionaries of keyword arguments for non diagonal element
plt.show()