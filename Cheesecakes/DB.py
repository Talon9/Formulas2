import sys
import pypyodbc as odbc
import DB_Config as DBC

def ExecSql(sql, params):
    debug = False
    try:
        conn = odbc.connect(DBC.conn_string)
    except Exception as e:
        print(e)
        if debug:
            print('task is terminated')
        sys.exit()
    else:
        cursor = conn.cursor()
  
    try:
        if params == []:
            cursor.execute(sql, params=None)        
        else:
            cursor.execute(sql, params=params)        
    except Exception as e:
        print(e.value)
        if debug:
            print('transaction rolled back')
        cursor.rollback()
    else:
        if debug:
            print('SQL executed successfully')
        cursor.commit()
        cursor.close()
    finally:
        if conn.connected == 1:
            if debug:
                print('connection closed')
            conn.close()

def ExecSql_Int(sql, params) -> int:
    res = None
    try:
        conn = odbc.connect(DBC.conn_string)
    except Exception as e:
        print(e)
        sys.exit()
    else:
        cursor = conn.cursor()
  
    try:
        if params == []:
            cursor.execute(sql, params=None)  
        else:
            cursor.execute(sql, params=params)   

        results = cursor.fetchone()     
        # res = (cursor.fetchall())[0]
        if results != None:
            res = results[0]
            # if debug:
            #     print(res)

    except Exception as e:
        print(e)
        # if debug:
        #     print('">>> " + transaction rolled back')
        cursor.rollback()
    else:
        # if debug:
        #     print('SQL executed successfully')
        cursor.commit()
        cursor.close()
    finally:
        if conn.connected == 1:
            conn.close()

    return res
        

