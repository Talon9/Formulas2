import sys
import pypyodbc as odbc
import DB_Config as DBC
import DB as DB
from dataclasses import dataclass, field
from Classes.cImportType import ImportType

@dataclass
class ImportFormulaLines():
    importFormulaID: int
    lnSeq: int
    lnTxt: str
    importTypeID: ImportType = 0
    importSeq: int = 0

    def FormulaLines_AddUpd(self):
        result = []
        try:
            conn = odbc.connect(DBC.conn_string)
        except Exception as e:
            print(e)
            print('task is terminated')
            sys.exit()
        else:
            cursor = conn.cursor()

        try:
            print(cursor) 
            #cursor.set_timeout = 120
            
            sql = f'EXEC [pr_IFL_AddUpd] ' + str(self.importFormulaID) + ', ' + str(self.lnSeq) + ', "' + self.lnTxt + '"'
            print (sql)
            #cursor.execute('CALL pr_IFL_AddUpd(?, ?, ?)', params=[self.importFormulaID, self.lnSeq, self.lnTxt])   
            cursor.execute(sql)    
            #cursor.execute('pr_IFL_AddUpd', params= [self.importFormulaID, self.lnSeq, self.lnTxt])    

            # result = cursor.fetchone() 
            #result = cursor.fetchall()
            result = cursor.fetchmany()
            print(result)
            print('----------------')
        except Exception as e:
            print(e.value)
            #cursor.rollback()
        else:
            print('records inserted successfully')
            #cursor.commit()
        finally:
            cursor.close()
            if conn.connected == 1:
                conn.close()

        return result
    
#---------------------------
