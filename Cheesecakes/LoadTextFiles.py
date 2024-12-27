import __main__
import glob
import DB
import Classes.cImportFormula as NF
import Classes.cImportFormulaLines  as IFL

       
for file in glob.glob(r'H:\FoodData\ToBeLoaded\*.txt'):
    with open (file, 'r') as f:
 
        fname = f.name
        fname = fname[1+fname.rfind("\\"):]
        F = NF.ImportFormula(importFormulaID=None, filename=fname, formulaNameOrig=fname)
        
        sql = "EXEC [dbo].[pr_IF_GetID] '" + fname + "'"
        print (sql)
        F.importFormulaID = DB.ExecSql_Int(sql, []) 
        if F.importFormulaID < 0:
            sql = "EXECUTE [dbo].[pr_IF_AddFilename] '" + fname + "'"
            DB.ExecSql(sql, [])
            sql = "EXEC [dbo].[pr_IF_GetID] '" + fname + "'"
            F.importFormulaID = DB.ExecSql_Int(sql, []) 
        
        print( F.importFormulaID )

        f_contentline = f.readline()
        i = 1
        while len(f_contentline)>0:
            newLine = f_contentline[:-1].strip()
            if len(newLine)>0:
                FL = IFL.ImportFormulaLines(importFormulaID=F.importFormulaID, 
                                             lnSeq=i, 
                                             lnTxt=newLine
                                             )
                
                sql = "EXECUTE [dbo].[pr_IFL_AddUpd] " + str(FL.importFormulaID) + "," + str(i) + ",'"+ FL.lnTxt + "'"
                print(sql)
                DB.ExecSql(sql, [])
                #FL.importSeq = FL.FormulaLines_AddUpd()[1:]
                print(FL)
                i=i+1                
            f_contentline = f.readline()
        
        if F.importFormulaID > 0:
            print(F)
            print('-----------------------')

print('--- Completed ---')     