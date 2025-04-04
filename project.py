import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#import the csv file(dataset)
data=pd.read_csv('phone_usage_india.csv')

#confirm csv file has imported
print("First few lines of Dataset: ")
print(data.head(15))

#get dataset information
print("Information about data: ")
print(data.info())

#Get the Summary statistic description
print("Statistical Description:")
print(data.describe())

#--------------------------------------------------------

#Dealing with Null values

#drop rows without User ID
print("No. of null values in User ID:",data["User ID"].isnull().sum())
data=data.dropna(subset='User ID')

data=data.dropna(subset='Screen Time (hrs/day)')

#Replacing null values in other colums null values with mean/mode/median

data['Data Usage (GB/month)']=data['Data Usage (GB/month)'].fillna(data['Data Usage (GB/month)'].median())
data['Calls Duration (mins/day)']=data['Calls Duration (mins/day)'].fillna(data['Calls Duration (mins/day)'].mean())
data['Number of Apps Installed']=data['Number of Apps Installed'].fillna(data['Number of Apps Installed'].mode().iloc[0])
data['Social Media Time (hrs/day)']=data['Social Media Time (hrs/day)'].fillna(data['Social Media Time (hrs/day)'].mean())
data['E-commerce Spend (INR/month)']=data['E-commerce Spend (INR/month)'].fillna(data['E-commerce Spend (INR/month)'].mean())
data['Streaming Time (hrs/day)']=data['Streaming Time (hrs/day)'].fillna(data['Streaming Time (hrs/day)'].median())
data['Gaming Time (hrs/day)']=data['Gaming Time (hrs/day)'].fillna(0)
data['Monthly Recharge Cost (INR)']=data['Monthly Recharge Cost (INR)'].fillna(data['Monthly Recharge Cost (INR)'].mode().iloc[0])


data.to_csv('phone_usage_india.csv',index=False)

#-------------------------------------------------------------------------







