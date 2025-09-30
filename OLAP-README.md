OLAP-MOLAP Python Script
This project demonstrates Online Analytical Processing (OLAP) and Multidimensional OLAP (MOLAP) operations using Python, pandas, SQLite, and data visualization libraries. It is designed for educational purposes to show how analytical queries and cube operations can be performed on tabular data.

Features
OLAP Operations: Performs SQL-based roll-up aggregations using SQLite.
MOLAP Operations: Uses pandas to create in-memory pivot tables and cubes for multidimensional analysis.
Data Visualization: Visualizes results with matplotlib and seaborn (bar charts, heatmaps).
Sample Data: Includes sample employee and department data for demonstration.
Slice, Dice, Drill Down, Roll Up: Demonstrates classic OLAP operations on the dataset.
Requirements
Python 3.7+
pandas
numpy
matplotlib
seaborn
sqlite3 (standard library)
Setup
Install required packages
Ensure you have Python installed and available in your PATH.
Usage
Place OLAP-MOLAP.py in your working directory.
Run the script
The script will:
Create sample employee and department tables
Load data into a SQLite database
Perform OLAP and MOLAP operations
Print results to the console
Display visualizations for analytical results
