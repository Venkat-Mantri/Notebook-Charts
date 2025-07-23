import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# Load CSV file
sales_data = """Date,Product,Region,Quantity,Price
2025-07-01,Mobile,South,10,15000
2025-07-01,Laptop,North,5,45000
2025-07-02,Tablet,East,8,20000
2025-07-02,Mobile,West,6,15000
2025-07-03,Laptop,South,3,46000
2025-07-03,Tablet,North,4,21000
2025-07-04,Mobile,East,7,15500
2025-07-04,Laptop,West,2,47000
2025-07-05,Tablet,South,5,20500"""
data = pd.read_csv(StringIO(sales_data))

# Create a 'Total' column (Quantity * Price)
data['Total'] = data['Quantity'] * data['Price']

# Group by Product and calculate total sales
product_sales = data.groupby('Product')['Total'].sum()

# Print total sales by product
print("Total Sales by Product:")
print(product_sales)

# Plot total sales by product
product_sales.plot(kind='bar', title='Sales by Product', color='skyblue')
plt.ylabel('Total Sales')
plt.xlabel('Product')
plt.tight_layout()
plt.show()

# Group by Region and calculate total sales
region_sales = data.groupby('Region')['Total'].sum()

# Print total sales by region
print("\nTotal Sales by Region:")
print(region_sales)

# Plot total sales by region
region_sales.plot(kind='bar', title='Sales by Region', color='orange')
plt.ylabel('Total Sales')
plt.xlabel('Region')
plt.tight_layout()
plt.show()