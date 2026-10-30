import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("sales.csv")

# Display first five records
print("First Five Records:")
print(df.head())

# Total and average sales
print("\nTotal Sales:", df["Sales"].sum())
print("Average Sales:", df["Sales"].mean())

# Month with highest sales
print("\nMonth with Highest Sales:")
print(df.loc[df["Sales"].idxmax()])

# Group sales by product category
category_sales = df.groupby("Category")["Sales"].sum()
print("\nSales by Product Category:")
print(category_sales)

# Bar chart: Category-wise sales
category_sales.plot(kind="bar")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.title("Sales by Product Category")
plt.tight_layout()
plt.show()

# Line chart: Monthly sales trends
monthly_sales = df.groupby("Month")["Sales"].sum()
monthly_sales.plot(kind="line", marker="o")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Monthly Sales Trend")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Pie chart: Category contribution
category_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Category-wise Sales Contribution")
plt.ylabel("")
plt.show()