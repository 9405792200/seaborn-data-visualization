#Draw a plot of two variables with bivariate and univariate graphs.By defauit it is combination of scatter plot & marginal distribution   
#This function provides a convenient interface to the JointGrid class,with several canned plot kinds. 
#This is intended to be a fairly lightweight wrapper; if you need more flexibility, you should use JointGrid directly
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

supermarket_df = pd.read_excel("supermarket_sales.xlsx")

sns.jointplot(data=supermarket_df, x='Unit price', y='Total') #For basic jointplot()
plt.title("Basic jointplot")
plt.show()

#kind : { “scatter” | “kde” | “hist” | “hex” | “reg” | “resid” } by default it is scatter
sns.jointplot(data=supermarket_df, x='Unit price', y='Total', kind='kde') #kind for kde plot
plt.title("jointplot with kind kde")
plt.show()

sns.jointplot(data=supermarket_df, x='Unit price', y='Total', kind='hist') #kind for histogram plot
plt.title("jointplot with kind hist")
plt.show()

sns.jointplot(data=supermarket_df, x='Unit price', y='Total', kind='hex') #kind for hex plot
plt.title("jointplot with kind hex")
plt.show()

sns.jointplot(data=supermarket_df, x='Unit price', y='Total', kind='reg',color='red') #kind for regression line
plt.title("jointplot with kind reg")
plt.show()

sns.jointplot(data=supermarket_df, x='Unit price', y='Total', kind='resid')
plt.title("jointplot with kind resid")
plt.show()

sns.jointplot(data=supermarket_df, x='Unit price', y='Total', hue='Gender') #with groupby gender
plt.title("jointplot with groupby")
plt.show()

sns.jointplot(data=supermarket_df, x='Unit price', y='Total', joint_kws=dict(color='red', marker='+'))
#joint_kws to set property of jointplot
plt.title("jointplot with joint_kws")
plt.show()

sns.jointplot(data=supermarket_df, x='Unit price', y='Total', marginal_kws=dict(color='red'))
#marginal_kws to set property of marginal distribution
plt.title("jointplot with marginal_kws")
plt.show()

#To plot jointplot with rugplot & kdeplot
sns.jointplot(data=supermarket_df, x='Unit price', y='Total')
sns.rugplot(data=supermarket_df, x='Unit price', y='Total')
sns.kdeplot(data=supermarket_df, x='Unit price', y='Total')
plt.title("jointplot with rugplot & kdeplot")
plt.show()

