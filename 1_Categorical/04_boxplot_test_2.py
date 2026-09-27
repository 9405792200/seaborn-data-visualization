#A boxplot is a graphical and standardised way to display the distribution of data based on six key numbers:
#1) minimum
#2) 1st Quartile (25th percentile) Q1
#3) median (2nd Quartile/ 50th Percentile) Q2 (middle of sorted list)
#4) 3rd Quartile (75th percentile) Q3
#5) maximum
#6) mean value

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 

supermarket_df = pd.read_excel('supermarket_sales.xlsx')

sns.boxplot(data=supermarket_df, x='Payment', y='Total', showmeans=True)
#To plot boxplot Payment Vs Total to show min,Q1,Q2(median),Q3,max & outliers 
plt.title("Supermarket Data")
plt.show()

sns.boxplot(data=supermarket_df, x='Payment', y='Total', hue='Gender', hue_order=['Male','Female'],showmeans=True)
#To plot boxplot Payment Vs Total to group by gender to show min,Q1,Q2(median),Q3,max & outliers 

plt.title("Supermarket Data Male & Female")
plt.show()