import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the data
for dirname, _, filenames in os.walk('C:\\Users\\solva\\Desktop\\Health Compus'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
df = pd.read_csv('C:\\Users\\solva\\Desktop\\Health Compus\\Student health Data.csv')

print(df.columns)

# Drop rows with missing values
df = df.dropna()

print(df.columns)

# Data Visualization

# Age distribution
# plt.figure(figsize=(10, 6))
# plt.hist(df['Age'], color='b', bins=20)
# plt.title("Age Distribution")
# plt.xlabel("Age")
# plt.ylabel("Frequency")
# plt.show()

# Gender distribution
plt.figure(figsize=(8, 8))
plt.title("Gender Distribution")
df['Choose your gender'].value_counts().plot.pie(autopct='%1.1f%%', colors=['skyblue', 'navajowhite'])
plt.ylabel('')
plt.show()

# Spectacles usage
plt.figure(figsize=(8, 6))
sns.countplot(x='Do You Wear Spectacles?', data=df)
plt.title("Spectacles Usage")
plt.xlabel("Wear Spectacles")
plt.ylabel("Count")
plt.show()

# Food preference
plt.figure(figsize=(8, 6))
sns.countplot(x='Food Preference', data=df)
plt.title("Food Preference")
plt.xlabel("Preference")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# Hospital visit
plt.figure(figsize=(8, 6))
sns.countplot(x='Have you visited CU hospital recently?', data=df)
plt.title("Hospital Visit")
plt.xlabel("Visited CU hospital")
plt.ylabel("Count")
plt.show()

# Purpose of hospital visit
plt.figure(figsize=(10, 6))
sns.countplot(y='Purpose of visiting hospital', data=df)
plt.title("Purpose of Hospital Visit")
plt.xlabel("Count")
plt.ylabel("Purpose")
plt.show()

# Referral to another hospital
plt.figure(figsize=(8, 6))
sns.countplot(x='Were you referred to Another Hospital ?', data=df)
plt.title("Referral to Another Hospital")
plt.xlabel("Referred to Another Hospital")
plt.ylabel("Count")
plt.show()

# Satisfaction with CU hospital
plt.figure(figsize=(8, 6))
sns.countplot(x='Has CU hospital helped you?', data=df)
plt.title("Satisfaction with CU Hospital")
plt.xlabel("Satisfaction")
plt.ylabel("Count")
plt.show()

# Medical leave from CU hospital
plt.figure(figsize=(8, 6))
sns.countplot(x='Have you received medical leave from cu hospital?', data=df)
plt.title("Medical Leave from CU Hospital")
plt.xlabel("Received Medical Leave")
plt.ylabel("Count")
plt.show()

# Sleep duration distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['How many hours do you sleep in a day?'], kde=True, bins=15)
plt.title("Sleep Duration Distribution")
plt.xlabel("Hours of Sleep")
plt.ylabel("Frequency")
plt.show()

# Mental exhaustion
plt.figure(figsize=(8, 6))
sns.countplot(x='Do you feel mentally exhausted sometimes?', data=df)
plt.title("Mental Exhaustion")
plt.xlabel("Feel Mentally Exhausted")
plt.ylabel("Count")
plt.show()

# Mental health rating
plt.figure(figsize=(8, 6))
sns.countplot(x='Rate your mental health on a scale of 1 to 5', data=df)
plt.title("Mental Health Rating")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

# Need for mental relaxation sessions
plt.figure(figsize=(8, 6))
sns.countplot(x='Do you need mental Relaxation Sessions', data=df)
plt.title("Need for Mental Relaxation Sessions")
plt.xlabel("Need Mental Relaxation Sessions")
plt.ylabel("Count")
plt.show()

# Blood group distribution
plt.figure(figsize=(8, 6))
sns.countplot(x='Blood Group', data=df)
plt.title("Blood Group Distribution")
plt.xlabel("Blood Group")
plt.ylabel("Count")
plt.show()

# Seasonal disease tracking
plt.figure(figsize=(10, 6))
sns.countplot(x='Seasonal Disease', data=df)
plt.title("Seasonal Disease Tracking")
plt.xlabel("Disease")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# Medication trends
plt.figure(figsize=(10, 6))
sns.countplot(x='Medication Trend', data=df)
plt.title("Medication Trends")
plt.xlabel("Trend")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# Precautions taken
plt.figure(figsize=(10, 6))
sns.countplot(x='Precautions Taken', data=df)
plt.title("Precautions Taken")
plt.xlabel("Precautions")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()
