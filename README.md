# Qskill-Python-Developer

Retail Store Sales Data Analysis using Pandas & Matplotlib
 Project Overview

This project demonstrates how to use Python’s Pandas library to load and analyze a CSV dataset, and Matplotlib/Seaborn to visualize the data. The dataset used is a simulated Retail Store Product Sales Dataset from Kaggle.

The main objectives are:

Load a CSV file.

Perform basic data analysis.

Calculate the average of a selected numeric column.

Create visualizations (bar chart, scatter plot, heatmap).

Derive meaningful insights from the data.

 Technologies Used

Python 3

Pandas – for data manipulation and analysis

Matplotlib – for plotting graphs

Seaborn – for heatmap visualization

KaggleHub – for downloading the dataset

 Dataset

Dataset Source:
Retail Store Product Sales Simulation Dataset (Kaggle)

The dataset contains simulated sales data for retail products including numeric and categorical features such as:

Product details

Sales quantities

Prices

Revenue-related fields

 Installation & Setup

Install the required libraries:

pip install pandas matplotlib seaborn kagglehub

 How to Run the Project

Clone or download this repository.

Make sure the dataset file RetailStoreProductSalesDataset.csv is in the same directory.

Run the Python script:

python main.py


(Replace main.py with your actual file name.)

 Features Implemented
1. Load CSV File
df = pd.read_csv("RetailStoreProductSalesDataset.csv")


Loads the dataset into a Pandas DataFrame.

2. Basic Data Analysis

Displays first 5 rows.

Shows dataset info and statistics.

Automatically selects a numeric column and calculates its average.

3. Bar Chart

Shows the top 10 most frequent values in the selected numeric column.

4. Scatter Plot

Plots a scatter graph between the first two numeric columns to observe relationships.

5. Heatmap

Displays a correlation matrix between all numeric columns using Seaborn.

 Sample Visualizations

The project generates:

Bar Chart → Distribution of values

Scatter Plot → Relationship between two variables

Heatmap → Correlation between features

 Insights & Observations

From the analysis:

The average value of the selected numeric column gives a general idea of the dataset’s central tendency.

The bar chart helps identify the most frequent values.

The scatter plot shows whether two variables are positively/negatively related.

The heatmap highlights which features are strongly correlated and which are independent.

These insights help in understanding sales patterns and relationships between different variables in the retail dataset.

Future Improvements

Add filtering by product category.

Perform time-series analysis.

Build a dashboard using Streamlit or Power BI.

Apply machine learning for sales prediction.

 Author

Z M
B.Sc Computer Science Student
Project on Data Analysis using Python

 License

This project is for educational purposes and uses a publicly available dataset from Kaggle.
