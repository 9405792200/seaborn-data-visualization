#Plot empirical cumulative distribution functions
#An ECDF represents the proportion or count of observations falling below each unique value in a dataset

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

supermarket_df = pd.read_excel("supermarket_sales.xlsx")

sns.ecdfplot(data=supermarket_df, x='Total') #basic ecdfplot()
plt.title("Basic ecdfplot for Total")
plt.show()

sns.ecdfplot(data=supermarket_df, x='Total', hue='Payment') #ecdfplot() with group by Gender
plt.title("ecdfplot for Total with payment")
plt.show()

sns.ecdfplot(data=supermarket_df, x='Total', hue='Payment', stat='count') #ecdfplot() with group by Gender with stat as count
#stat - “proportion”, “count” Distribution statistic to compute.
plt.title("ecdfplot for Total with payment count")
plt.show()