import os
import pyodbc
import pandas as pd
from getpass import getpass
import tqdm #TODO: progressbar

SCRIPT_DIR: str = "sql_to_excel/sripts"

pw = getpass("Password?")

conn_params = {
    "driver": "ODBC Driver 17 for SQL Server",
    "server": "globalfr",
    "db": "AdventureWorks2017",
    "me": "SA",
    "passw": pw,
}

scripts = [i for i in os.listdir(SCRIPT_DIR)]

conn = pyodbc.connect(
    f"Driver={conn_params['driver']};SERVER={conn_params['server']};Database={conn_params['db']};UID={conn_params['me']};PWD={conn_params['passw']}"
)

#TODO: connection tesztelése (ping?)
#TODO: sql_alchemy variáns connection készítése

with pd.ExcelWriter("data.xlsx") as ew:
    for s in scripts:
        with open(SCRIPT_DIR + "/" + s, "r") as f:
            pd.read_sql(f.read().replace("\n", " "), conn).to_excel(
                ew, sheet_name=s[:-4], header=True
            )
