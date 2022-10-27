"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------
Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.
"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    #
    # Inserte su código aquí
    #
    #Inicio limpieza
    #df = pd.read_csv("solicitudes_credito.csv", sep=";",encoding = 'utf-8')
    df = pd.read_csv('solicitudes_credito.csv', sep=";",encoding = 'utf-8-sig')
    #df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'])


    df_mod = df.copy()
    df_mod = df_mod.iloc[:,1:]
    df_mod['fecha_de_beneficio'] = pd.to_datetime(df_mod['fecha_de_beneficio'],dayfirst=True)
    df_mod.drop_duplicates(inplace = True)
    df_mod.dropna(axis=0,inplace=True)


    #transformacion columna sexo
    df_mod['sexo'] = df_mod['sexo'].str.lower()

    #transformacion columna tipo_emprendimiento
    #df_mod.tipo_de_emprendimiento.fillna('sin tipo',inplace = True)
    df_mod['tipo_de_emprendimiento'] = df_mod['tipo_de_emprendimiento'].str.lower()

    #transformacion columna idea_negocio
    df_mod['idea_negocio'] = df_mod['idea_negocio'].str.lower()
    df_mod['idea_negocio'] = df_mod['idea_negocio'].apply(lambda x: x.replace('_',' ') )
    df_mod['idea_negocio'] = df_mod['idea_negocio'].apply(lambda x: x.replace('-',' ') )
    #df_mod['idea_negocio'] = df_mod['idea_negocio'].apply(lambda x: x.strip() )

    #transformacion columna barrio
    #df_mod['barrio'] = df_mod['barrio'].astype(str)
    df_mod['barrio'] = df_mod['barrio'].str.lower()
    #df_mod['barrio'] = df_mod['barrio'].apply(lambda x: x.strip() )
    df_mod['barrio'] = df_mod['barrio'].apply(lambda x: x.replace('_',' ') )
    df_mod['barrio'] = df_mod['barrio'].apply(lambda x: x.replace('-',' ') )
    #df_mod['barrio'] = df_mod['barrio'].apply(lambda x: x.strip() )

    #transformacion línea_credito
    df_mod['línea_credito'] = df_mod['línea_credito'].astype(str)
    df_mod['línea_credito'] = df_mod['línea_credito'].str.lower()
    df_mod['línea_credito'] = df_mod['línea_credito'].apply(lambda x: str(x).replace('_',' ') )
    df_mod['línea_credito'] = df_mod['línea_credito'].apply(lambda x: x.replace('-',' ') )
    #df_mod['línea_credito'] = df_mod['línea_credito'].apply(lambda x: x.replace('soli diaria','solidaria') )

    #transformacion columna monto_credito
    df_mod['monto_del_credito'] = df_mod['monto_del_credito'].apply(lambda x: x.replace(',','') )
    df_mod['monto_del_credito'] = df_mod['monto_del_credito'].apply(lambda x: x.replace('$','') )
    df_mod['monto_del_credito'] = df_mod['monto_del_credito'].apply(lambda x: x.replace(' ','') )
    df_mod['monto_del_credito'] = df_mod['monto_del_credito'].astype(float)

    #Eliminación de valores 
    #df_mod = df_mod[df_mod['comuna_ciudadano'] != 'sin comuna'] 
    #df_mod = df_mod[df_mod['idea_negocio'] != 'sin barrio']
    #df_mod = df_mod[df_mod['tipo_de_emprendimiento'] != 'sin tipo']
    #df_mod = df_mod[df_mod['barrio'] != 'sin barrio']
    

    df_mod.drop_duplicates(inplace = True)

    return df_mod

