#Draw a combination of boxplot and kernel density estimate
#it is combination of Box plot and Kernal Density plot

import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt 

supermarket_df = pd.read_excel("supermarket_sales.xlsx")

sns.violinplot(y='Total', data=supermarket_df) # To plot basic violinplot
plt.title("Violin Plot")
plt.show()

sns.violinplot(data=supermarket_df, x="Payment", y="Total") #To plot violinplot of two categories one string , another numeric
plt.title("Violin Plot Of Two Categories")
plt.show()

sns.violinplot(data=supermarket_df, x="Payment", y="Total", hue='Gender', hue_order=['Male','Female'], split=True, cut=0) 
#To plot violinplot of two categories one string , another numeric with group by gender
#setting split to True will draw half of a violin for each level, split can be used on exact two hue level
#cut to cut extreme datapoints of violin
plt.title("Violin Plot Of Two Categories With hue")
plt.show()