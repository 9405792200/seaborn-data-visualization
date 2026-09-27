import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

#Multi-plot grid for plotting conditional relationships

supermarket_df = pd.read_excel("supermarket_sales.xlsx")

multigridpanel = sns.FacetGrid(data=supermarket_df, col='Payment') #it will return multigrid panel which divide into column 
#Note:->"multigridpanel helps in visualizing distribution of one variable as well as 
#the relationship between multiple variables separately within subsets of your dataset using multiple panels"

#To map_dataframe we can provide any plot of type 
#1)Categorical -  countplot,barplot,boxplot,violinplot,stripplot,swarmplot
#2)Distribution - histplot, kdeplot, ecdfplot
#3)Relational -   scatterplot, lineplot
#4)Regression -   regplot

multigridpanel.map_dataframe(sns.countplot, x='City')
plt.title("FacetGrid countplot")
plt.show()

multigridpanel = sns.FacetGrid(data=supermarket_df, col='Payment') #it will return multigrid panel
multigridpanel.map_dataframe(sns.histplot, x='Total')
plt.title("FacetGrid histplot")
plt.show()

multigridpanel = sns.FacetGrid(data=supermarket_df, col='Payment') #it will return multigrid panel
multigridpanel.map_dataframe(sns.kdeplot, x='Total')
plt.title("FacetGrid kdeplot")
plt.show()

multigridpanel = sns.FacetGrid(data=supermarket_df, col='Payment') #it will return multigrid panel
multigridpanel.map_dataframe(sns.lineplot, x='City', y='Total', errorbar=None)
plt.title("FacetGrid lineplot")
plt.show()

multigridpanel = sns.FacetGrid(data=supermarket_df, col='Payment') #it will return multigrid panel
multigridpanel.map_dataframe(sns.scatterplot, x='City', y='Total')
plt.title("FacetGrid scatterplot")
plt.show()

multigridpanel = sns.FacetGrid(data=supermarket_df, col='Payment', row='Gender', sharey=False) #it will return multigrid panel which divide into column * row 
multigridpanel.map_dataframe(sns.histplot, x='Total')
plt.title("FacetGrid histplot")
plt.show() 



