#!/usr/bin/env python
# coding: utf-8

# # OMNIFY (DATA ANALYST INTERN ASSESSMENT)

# - Objective: The goal of this assignment is to assess your data analysis, 
# problem-solving, and visualization skills. Please ensure your submission 
# is clear, well-structured, and includes relevant insights.
# 

# #### Importing the necessary libraries

# In[6]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# #### Loading the dataset

# In[8]:


# Have converted excel file to csv file
df = pd.read_csv("C:/Users/yasha/Downloads/DataAnalyst_Assesment_Dataset.csv")


# #### Basic Checks

# In[9]:


df.head() # Prints first 5 rows of the dataset


# In[10]:


df.tail() # prints last 5 rows of the dataset


# In[11]:


# Basic information of the data present in dataset
print("Data Information: ")
df.info()


# ##### Here we get to know the datatypes of the columns present in dataset along with their count, missing values and also shows total number of rows present and memory usage.

# ### Statistical Summary of Data

# In[13]:


print("Statistical Summary: ") # only useful for numeric datatype
df.describe()


# ### EXPLORATORY DATA ANALYSIS

# #### Checking if any missing values present

# In[16]:


print("Missing Values with respect to each column: ")
df.isnull().sum()


# ##### We have seen that some of the columns are having missing values.

# #### Step 1 : Handling Missing Values

# In[18]:


# The column "Subscription Type" has 100% missing values. So let's drop this column.
df.drop(columns = ["Subscription Type"], inplace = True)


# In[19]:


# Filling the missing values with median in "Duration(mins)" columns
df["Duration (mins)"].fillna(df["Duration (mins)"].median(), inplace=True)


# In[20]:


# Replacing missing instructors with 'Unknown' or 'Not Specified'
df["Instructor"].fillna("Unknown", inplace=True) 
df["Class Type"].fillna("Not Specified", inplace=True)
df["Facility"].fillna("Not Specified", inplace=True)
df["Theme"].fillna("Not Specified", inplace=True)
df["Time Slot"].fillna("Unknown", inplace=True)


# In[22]:


# Filling missing Customer Email/Phone with "Not Provided"
df["Customer Email"].fillna("Not Provided", inplace=True)
df["Customer Phone"].fillna("Not Provided", inplace=True)


# In[23]:


df.head(10) # checking the data 


# #### Step 2 : Removing Duplicates

# In[27]:


df.drop_duplicates(inplace=True)


# In[28]:


df.shape


# #### Step 3 : Standardizing Categorical Data

# In[29]:


df["Status"] = df["Status"].str.capitalize()
df["Booking Type"] = df["Booking Type"].str.title()


# In[30]:


df.head()


# #### Step 4 : Checking for Anomalies

# In[31]:


# Here we are checking if we have negative prices or durations
df = df[df["Price"] > 0]
df = df[df["Duration (mins)"] > 0]


# In[32]:


# Convert 'Booking Date' to datetime format 
df["Booking Date"] = pd.to_datetime(df["Booking Date"])


# In[34]:


df.head(10)


# In[36]:


# checking the unique types with their frequency for "Booking Type" and "Status" columns.
print("\nUnique Booking Types:\n", df["Booking Type"].value_counts())
print("\nUnique Status:\n", df["Status"].value_counts())


# ### Data Visualization

# In[38]:


# Visualization 1: Booking Type Distribution
plt.figure(figsize=(10,5))
sns.countplot(data=df, x="Booking Type", palette="viridis")
plt.xticks(rotation=45)
plt.title("Distribution of Booking Types")
plt.show()


# In[39]:


# Visualization 2: Booking Status Breakdown
plt.figure(figsize=(7,5))
df["Status"].value_counts().plot.pie(autopct="%1.1f%%", colors=["lightblue", "lightcoral", "lightgreen"])
plt.title("Booking Status Distribution")
plt.ylabel("")
plt.show()


# In[40]:


# Visualization 3: Price Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["Price"], bins=30, kde=True, color="teal")
plt.title("Price Distribution")
plt.show()


# In[41]:


# Visualization 4: Monthly Booking Trend
df["Month"] = df["Booking Date"].dt.to_period("M")
monthly_counts = df.groupby("Month")["Booking ID"].count()
plt.figure(figsize=(10,5))
monthly_counts.plot(marker="o", color="blue")
plt.title("Monthly Booking Trend")
plt.xlabel("Month")
plt.ylabel("Number of Bookings")
plt.xticks(rotation=45)
plt.show()


# In[44]:


# Final Cleaned Dataset 
df.to_csv("C:/Users/yasha/Downloads/DataAnalyst_Assesment_Dataset.csv", index=False)


# In[45]:


print("Data Cleaning & Analysis Completed! Cleaned dataset saved.")


# ### Conclusion

# Here for the given dataset, we have done the following points to perform EDA: 
# - Cleaned the dataset (handles missing values, duplicates, and anomalies).
# - Standardized the  categorical values (fixing inconsistencies).
# - Performed basic exploratory data analysis (EDA).
# - Created interactive visualizations to analyze key trends.
# - Saved the cleaned dataset for dashboard creation.

# In[ ]:




