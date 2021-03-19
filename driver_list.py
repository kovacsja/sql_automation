import pyodbc

for i in pyodbc.drivers():
    print(i)