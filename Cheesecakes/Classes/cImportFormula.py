import sys
import pypyodbc as odbc
import DB_Config as DBC
from dataclasses import dataclass

@dataclass
class ImportFormula:
    filename: str
    importFormulaID: int
    formulaNameOrig: str = ""
    formulaName: str = ""
    #importFormulaLines: list[str] = field(default_factory=list)

    def get_ImportFormulaID(self) -> int:
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
            cursor.execute('{CALL pr_IF_GetID(?)}', params= [self.filename])    
            result = cursor.fetchone()    
        except Exception as e:
            print(e.value)
            print('transaction rolled back')
            #cursor.rollback()
        # else:
            #cursor.commit()

        finally:
            cursor.close()
            if conn.connected == 1:
                conn.close()
        
        return result

    @staticmethod
    def get_ImportFormula_List() -> list:
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
            cursor.execute('pr_IF_GetList')    
            result = cursor.fetchall()    
        except Exception as e:
            print(e.value)
        else:
            cursor.close()
        finally:
            if conn.connected == 1:
                conn.close()
        #print (type(result))
        return result

    def FormulaName_AddUpd(self):
        try:
            conn = odbc.connect(DBC.conn_string)
        except Exception as e:
            print(e)
            print('task is terminated')
            sys.exit()
        else:
            cursor = conn.cursor()

        insert_statement = """
            INSERT INTO [dbo].[pyFormulas] ([FormulaName],[Filename])
            VALUES (?, ?)
        """

        try:
            cursor.execute(insert_statement, [self.formulaName, self.filename])        
        except Exception as e:
            print(e.value)
            print('transaction rolled back')
            cursor.rollback()
        else:
            print('records inserted successfully')
            cursor.commit()
            cursor.close()
        finally:
            if conn.connected == 1:
                print('connection closed')
                conn.close()


# ##############################################################################################
# Testing
# ##############################################################################################
# F = NewFormula(importFormulaID=12, filename="fi.txt", formulaNameOrig="Plastic Cheese")
# F.importFormulaLines.append("A1")
# F.importFormulaLines.append("A2")
# F.importFormulaLines.append("A3")

# G = NewFormula(importFormulaID=14, filename="fiGGG.txt", formulaNameOrig="Mashed Potatoes")
# G.importFormulaLines.append("B1")
# G.importFormulaLines.append("B2")
# G.importFormulaLines.append("B3")

# print( '----------------------------')
# print(F)            
# print(F.get_ImportFormulaID())
# print( '----------------------------')

# print(G)
# print(G.get_ImportFormulaID())
# print( '----------------------------')

# FormulaList = NewFormula.get_ImportFormula_List()
# for ln in FormulaList:
#     print('')
#     for co in ln:
#         print(co)

# print( '----------------------------')
