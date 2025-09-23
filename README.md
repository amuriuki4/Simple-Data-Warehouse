# Simple Data Warehouse

This project is a basic implementation of a data warehouse using Python, SQLite, and pandas. It demonstrates how to store, analyze, and visualize data in a simple, self-contained environment.

## Features
- Create and connect to a SQLite database
- Store pandas DataFrames as database tables
- Execute SQL queries and fetch results
- Perform basic data analysis (head, info, describe, missing values)
- Visualize data using matplotlib and seaborn (bar, line, scatter plots)

## Requirements
- Python 3.13+
- pandas
- sqlite3 (standard library)
- matplotlib
- seaborn
- numpy

## How to Run
1. Install required packages:
   ```powershell
   pip install pandas matplotlib seaborn numpy
   ```
2. Run the script:
   ```powershell
   python "Simple Data Warehouse.py"
   ```

## Example Usage
The script creates a sample employee table, performs analysis, and visualizes salary data:
- Creates a SQLite database `data_warehouse.db`
- Stores a sample DataFrame as the `employees` table
- Fetches and prints all employee records
- Shows basic analysis of the DataFrame
- Displays a bar chart of employee salaries

## File Structure
- `Simple Data Warehouse.py`: Main script with all functions and logic
- `data_warehouse.db`: SQLite database file (created at runtime)

## License
This project is provided for educational purposes.
