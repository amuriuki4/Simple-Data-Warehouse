# Simple Data Warehouse Implementation in Python
import pandas as pd
import sqlite3
import os
from sqlite3 import Error
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import datetime

#function to create a database connection
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
    except Error as e:
        print(e)
    return conn
#function to execute a query
def execute_query(conn, query):
    try:
        c = conn.cursor()
        c.execute(query)
        conn.commit()
        print("Query executed successfully")
    except Error as e:
        print(e)
#function to fetch data from a query
def fetch_data(conn, query):
    try:
        c = conn.cursor()
        c.execute(query)
        rows = c.fetchall()
        return rows
    except Error as e:
        print(e)
        return None
#function to create a table from a dataframe
def create_table_from_df(conn, df, table_name):
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    print(f"Table {table_name} created successfully")

#function to visualize data
def visualize_data(df, x, y, kind='bar'):
    if kind == 'bar':
        sns.barplot(x=x, y=y, data=df)
    elif kind == 'line':
        sns.lineplot(x=x, y=y, data=df)
    elif kind == 'scatter':
        sns.scatterplot(x=x, y=y, data=df)
    plt.show()
#function to perform basic data analysis
def basic_data_analysis(df):
    print("Dataframe Head:")
    print(df.head())
    print("\nDataframe Info:")
    print(df.info())
    print("\nDataframe Description:")
    print(df.describe())
    print("\nMissing Values:")
    print(df.isnull().sum())

#main function

def main():

    database = "data_warehouse.db"
    conn = create_connection(database)
    if conn is not None:
        #create a sample dataframe
        data = {
            'id': [1, 2, 3, 4, 5],
            'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
            'age': [24, 30, 22, 35, 28],
            'salary': [50000, 60000, 55000, 70000, 65000]
        }
        df = pd.DataFrame(data)
        #create table from dataframe
        create_table_from_df(conn, df, 'employees')
        #fetch data from table
        rows = fetch_data(conn, "SELECT * FROM employees")
        print("Fetched Data:")
        for row in rows:
            print(row)
        #perform basic data analysis
        basic_data_analysis(df)
        #visualize data
        visualize_data(df, x='name', y='salary', kind='bar')
        conn.close()
    else:
        print("Error! Cannot create the database connection.")

if __name__ == "__main__":
    main()
