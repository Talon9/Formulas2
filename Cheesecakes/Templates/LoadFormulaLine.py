
import sys
import pypyodbc as odbc
import DB_Config as DBC
# import pyodbc as odbc

records = [
    ['Priscilla', 'Movie', '2020-01-09', 2020], 
    ['Teen Wolf', 'TV Show', None, 2019]
]

try:
    conn = odbc.connect(DBC.conn_string)
except Exception as e:
    print(e)
    print('task is terminated')
    sys.exit()
else:
    cursor = conn.cursor()


insert_statement = """
    INSERT INTO NetflixMovies
    VALUES (?, ?, ?, ?)
"""

try:
    for record in records:
        print(record)
        cursor.execute(insert_statement, record)        
except Exception as e:
    cursor.rollback()
    print(e.value)
    print('transaction rolled back')
else:
    print('records inserted successfully')
    cursor.commit()
    cursor.close()
finally:
    if conn.connected == 1:
        print('connection closed')
        conn.close()


        

