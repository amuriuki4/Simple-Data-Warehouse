# OLAP DEMO
# This script demonstrates a simple OLAP operation using pandas.
# ROLAP, OLAP, MOLAP
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# database connection
def create_connection(db_file = "olap_demo.db"):
    conn = sqlite3.connect(db_file)
    return conn

# create a sample dataset

employees = pd.DataFrame({
    'emp_id':[1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'age': [30, 45, 25, 35, 28],
    'salary': [70000, 80000, 50000, 60000, 75000],
    'dept_id': [1, 2, 1, 3, 2]
})

departments = pd.DataFrame({
    'dept_id': [1, 2, 3],
    'department': ['IT', 'HR', 'Finance']
})

# load data into sqlite database
conn = create_connection()
employees.to_sql('employees', conn, if_exists='replace', index=False)
departments.to_sql('departments', conn, if_exists='replace', index=False)
print("Tables created: employeees and departments")

# Perform OLAP operation

#OLAP operation
query = """
SELECT d.department, AVG(e.salary) as avg_salary
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
GROUP BY d.department


"""


rolap_result = pd.read_sql_query(query, conn)
print("\nROLAP Result (SQL aggregation):")
print(rolap_result)


# Visualization: Roll up by department
sns.barplot(x='department', y='avg_salary', data=rolap_result)
plt.title('ROLAP: Average Salary by Department')
plt.show()

# MOLAP operation
#using pandas for in-memory aggregation
molap_cube = pd.pivot_table(
    
    employees.merge(departments, on='dept_id'),
    values='salary',
    index=['department'],
    columns='age',
    aggfunc=np.mean,
    fill_value=0
)

print("\nMOLAP cube (Department vs Age):")
print(molap_cube)

# Visualization: MOLAP cube heatmap
sns.heatmap(molap_cube, annot=True, fmt=".0f", cmap="Blues")
plt.title('MOLAP: Average Salary Cube (Department vs Age)')
plt.show()


# MOLAP Operations
# Combining MOLAP and ROLAP Approaches

detail_sql = """
SELECT d.department, e.name, e.age, e.salary
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
"""

detail_df = pd.read_sql_query(detail_sql, conn)

# Pandas MOLAP aggregation
holap_summary = detail_df.groupby('department')['salary'].mean().reset_index()

print("\nHOLAP Summary (Department Vs Age):")
print(molap_cube)

# Visualization: molap cube heatmap
sns.heatmap(molap_cube, annot=True, fmt=".0f")
plt.title('HOLAP: Average Salary by Department')
plt.show()

# OLAP Operations Demonstrates
# Slice
slice_df = detail_df[detail_df['department'] == 'IT']
print("\nSlice (IT Department):")
print(slice_df)

# Dice
dice_df = detail_df[(detail_df['department'] == 'IT') & (detail_df['salary'] > 60000)]
print("\nDice (IT Department with Salary > 60000):")
print(dice_df)

# Drill Down
sns.barplot(data=detail_df, x='name', y='salary', hue='department')
plt.title('Drill Down: Salary by Employee and Department')
plt.show()



# Roll Up
rollup_df = detail_df.groupby('department')['salary'].mean().reset_index()
print("\nRoll Up :Total Salary by Department")
print(rollup_df)


# Visualization
sns.barplot(x='department', y='salary', data=rollup_df)
plt.title('Roll Up: Total Salary by Department')
plt.show()
