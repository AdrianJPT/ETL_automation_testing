name_origen = 'VUPC_GET_INSCALUMNO_BLACKBOARD_EPG'

# Query 
query = """SELECT 

USER_ID,
PASSWD,
FIRSTNAME,
LASTNAME,
EMAIL

FROM
SCHEME01.TABLE01"""


# Import CSV source:
csv_file_source = 'Source_Sample.txt'
delimiter_source = ','

# Import Target: Path | Ruta del archivo
csv_file_target = 'Target_Sample.txt'
delimiter_target = '|'     # The delimiter symbol , | ; -

# General
encoding = 'utf-8'   # cp1252,utf-8
Order_target_Values_by_Headers =['USER_ID','FIRSTNAME','EMAIL'] #HEADERS of the Source Value

ASC = [True,True,True] #The boolean depends on the "Order_target_Values_by_Headers"