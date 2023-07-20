import pandas as pd
import numpy as np
import cx_Oracle
#Variables Parametros Locales
from Parameters import *
from Credenciales import *


###############################################################
''' Origen SQL
pre_source = pd.read_sql(
    query
    ,con=connection
    )
source = pre_source.astype(str
    ).sort_values(by=Value_to_Order, ascending=ASC, kind='mergesort',ignore_index=False
    ).reset_index(drop=True)
'''
''' Origen CSV'''
pre_source = pd.read_csv(csv_file_source, sep=f'{delimiter_source}', dtype=str
                     ).sort_values(by=Order_target_Values_by_Headers, ascending=ASC, kind='mergesort',ignore_index=False)
source = pre_source.reset_index(drop=True)


###############################################################
''' Destino CSV'''
try:
    pre_target = pd.read_csv(
        csv_file_target,sep=f'{delimiter_target}',
        encoding = encoding
        ,dtype=str                  # STRING / OBJECT
        #,header=None               # NO HEADER
        #,index_col=0             # NO index
        ).sort_values(by=Order_target_Values_by_Headers, ascending=ASC, kind='mergesort',ignore_index=False
        ).reset_index(drop=True)
    target = pre_target.where(pd.notnull(pre_target), str(None))
    
except ValueError as e:
    print(e)
    pre_target = pd.read_csv(
        csv_file_target,sep=f'{delimiter_target}',
        encoding = encoding
        ,dtype=str                  # STRING / OBJECT
        #,header=None               # NO HEADER
        #,index_col=0             # NO index
        )
    target = pre_target.where(pd.notnull(pre_target), None)
    
print()
print("==============================================")
print("SHOW | Source Data and Target Data")
print("==============================================")

print(f'Source : ')
print(f'--------')
print(source)
print()
print(f'Target : ')
print(f'---------')
print(target)
###############################################################
print()

try:
    print("==============================================")
    print("TEST 01 | Compare Amount of rows are equals")
    print("==============================================")
    #diffe = origen.compare(destino, align_axis=0)
    des_count_row = target.shape[0]
    ori_count_row = source.shape[0]

    print (f"Source Rows = {ori_count_row}")
    print (f"Target Rows = {des_count_row}")
    print()
except ValueError as e:
    print(e)    
try:
    print("==============================================")
    print("TEST 02 | Check the Headers are correct")
    print("==============================================")
    data_cabeceras = {
        'Source_HEADERS':list(source.columns),
        'Target_HEADERS':list(target.columns)
                    }
    data_cabeceras_view = pd.DataFrame(data_cabeceras)

    data_cabeceras_view['IGUALDAD'] = data_cabeceras_view['Source_HEADERS'] == data_cabeceras_view['Target_HEADERS']
    df2=data_cabeceras_view[data_cabeceras_view['IGUALDAD'] == False]
    
    print(data_cabeceras_view)
    print('-------------------------------------------')
    print(df2)
except: 
    print('CABECERAS | Headers are NOT equals :')
    print()
    print(f'Source : {list(source.columns)}')
    print(f'- rows : {len(list(source.columns))}')
    print(f'Target : {list(target.columns)}')
    print(f'- rows : {len(list(target.columns))}')
    
try:
    a = [i for i in list(source.columns) if i not in list(target.columns)]
    print()
    print(f'Misspelled words are found: {a}')
    print()
except ValueError as e:
    print(e)
    print()
    
try:
    print("==============================================")
    print("TEST 03 | Validate the values ")
    print("==============================================")
    difference = source.compare(target, align_axis=0, result_names=('Source', 'Target'))
    #difference.to_csv('output.csv',sep='\t')

    print("Diferent values: ")
    print()
    print(difference)
    print()
    
    difference_rows = difference.shape[0]
    print(f" Amount of diferent values : {difference_rows/2}")

    #print(origen.dtypes) #Debugear inconsistenciaSs
    
except ValueError as e:
    print('\n The number of rows is not the same, or the headers are not in an appropriate order\n')
    print()
    print(e)
