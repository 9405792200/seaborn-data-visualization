#displot() - Distribution plot function provides access to several approaches for visualizing the univariate or bivariate distribution of data, 
#including subsets of data defined by semantic mapping and faceting across multiple subplots. 
#The kind parameter selects the approach to use kind{“hist”, “kde”, “ecdf”}. hist for histplot(), kde for kdeplot(), ecdf for ecdfplot()

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 

supermarket_df = pd.read_excel("supermarket_sales.xlsx")

sns.displot(data=supermarket_df, x='Total', kde=True, rug=True, rug_kws={"height":0.05}) #displot() with kde & rug 
plt.title("displot with kde & rug")
plt.show()

sns.displot(data=supermarket_df, x='Total', kde=True, rug=True, hue='Payment', multiple='stack')
plt.title("displot with kde & rug & hue")
plt.show()

sns.displot(data=supermarket_df, x='Total', kde=True, rug=True, hue='Payment', multiple='stack', col='Gender') 
#displot with kde & rug & hue & col. col will divide figure in number of columns 
plt.show()

sns.displot(data=supermarket_df, x='Total', kde=True, rug=True, hue='Payment', multiple='stack', col='Gender', row='Branch') 
#displot with kde & rug & hue & col. col & row will divide figure in number of rows*columns 
plt.show()

sns.displot(data=supermarket_df, x='Total', rug=True, hue='Payment', col='Gender', row='Branch', kind='ecdf', rug_kws={"height":0.2}) 
#displot with kde & rug & hue & col. col & row will divide figure in number of rows*columns based on different values of it.
plt.show()