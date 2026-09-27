import seaborn as sns
import pandas as pd

dataset_name = sns.get_dataset_names() #Provide inbuilt dataset names available in seaborn
print(dataset_name)

iris_df = sns.load_dataset(name='iris') #Load an name dataset from the online repository 

iris_df.to_csv("iris.csv",index=False)

print("File Saved!!!")
