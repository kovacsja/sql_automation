import os
from pandas.io import excel
import pyodbc
import pandas as pd
import urllib
from getpass import getpass

SCRIPT_DIR: str = "sql_to_excel/sripts"

driver: str = "ODBC Driver 17 for SQL Server"
server: str = "globalfr"
db: str = "AdventureWorks2017"
me: str = "SA"
passw: str = getpass("Password?")

params_in = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server}"
    + ";SERVER="
    + server
    + ";DATABASE="
    + db
    + ";UID="
    + me
    + ";PWD="
    + passw
)

scripts = [i for i in os.listdir(SCRIPT_DIR)]

conn = pyodbc.connect("Driver={SQL Server};SERVER=" + server + ";Database=" + db + ";UID=me;PWD=" + passw)

#conn = sqlalchemy.create_engine("mssql+pyodbc:///?odbc_connect=%s" % params_in)

for s in scripts:
    with open(SCRIPT_DIR + "/" + s, "r") as f:
        df = pd.read_sql(f.read().replace("\n", ""), conn)
#        with pd.ExcelWriter("data.xlsx") as ew:
#            df.to_excel(excel_writer=ew, sheet_name=s[:-4], header=True)

print(df.head())