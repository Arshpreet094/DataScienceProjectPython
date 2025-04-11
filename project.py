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

#Removing the duplicate rows
print("No. of dupicate rows: ",data.duplicated().sum())
data=data.drop_duplicates()

data.to_csv('phone_usage_india.csv',index=False)

#---------------------------------------------------------------------------

#Checking for Outliers using BoxPlot

sns.set(style="whitegrid")

plt.figure(figsize=(6, 5))
sns.boxplot(y=data['Number of Apps Installed'], color='skyblue', width=0.3, linewidth=2, fliersize=6)
plt.show()

plt.figure(figsize=(6, 5))
sns.boxplot(y=data['Calls Duration (mins/day)'], color='orange', width=0.3, linewidth=2, fliersize=6)
plt.show()

plt.figure(figsize=(6, 5))
sns.boxplot(y=data['Screen Time (hrs/day)'], color='cyan', width=0.3, linewidth=2, fliersize=6)
plt.show()

#No Outliers found

#----------------------------------------------------------------------------------

#Vizualising the relations

#Plotting barchart for phone brands an no. of usuers
print(data['Phone Brand'].unique())
print(data.groupby('Phone Brand')['User ID'].count())
plt.figure(figsize=(8,6))
sns.barplot(data=data.groupby('Phone Brand')['User ID'].count(),palette='Set2')
plt.title('Phone Brands used in India')
plt.xticks(rotation=45)
plt.xlabel('Phone Brands')
plt.ylabel('No. of users')
plt.show()

#Plotting BarChart for checking primary use
print(data['Primary Use'].unique())
df=data.groupby('Primary Use')['User ID'].count()
plt.figure(figsize=(8,6))
sns.barplot(data=df,palette='pastel',width=0.5)
plt.title("Primary Use of Mobile Phones")
plt.xlabel("Uses")
plt.ylabel("No. of users")
plt.show()

#Usage of phone on basis of gender PIE
gend_stime=data.groupby('Gender')['User ID'].count()
print("Avg Screen Time on the basis of Gender: ")
print(gend_stime)
plt.figure(figsize=(6,4))
plt.pie(gend_stime,labels=['Female','Male','Other'],autopct='%1.2f%%')
plt.title("Usage of Phone on the basis of gender")
plt.show()

#Mobile OS most preffered PIE
df=data.groupby('OS')['User ID'].count()
print("Mobile Phone OS")
print(df)
plt.figure(figsize=(6,4))
plt.pie(df,labels=['Android','iOS'],autopct='%1.2f%%',startangle=140)
plt.title("Mobile OS Used")
plt.axis('equal')
plt.show()

#Histogram for find mobile usage of different age groups
plt.figure(figsize=(8,6))
sns.histplot(data['Age'],bins=10,color='orange',kde=True)
plt.title("Phone usage for Age Groups")
plt.ylabel('Frequence')
plt.show()

#Horizontal Bar for Avg data usage in dfferent Location
plt.figure(figsize=(8,10))
loct=data.groupby('Location')['Data Usage (GB/month)'].mean()
plt.barh(data['Location'].unique(),loct,color=['skyblue','violet','cyan','orange','pink'])
plt.title("Average Data Usage for Cities")
plt.ylabel("Cities")
plt.xlabel("Data Usage Gb/month")
plt.show()

#-----------------------------------------------------------------------------------------

#Finding correlations using scatter charts and heatmaps

#Scatter chart 1
plt.figure(figsize=(8,6))
sns.scatterplot(data=data,x='Screen Time (hrs/day)',y='Data Usage (GB/month)',alpha=0.7,color='red')
plt.xscale('log')
plt.yscale('log')
plt.show()

#Scatter chart 2
plt.figure(figsize=(8,6))
sns.scatterplot(data=data,x='Screen Time (hrs/day)',y='Calls Duration (mins/day)',alpha=0.7,color='green')
plt.xscale('log')
plt.yscale('log')
plt.show()

#Correlation Matrix using Heatmaps
corr_matrix=data.corr(numeric_only=True)
plt.figure(figsize=(5,3))
sns.heatmap(corr_matrix,annot=True,cmap='Blues',fmt=".2f",linewidth=0.8)
plt.xticks(fontsize=4,rotation=45)
plt.yticks(fontsize=8)
plt.title("Correlation Matrix")
plt.show()


#------------------------------------------------------------------------------------------------------

#Extracting the major insights and Achieving objectives


#Objt_1:Maximum Mobile phone usage on the basis of age, city, and gender

age_1=data[(data['Age']<=20)]
age_2=data[(data['Age']>20) & (data['Age']<=50)]
age_3=data[(data['Age']>50)]
print(f"\n\n\nMobile phone user who are under 20 :{(age_1['Age'].count()/data['Age'].count())*100:.2f}%")
print(f"Mobile phone user who between 20 to 50 :{(age_2['Age'].count()/data['Age'].count())*100:.2f}%")
print(f"Mobile phone user who are above 50 :{(age_3['Age'].count()/data['Age'].count())*100:.2f}%\n")
print("Maximum phone users are between 20 and 50 years\n\n")


city=data.groupby('Location')['User ID'].count()
print("Loction wise usage of phones: ")
print(city)
print("\n")
print("City with maximum usage of phone:",city.idxmax(),"\n\n")


gender=data.groupby('Gender')['User ID'].count()
print("Majority of Mobile phone users are: ",gender.idxmax(),"\n\n")


#Objt_2:Analyzing the correlation between screen  timing,data usage,primary uses

corr_matrix=data.corr(numeric_only=True)
print("Correlation between Screen timings and other uses: ")
print(corr_matrix)
plt.figure(figsize=(5,3))
sns.heatmap(corr_matrix,annot=True,cmap='coolwarm',fmt=".2f",linewidth=0.8)
plt.xticks(fontsize=6,rotation=45)
plt.yticks(fontsize=8)
plt.title("Correlation Matrix")
plt.show()


#Objt_3:Understanding the variation usage across different primary usage categories
p_use=data.groupby('Primary Use')['Screen Time (hrs/day)'].mean()
print("\n\n",p_use)
print("\nThe mobile phone is primarily used for: ",p_use.idxmax())
plt.figure(figsize=(8,6))
sns.barplot(data=p_use,palette='deep',width=0.5)
plt.title("Primary Use of Mobile Phones")
plt.xlabel("Uses")
plt.ylabel("No. of users")
plt.show()


#Objt_4:Reccomendations for smart phone compaies to optimize their strategies
os_used=data.groupby('OS')['User ID'].count()
print("\n\n\nMost Widely used Mobile OS: ",os_used.idxmax())
plt.figure(figsize=(6,4))
plt.pie(os_used,labels=['Android','iOS'],autopct='%1.2f%%',colors=['violet','pink'],startangle=140)
plt.title("Mobile OS Used")
plt.axis('equal')
plt.show()

brand=data.groupby('Phone Brand')['User ID'].count()/data['User ID'].count() *100
print("Mobile phone brands used are (percentage of users): ")
print(brand)
print("The most preffered brand is ",brand.idxmax())
plt.figure(figsize=(8,6))
sns.barplot(data=brand,palette='Set2',width=0.4)
plt.title('Phone Brands used in India')
plt.xticks(rotation=45)
plt.xlabel('Phone Brands')
plt.ylabel('No. of users')
plt.show()

#-------------------------XXXXXXXXXXXXXXXXXXXXXXXXXXXX---------------------------------------

