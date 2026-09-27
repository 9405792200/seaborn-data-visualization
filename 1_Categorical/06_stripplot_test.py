#stripplot is categorical scatterplot by using jitter to reduce overplotting
#"A strip plot can be drawn on its own, but it is also a good complement to a box or violin plot in cases where you want to show 
#all observations along with some representation of the underlying distribution"

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 

supermarket_df = pd.read_excel("supermarket_sales.xlsx")

sns.stripplot(data=supermarket_df, y='Total') # To create basic stripplot
plt.title("Stripplot Test")
plt.show()

sns.stripplot(data=supermarket_df, x='Payment', y='Total', color='red') # To create stripplot for two categories
plt.title("Stripplot Test Payment & Total")
plt.show()

sns.stripplot(data=supermarket_df, x='Payment', y='Total', hue='Gender', jitter=0.2) 
#To create stripplot for two categories group by third variable 
#jitter can be useful when you have many points and they overlap, so that it is easier to see the distribution
plt.title("Stripplot Test Payment & Total with Gender")
plt.show()

sns.stripplot(data=supermarket_df, x='Payment', y='Total', hue='Gender', jitter=0.2, dodge=True) 
#dodge setting this to True will separate the strips for different hue levels along the categorical axis. 
#Otherwise, the points for each level will be plotted on top of each other.
plt.title("Stripplot Test Payment & Total Seperate with Gender")
plt.show()

sns.stripplot(data=supermarket_df, x='Payment', y='Total', hue='Gender', dodge=True) 
sns.boxplot(data=supermarket_df, x='Payment', y='Total', hue='Gender')
plt.title("Stripplot Test Payment & Total Seperate with Gender Boxplot")
plt.show()

sns.stripplot(data=supermarket_df, x='Payment', y='Total', hue='Gender', dodge=True) 
sns.violinplot(data=supermarket_df, x='Payment', y='Total', hue='Gender',cut=0)
plt.title("Stripplot Test Payment & Total Seperate with Gender violinplot")
plt.show()