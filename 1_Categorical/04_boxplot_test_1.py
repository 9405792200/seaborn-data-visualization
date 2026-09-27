#A boxplot is a graphical and standardised way to display the distribution of data based on six key numbers:
#1) minimum
#2) 1st Quartile (25th percentile) Q1
#3) median (2nd Quartile/ 50th Percentile) Q2 (middle of sorted list)
#4) 3rd Quartile (75th percentile) Q3
#5) maximum
#6) mean value

#Draw a box plot to show distributions with respect to categories
#They provide us with a quick statistical summary of the data, 
#help us understand how data is distributed and help identify anomalous data points (outliers).

import matplotlib.pyplot as plt
import seaborn as sns

num = [8,11,13,17,19,21,23,26,29,31,35,40]

sns.boxplot(data=num, color='red',showmeans=True) # To plot Box with (minimum, Q1, median, Q3, maximum & outliers)
plt.title("Box Plot")
plt.show()

#IQR value = Q3 - Q1
#Range of a Outlier=[ Q1 - 1.5*IQR, Q3 + 1.5*IQR ]