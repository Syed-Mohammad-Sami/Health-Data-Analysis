#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt

# Simulating a sample dataset for demonstration
data = {
    'Age': [25, 30, 45, 50, 65, 70, 22, 35, 60, 40, 55, 48],
    'BMI': [22.4, 28.5, 26.1, 30.0, 27.5, 31.2, 19.8, 24.5, 29.9, 25.1, 23.3, 28.0],
    'BloodPressure': [120, 130, 135, 145, 150, 160, 110, 125, 140, 135, 130, 138],
    'Cholesterol': [1, 2, 2, 3, 3, 2, 1, 1, 3, 2, 1, 2]
}

df = pd.DataFrame(data)

# Display the first few rows of the dataframe
print("First 5 rows of the dataset:")
print(df.head())

# Check the data types and for any missing values
print("\nData types and missing values:")
print(df.info())

# Basic statistics for numerical columns
print("\nDescriptive statistics:")
print(df.describe())

# Handling missing values (fill with mean for numerical columns)
df.fillna(df.mean(), inplace=True)

# Visualize the distribution of BMI
plt.figure(figsize=(10, 6))
plt.hist(df['BMI'], bins=30, alpha=0.7, color='blue')
plt.title('BMI Distribution')
plt.xlabel('BMI')
plt.ylabel('Frequency')
plt.grid(axis='y')
plt.show()

# Correlation matrix
correlation_matrix = df.corr()

# Plotting the correlation matrix
plt.figure(figsize=(10, 8))
plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='none')
plt.colorbar()
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=45)
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
plt.title('Correlation Heatmap')
plt.show()

# Age vs. Blood Pressure scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Age'], df['BloodPressure'], c=df['Cholesterol'], cmap='coolwarm', alpha=0.6)
plt.colorbar(label='Cholesterol Level')
plt.title('Age vs. Blood Pressure')
plt.xlabel('Age')
plt.ylabel('Blood Pressure')
plt.show()

# Boxplot of BMI by Cholesterol levels (manual creation)
cholesterol_levels = df['Cholesterol'].unique()
plt.figure(figsize=(10, 6))
for i, level in enumerate(cholesterol_levels):
    plt.boxplot(df[df['Cholesterol'] == level]['BMI'], positions=[i], widths=0.6)

plt.xticks(range(len(cholesterol_levels)), cholesterol_levels)
plt.title('BMI by Cholesterol Levels')
plt.xlabel('Cholesterol Level')
plt.ylabel('BMI')
plt.show()

# Group by and summarize average BMI and Blood Pressure by Age group
age_bins = [0, 18, 35, 50, 65, 100]
age_labels = ['0-18', '19-35', '36-50', '51-65', '66+']
df['AgeGroup'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels)

age_summary = df.groupby('AgeGroup')[['BMI', 'BloodPressure']].mean()
print("\nAverage BMI and Blood Pressure by Age Group:")
print(age_summary)


# In[ ]:




