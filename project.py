import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#import the csv file(dataset)
data=pd.read_csv('phone_usage_india.csv')

#confirm csv file has imported
print(data.head(15))

#get dataset information
print(data.info())

#--------------------------------------------------------

#Dealing with Null values

#drop rows without User ID
print("No. of null values in User ID:",data["User ID"].isnull().sum())
data=data["User ID"].dropna()







