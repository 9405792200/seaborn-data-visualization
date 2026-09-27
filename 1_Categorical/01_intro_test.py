import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt

supermarket_df=pd.read_excel('supermarket_sales.xlsx')

sns.countplot(x='Gender', data=supermarket_df) 
#Show the counts of observations in each categorical bin using bars, x, y, huenames of variables in data or vector data, optional

plt.xlabel("Sex")
plt.ylabel("Frequency")
plt.title("SuperMarket Sale")

plt.show()