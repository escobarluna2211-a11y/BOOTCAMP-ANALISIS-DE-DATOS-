import streamlit as st
import pandas as pd

## CARGA DE DATOS ❤️

ruta ='data\ZNI.csv'
df = pd.read_csv(ruta)

## ANALISIS DE DATOS❤️
filas = df.shape[0]
columnas = df.shape[1]

## VISULUALIZACION DE DATOS❤️

col1, col2 = st.columns(2)
with col1 :
    with st.container(border=True):
         st.subheader('Numero de filas')
         st.text(filas)

with col2 :
    with st.container(border=True):
         st.subheader('Numero de filas')
         st.text(filas)

### otra forma de mostrar indicadores 
col3, col4 = st.columns(2)
with col3:
    st.metric('Numero de filas', filas, border=True)
with col4:
    st.metric('Numero de columnas', columnas, border=True)