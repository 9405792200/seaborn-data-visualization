#swarmplot is categorical scatterplot with points adjusted to be non-overlapping
#swarmplot is similar to stripplot(),but the points are adjusted so that they don’t overlap. 
#It will represent each of the data points on the plot without overlapping
#"A swarmplot can be drawn on its own, but it is also a good complement to a box or violin plot in cases where you want to show 
#all observations along with some representation of the underlying distribution"

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 

supermarket_df = pd.read_excel(r"supermarket_sales.xlsx")

sns.swarmplot(data=supermarket_df, y='Total') #To plot basic swarmplot 
plt.title("Basic swarmplot")
plt.show()

sns.swarmplot(data=supermarket_df, x='Payment', y='Total') #To plot swarmplot between two categories 
plt.title("Complex swarmplot")
plt.show()

sns.swarmplot(data=supermarket_df, x='Payment', y='Total', hue='Gender')
#To plot swarmplot between two categories & group by Gender
plt.title("swarmplot with group by")
plt.show()

sns.swarmplot(data=supermarket_df, x='Payment', y='Total', hue='Gender', dodge=True)
#dodge setting this to True will separate the strips for different hue levels along the categorical axis. 
#Otherwise, the points for each level will be plotted on top of each other.
plt.title("swarmplot with dodge")
plt.show()

#To overlay swarmplot on boxplot
sns.swarmplot(data=supermarket_df, x='Payment', y='Total',color='red')
sns.boxplot(data=supermarket_df, x='Payment', y='Total')
plt.title("swarmplot & boxplot overlay")
plt.show()

#To overlay swarmplot on violinplot
sns.swarmplot(data=supermarket_df, x='Payment', y='Total', color='red')
sns.violinplot(data=supermarket_df, x='Payment', y='Total')
plt.title("swarmplot & violinplot overlay")
plt.show()