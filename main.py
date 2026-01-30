import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import kagglehub

# Download latest version
path = kagglehub.dataset_download("mabubakrsiddiq/retail-store-product-sales-simulation-dataset")

print("Path to dataset files:", path)

# -------------------------------
# 1. Load CSV file
# -------------------------------
# Replace 'data.csv' with your file name
df = pd.read_csv("RetailStoreProductSalesDataset.csv")

# Display first few rows
print("First 5 rows of dataset:")
print(df.head())

# -------------------------------
# 2. Basic Data Analysis
# -------------------------------
print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# Select a numeric column for average calculation
column_name = df.select_dtypes(include='number').columns[0]
average_value = df[column_name].mean()

print(f"\nAverage of '{column_name}': {average_value}")

# -------------------------------
# 3. Bar Chart
# -------------------------------
plt.figure(figsize=(8, 5))
df[column_name].value_counts().head(10).plot(kind='bar')
plt.title(f"Bar Chart of {column_name}")
plt.xlabel(column_name)
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# -------------------------------
# 4. Scatter Plot
# -------------------------------
numeric_cols = df.select_dtypes(include='number').columns

if len(numeric_cols) >= 2:
    plt.figure(figsize=(8, 5))
    plt.scatter(df[numeric_cols[0]], df[numeric_cols[1]], alpha=0.7)
    plt.title(f"Scatter Plot: {numeric_cols[0]} vs {numeric_cols[1]}")
    plt.xlabel(numeric_cols[0])
    plt.ylabel(numeric_cols[1])
    plt.tight_layout()
    plt.show()

# -------------------------------
# 5. Heatmap (Correlation Matrix)
# -------------------------------
plt.figure(figsize=(8, 6))
correlation_matrix = df[numeric_cols].corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# -------------------------------
# 6. Insights & Observations
# -------------------------------
print("\nInsights & Observations:")
print(f"- The average value of '{column_name}' is {average_value:.2f}.")
print("- The bar chart shows the distribution of values in the selected column.")
print("- The scatter plot reveals the relationship between two numeric variables.")
print("- The heatmap highlights correlations between numeric features.")
