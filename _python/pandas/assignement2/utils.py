"""utility module to try to automate the process of creating and filling an sql table for any given dataframe"""


import pandas as pd
import mysql.connector 

from typing import Union



def get_query_create_table(table_name:str, df:pd.DataFrame) -> str:
    """fonction to generate a query to create a table from a given dataframe"""

    dtype_mapping = {
        'int64': 'int',
        'float64': 'float',
        'O': 'varchar(255)',  
        'object': 'varchar(255)', 
        'bool': bool,
        'datetime64[ns]': 'datetime', 
    }


    query = f"create table {table_name} ("
    for colname in df.columns: 
        query += f'\n `{colname}` {dtype_mapping[str(df[colname].dtype)]},'
    query = query[:-1] + ");"



    return query 


def insert_df2sql(connection, table_name:str, df:pd.DataFrame, debug=False) -> None: 
    """Function to insert dataframe rows into a given sql table, that has same columns as the dataframe"""
    
    cols = ", ".join([f"`{col}`" for col in df.columns])
    placeholders = ", ".join(["%s"] * len(df.columns))

    query = f"INSERT INTO {table_name} ({cols}) VALUES ({placeholders})" 

    cursor = connection.cursor()

    if debug: 
        print('inserting rows now')
        print('query is like this : ', query)

    # inserting the rows
    for _, row in df.iterrows():
        row_data = tuple(None if pd.isna(val) else val for val in row)
        cursor.execute(query, row_data)
        print('one row inserted : ')

    # commit() the transaction
    connection.commit()
    cursor.close()





if __name__ == '__main__': 

    # from os import path 
    # import os 

    # print('os.pardir: ', os.pardir)
    # print(__file__)
    # file_path = path.join(path.dirname(__file__), '..', 'movies.xls')
    # print('file_path :', file_path)

    # df = pd.read_excel('../movies.xls')
    # print('shape of df : ', df.shape)
    # print('query create table is : ')
    # print(get_query_create_table('movies', df))

    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="assignement_db"
        )
        print("Database connection successful")
    except Exception as e:
        print(f"Error connecting to MySQL: {e}")


    print('creating cursor')
    cursor = db.cursor()

    # print insertin go to sql : 
    # print('now inserting to movies table')
    # insert_df2sql(db, 'movies', df, debug=True)


