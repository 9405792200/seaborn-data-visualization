import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

#heatmap=> "it is graphical representation of data where values are represented by color"

supermarket_df = pd.read_excel("supermarket_sales.xlsx")

mean_supermarket_pivot = pd.pivot_table(data=supermarket_df, index='Product line',columns='City', values='Total', aggfunc='mean')

print(mean_supermarket_pivot)

sns.heatmap(data=mean_supermarket_pivot) #heatmap work on pivot data. i.e data in matrix format
plt.title("Basic heatmap")
plt.show()

sns.heatmap(data=mean_supermarket_pivot, annot=True, fmt='0.2f') #To write the data value in each cell with float format 
plt.title("Heatmap with cell value")
plt.show()

sns.heatmap(data=mean_supermarket_pivot, annot=True, fmt='0.2f', linewidth=0.5) #Width of the lines that will divide each cell
plt.title("Heatmap with cell divide")
plt.show()