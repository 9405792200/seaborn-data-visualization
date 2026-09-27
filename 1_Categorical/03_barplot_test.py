#A barplot is basically used to aggregate the categorical data according to some methods and by default it’s the mean. 
#Method is provided by estimator parameter = 'Mean'/np.sum/np.median e.t.c
#It can also be understood as a visualization of the group by action. 
#To use this plot we choose a categorical column for the x-axis and a numerical column for the y-axis, 
#and we see that it creates a plot taking a default mean per categorical column.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

#print(sns.get_dataset_names()) # To get all inbuild dataset names in seaborn
#print(sns.load_dataset('diamonds'))#To read dataset diamonds 

supermarket_df = pd.read_excel('supermarket_sales.xlsx')
supermarket_df.sort_values(by='Product line', inplace=True)

sns.barplot(x='Product line', y='Total', errorbar=None, data=supermarket_df)
#A barplot is basically used to aggregate the categorical data according to some methods and by default it’s the mean
#Method is provided by estimator parameter = 'Mean'/np.sum/np.median e.t.c
#errorbar to remove error bar
plt.title("Product line & Total Mean")
plt.show()

sns.barplot(x='Product line', y='Total', hue='Gender', errorbar=None, estimator=np.median ,data=supermarket_df)
#A barplot is basically used to aggregate the categorical data according to some methods and by default it’s the mean
#Method is provided by estimator parameter = 'Mean'/np.sum/np.median e.t.c
#errorbar to remove error bar, hue to group by
plt.title("Product line & Total Per Gender")
plt.show()