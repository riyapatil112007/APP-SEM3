import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("customer_churn.csv")

# Display first five records
print("First Five Records:")
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Dataset shape
print("\nDataset Shape:", df.shape)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate records
print("\nDuplicate Records:", df.duplicated().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Handle missing values
for col in df.select_dtypes(include=np.number).columns:
    df[col] = df[col].fillna(df[col].median())

for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# Remove extra spaces and standardize text
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

# Display cleaned dataset
print("\nCleaned Dataset:")
print(df.head())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Churn distribution
if "Churn" in df.columns:
    print("\nCustomer Churn Count:")
    print(df["Churn"].value_counts())

    # Bar chart
    df["Churn"].value_counts().plot(kind="bar")
    plt.title("Customer Churn Distribution")
    plt.xlabel("Churn")
    plt.ylabel("Number of Customers")
    plt.show()

# Numerical column distribution
numeric_cols = df.select_dtypes(include=np.number).columns

if len(numeric_cols) > 0:
    df[numeric_cols[0]].hist()
    plt.title("Numerical Data Distribution")
    plt.xlabel(numeric_cols[0])
    plt.ylabel("Frequency")
    plt.show()

# Correlation heatmap
if len(numeric_cols) > 1:
    sns.heatmap(df[numeric_cols].corr(),
                annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()

# Grouping analysis
if "Churn" in df.columns and len(numeric_cols) > 0:
    print("\nAverage Numerical Values by Churn:")
    print(df.groupby("Churn")[numeric_cols].mean())

# Save cleaned dataset
df.to_csv("cleaned_customer_churn.csv", index=False)

print("\nEDA Completed Successfully!")