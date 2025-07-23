# Notebook-Charts
# CSV Sales Data Analysis - Python Developer Internship Task 5

# Objective
Analyze sales data from a CSV file using *Python* and *Pandas*, and visualize the results using simple charts.


# Tools Used
- Python
- Pandas
- Matplotlib
- Jupyter Notebook / Google Colab


# Dataset
The CSV file contains basic sales data with the following columns:
- Date – Date of the sale
- Product – Name of the product sold
- Region – Sales region
- Quantity – Number of units sold
- Price – Price per unit

> A new column Total is calculated as Quantity * Price.


# Features / What This Project Does
- Loads sales data from a .csv file
- Creates a new column for total sales
- Groups data by:
  - Product (to find total sales per product)
  - Region (to find total sales per region)
- Visualizes the grouped data using bar charts


# Sample Output
- Console output: Total sales by Product and Region
- Bar chart 1: 📊 Total Sales by Product
- Bar chart 2: 📊 Total Sales by Region


# How to Run the Project

1. Clone the repository or download the code
2. Place your sales_data.csv file in the same folder
3. Run the notebook or script:
    bash
    python sales_analysis.py
    
   Or open sales_analysis.ipynb in Jupyter/Colab
4. View the printed summaries and bar charts

---

# Example CSV Format

```csv
Date,Product,Region,Quantity,Price
2025-07-01,Mobile,South,10,15000
2025-07-01,Laptop,North,5,45000
...
