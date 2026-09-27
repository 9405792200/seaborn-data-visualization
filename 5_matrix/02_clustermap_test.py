import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt 

#Plot a matrix dataset as a hierarchically-clustered heatmap

supermarket_df = pd.read_excel("supermarket_sales.xlsx")

supermarket_pivot = pd.pivot_table(data=supermarket_df, index='Product line', columns='City', values='Total')
print(supermarket_pivot)

sns.clustermap(data=supermarket_pivot, annot=True, fmt='0.2f')
plt.title("Basic clustermap")
plt.show()

sns.clustermap(data=supermarket_pivot, row_cluster=False,annot=True, fmt='0.2f') #To remove row level clustered
plt.title("clustermap with row false")
plt.show()

sns.clustermap(data=supermarket_pivot, col_cluster=False, annot=True, fmt='0.2f') #To remove column level clustered
plt.title("clustermap with columns false")
plt.show()

sns.clustermap(data=supermarket_pivot, row_cluster=False ,col_cluster=False, annot=True, fmt='0.2f') #To remove row & column level clustered
plt.title("clustermap with row columns false")
plt.show()