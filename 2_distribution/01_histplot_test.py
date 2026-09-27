#"A histogram is a classic visualization tool that represents the distribution of one or more variables 
# by counting the number of observations that fall within discrete bins"
import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np

supermarket_df = pd.read_excel("supermarket_sales.xlsx")

sns.histplot(data=supermarket_df, x='Total') #To plot basic histogram
plt.title("Distribution of Total")
plt.show()

sns.histplot(data=supermarket_df, x='Total', binwidth=100) #binwidth represents width of each bin
plt.title("Binwidth Test 100 ")
plt.show()

sns.histplot(data=supermarket_df, x='Total', bins=np.arange(0,1100,50)) #Total number of bins in histogram
plt.xticks(np.arange(0,1100,50))
plt.title("Bins parameter test 22")
plt.show()

sns.histplot(data=supermarket_df, x='Total', kde=True) #kde is used compute a kernel density estimate
plt.title("KDE test with histplot")
plt.show()

sns.histplot(data=supermarket_df, x='Total', hue='Gender', multiple='stack') 
#To plot histplot male female on each other using hue & multiple as stack. option for multiple{“layer”, “dodge”, “stack”, “fill”}
plt.title("histplot with hue") 
plt.show()

sns.histplot(data=supermarket_df, x='Total', hue='Gender', element='step', multiple='stack')
#To plot histplot element is used Visual representation of the histogram statistic {“bars”, “step”, “poly”}
plt.title("histplot with element step")
plt.show()