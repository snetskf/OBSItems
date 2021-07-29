import pandas as pd
import pyodbc
import GenerateXLSX

def GetXls():

    print('SQL connectivity')
    conn = pyodbc.connect('Driver={SQL Server};Server=W2812;Database=ScrapInventory;Trusted_Connection=yes;')
    # cursorobj=conn.cursor()
    # cursorobj.execute('ReportOBSItems4470')

    df = pd.read_sql_query('ReportOBSItems4470', conn)
    writer = pd.ExcelWriter('c:\\projects\\ReportOBSItems4470.xlsx')
    df.to_excel(writer, sheet_name='OBS', index=0)
    writer.save()
    GenerateXLSX.SendEmail("C:\\projects\\ReportOBSItems4470.xlsx","ReportOBSItems4470.xlsx")

    df = pd.read_sql_query('ReportOBSItems', conn)
    writer = pd.ExcelWriter('c:\\projects\\ReportOBSItems.xlsx')
    df.to_excel(writer, sheet_name='OBS', index=0)
    writer.save()
    GenerateXLSX.SendEmail("C:\\projects\\ReportOBSItems.xlsx","ReportOBSItems.xlsx")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    GetXls()
