import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt 

supermarket_df = pd.read_excel('supermarket_sales.xlsx')

sns.countplot(x='Product line', data=supermarket_df)
#Show the counts of observations in each categorical bin using bars  x, y, hue names of column in dataframe or vector data, optional
plt.title("Transaction Count")
plt.show()

sns.countplot(x='Product line', data=supermarket_df, hue='Gender')
#To get count of two categories,i.e product line with respective Gender 
plt.title("Transaction Count Male & Female")
plt.show()