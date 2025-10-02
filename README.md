# Simple Data Warehouse: OLAP Assignment

## Overview

This project demonstrates the design and implementation of a simple data warehouse using a **star schema** in SQLite, and showcases various **OLAP (Online Analytical Processing) operations** using Python (Pandas, SQLite, and visualization libraries).

---

## Star Schema Design

The data warehouse consists of:
- **Fact Table:** `sales`  
  Stores transactional sales data, including product, date, quantity, and revenue.
- **Dimension Tables:**  
  - `products`: Product details (name, category, subcategory)
  - `dates`: Date details (date, year, quarter, month)

**Schema Diagram:**

```
products      dates
----------    -----------
product_id    date
product_name  year
category      quarter
subcategory   month

         \         /
          \       /
           \     /
            sales
-------------------------------------------
sale_id | product_id | date | quantity | revenue
```

---

## Data Population

Sample data is inserted into each table:
- **Products:** 5 products across different categories and subcategories.
- **Dates:** 5 dates with year, quarter, and month.
- **Sales:** 5 sales transactions linking products and dates.

---

## OLAP Operations

The notebook demonstrates the following OLAP operations:

### 1. **Relational OLAP (ROLAP)**
- **Roll-up:** Aggregates total revenue by product category.
- **Drill-down:** Aggregates total sales by year and month.
- **Slice:** Shows best-selling products in a specific category.

### 2. **Multidimensional OLAP (MOLAP)**
- Uses Pandas pivot tables to create a cube for analyzing total revenue by category and month.

### 3. **Hybrid OLAP (HOLAP)**
- Fetches detailed sales data using SQL (ROLAP).
- Summarizes data using Pandas (MOLAP).

### 4. **OLAP Operations Demonstrated**
- **Slice:** Fixes one dimension (e.g., sales date).
- **Dice:** Applies multiple filters (e.g., date range and category).
- **Roll-up:** Aggregates from product to category to year.
- **Drill-down:** Breaks down from year to quarter to month.

---

## Visualization

The notebook includes the following visualizations:
- **Heatmap:** Total revenue by product category and month.
- **Linear Gauge Chart:** Total revenue by product category.
- **Stacked Area Chart:** Cumulative revenue over time by product category.

---

## How to Run

1. **Requirements:**
   - Python 3.x
   - Libraries: `sqlite3`, `pandas`, `numpy`, `matplotlib`, `seaborn`

2. **Run the Notebook:**
   - Open `olap_assignment.ipynb` in Jupyter Notebook or VS Code.
   - Run all cells to create the database, populate data, perform OLAP operations, and generate visualizations.

---

## Key Takeaways

- **Star schema** is effective for analytical queries.
- **OLAP operations** (slice, dice, roll-up, drill-down) enable flexible data analysis.
- **Python and SQLite** provide a simple yet powerful environment for prototyping data warehouse and OLAP solutions.
- **Visualization** helps in understanding and communicating analytical results.

---
