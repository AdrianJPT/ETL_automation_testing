# ETL_automation_testing
Python scripts using Pandas library to get the SOURCE (txt - csv - DataBase) and compre with the TARGET (txt - csv - DataBase)

## Quickstart
### 1) Chose the Python Script that your need 
  * app_CSV.py : Extract data from a CSV or TXT file
    
    Set the corresponding variables in:
    * Credenciales.py:
    ```python
    # Import CSV source:
    csv_file_source = 'Source_Sample.txt'
    delimiter_source = ','
    
    # Import Target: Path | Ruta del archivo
    csv_file_target = 'Target_Sample.txt'
    delimiter_target = '|'     # The delimiter symbol , | ; -
    ```
  * app_NoHeaders.py : Extract data with no Headers in the DataFrame  
  * app_SQL.py : Extract data from a SQL DataBase

    Set the corresponding variables in:
    * Credenciales.py:
    ```python
    # Data Base Parameters connections
    username = 'SCHEME01'
    password = 'password'
  
    ip = 'your_ip'
    port = '1521'
    SID = 'BD_SID'
    ```
    * Parameters.py:
    ```python
    # Query 
    query = """SELECT 
    USER_ID,
    PASSWD,
    FIRSTNAME,
    LASTNAME,
    EMAIL
    FROM
    SCHEME01.TABLE01"""
    ```
### 2) Set the General variables in Credentials.py
    ```python
    # General
    encoding = 'utf-8'   # cp1252,utf-8
    Order_target_Values_by_Headers =['USER_ID','FIRSTNAME','EMAIL'] #HEADERS of the Source Value

    #The booleans depends on the "Order_target_Values_by_Headers" you want to sort
    ASC = [True,True,True] 
    ```
### 3) Run the python script (Example)
* Script:
```python
python3 app_CSV.py
```
* Output:
```bash
==============================================
SHOW | Source Data and Target Data
==============================================
Source : 
--------
    USER_ID   PASSWD  FIRSTNAME     LASTNAME          EMAIL
0    D13628  6678384  nombre_05  apellido_05      correo_05
1  D2402051  6410404  nombre_10  apellido_10      correo_10
2  D2760570  7163526  nombre_01  apellido_01  NOT_correo_01
3   D350818  6121272  nombre_04  apellido_04      correo_04
4   D350818  6121272  nombre_08  apellido_08      correo_08
5  D4030170  6064032  nombre_02  apellido_02      correo_02
6   D406846  6172699  nombre_03  apellido_03      correo_03
7  D7987890  7062820  nombre_09  apellido_09      correo_09
8  D8627970  5708328  nombre_06  apellido_06      correo_06
9   D909611  5837275  nombre_07  apellido_07      correo_07

Target : 
---------
    USER_ID   PASSWD  FIRSTNAME     LASTNAME      EMAIL    
0    D13628  6678384  nombre_05  apellido_05  correo_05    
1  D2402051  6410404  nombre_10  apellido_10  correo_10    
2  D2760570  7163526  nombre_01  apellido_01  correo_01    
3   D350818  6121272  nombre_04  apellido_04  correo_04    
4   D350818  6121272  nombre_08  apellido_08  correo_08    
5  D4030170  6064032  nombre_02  apellido_02  correo_02    
6   D406846  6172699  nombre_03  apellido_03  correo_03
7  D7987890  7062820  nombre_09  apellido_09  correo_09
8  D8627970  5708328  nombre_06  apellido_06  correo_06
9   D909611  5837275  nombre_07  apellido_07  correo_07

==============================================
TEST 01 | Compare Amount of rows are equals
==============================================
Source Rows = 10
Target Rows = 10

==============================================
TEST 02 | Check the Headers are correct
==============================================
  Source_HEADERS Target_HEADERS  IGUALDAD
0        USER_ID        USER_ID      True
1         PASSWD         PASSWD      True
2      FIRSTNAME      FIRSTNAME      True
3       LASTNAME       LASTNAME      True
4          EMAIL          EMAIL      True
-------------------------------------------
Empty DataFrame
Columns: [Source_HEADERS, Target_HEADERS, IGUALDAD]
Index: []

Misspelled words are found: []

==============================================
TEST 03 | Validate the values
==============================================
Diferent values:

                  EMAIL
2 Source  NOT_correo_01
  Target      correo_01

 Amount of diferent values : 1.0
```
