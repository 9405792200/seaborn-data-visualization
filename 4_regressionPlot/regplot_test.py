import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt 

#This regplot() is used to plot data and a linear regression model fit. There are a number of mutually exclusive options for estimating the regression model

#tips_df = sns.load_dataset("tips") # To load tips dataset 
#tips_df.to_csv("tips.csv", index=False) #To store it in csv file

tips_df = pd.read_csv("tips.csv")

sns.regplot(data=tips_df, x='total_bill', y='tip', ci=None) #To plot basic regression plot
plt.title("basic regplot")
plt.show()

sns.regplot(data=tips_df, x='total_bill', y='tip', ci=None, line_kws=dict(color='red'), scatter_kws=dict(color='pink'))
plt.title("regplot with line & scatter property")
plt.show()

