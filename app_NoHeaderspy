import pandas as pd
import numpy as np
import cx_Oracle
#Variables Parametros Locales
from Parameters import *
from Credenciales import *

dsn_tns = cx_Oracle.makedsn(ip, port, SID)
connection = cx_Oracle.connect(username, password, dsn_tns)

###############################################################
''' Origen SQL'''
pre_origen = pd.read_sql(
    query
    , con=connection
    )
pre2_origen = pre_origen.astype(str)
pre2_origen.columns = range(pre2_origen.shape[1])

origen = pre2_origen.sort_values(by=Order_target_Values_by_Headers, ascending=ASC, kind='mergesort',ignore_index=False
    ).reset_index(drop=True)


''' Origen CSV'''
#origen = pd.read_csv(csv_file_source, dtype=str)

''' Destino CSV'''
destino = pd.read_csv(
    csv_file_target,sep=f'{delimiter}',
    encoding = encoding
    ,dtype=str       #STRING / OBJECT
    ,header=None        # NO HEADER
    ).sort_values(by=Order_target_Values_by_Headers, ascending=ASC, kind='mergesort',ignore_index=False
        ).reset_index(drop=True)

print()
print("==============================================")
print("MOSTRAR EL ORIGEN Y DESTINO")
print("==============================================")

print(f'Origen : {name_origen}')
print(f'--------')
print(origen)
print()
print(f'Destino : {csv_file_target}')
print(f'---------')
print(destino)
###############################################################
print()

try:
    print("==============================================")
    print("TEST 01: CANTIDAD DE ROWS FUERON ENVIADOS")
    print("==============================================")
    #diffe = origen.compare(destino, align_axis=0)
    des_count_row = destino.shape[0]
    ori_count_row = origen.shape[0]

    print (f"Origen Rows = {ori_count_row}")
    print (f"Destino Rows = {des_count_row}")
    print()
except ValueError as e:
    print(e)    
try:
    print("==============================================")
    print("TEST 02: VALIDAR LAS CABECERAS")
    print("==============================================")
    data_cabeceras = {
        'Cabecera_Origen':list(origen.columns),
        'Cabecera_Destino':list(destino.columns)
                    }
    data_cabeceras_view = pd.DataFrame(data_cabeceras)

    data_cabeceras_view['IGUALDAD'] = data_cabeceras_view['Cabecera_Origen'] == data_cabeceras_view['Cabecera_Destino']
    df2=data_cabeceras_view[data_cabeceras_view['IGUALDAD'] == False]
    
    print(data_cabeceras_view)
    print('-------------------------------------------')
    print(df2)
except: 
    print('CABECERAS | la cantidad de cabeceras no son iguales :')
    print()
    print(f'Origen : {list(origen.columns)}')
    print(len(list(origen.columns)))
    print(f'Destino: {list(destino.columns)}')
    print(len(list(destino.columns)))
    
try:
    a = [i for i in list(origen.columns) if i not in list(destino.columns)]
    print()
    print(f'Errores Tipograficos Encontrados: {a}')
    print()
except ValueError as e:
    print(e)
    print()
    
try:
    print("==============================================")
    print("TEST 03: INTEGRIDAD DE LOS VALORES")
    print("==============================================")
    difference = origen.compare(destino, align_axis=0, result_names=('Origen', 'Destino'))
    #difference.to_csv('output.csv',sep='\t')

    print("Valores distintos:")
    print()
    print(difference)
    print()
    
    difference_rows = difference.shape[0]
    print(f" La cantidad de registros distintos es : {difference_rows/2}")

    #print(origen.dtypes) #Debugear inconsistenciaSs
    
except ValueError as e:
    print('\n La cantidad de row no es la misma o las cabeceras estan en un orden no adecuado\n')
    print()
    print(e)
