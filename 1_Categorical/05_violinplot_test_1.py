#Draw a combination of boxplot and kernel density estimate
#it is combination of Box plot and Kernal Density plot

import matplotlib.pyplot as plt
import seaborn as sns

num = [8,11,13,17,19,21,23,26,29,31,35,40]

sns.violinplot(data=num)# To plot violinplot 

plt.title("Violin Plot")
plt.show()
