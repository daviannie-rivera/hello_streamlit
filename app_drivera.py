import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


####################
## ajustar el layout
#################### 

st.set_page_config(layout="wide") #To set the layout of the webpage


##################
## tamaño del plot
################## 

fig, ax = plt.subplots()


#########
## titulo
######### 

col1, col2, col3 = st.columns([1,3,1])

col1.image("logouprh.png")
col2.title("Datos de Covid - Variante Omicrón")
col3.image("covid.png") 
           
#st.title("Datos de Covid - Variante Omicrón")


##############################################
## esto es para que salga una linea horizontal
############################################## 

st.divider() #A thin line to divide

#################
## datos de covid 
################# 

df_covid = pd.read_csv("https://raw.githubusercontent.com/elioramosweb/archivo_datos/main/datos_diarios-2022-03-22_10_20_15.csv",parse_dates=['date'])

#df_covid["date"] = pd.to_datetime(df_covid["date"]) #Considera la primera columna como fecha

nombres = list(df_covid.columns)[1:]

columna = st.sidebar.selectbox("Columna de Interés",nombres)

#Indicar suavizado

#suavizado = st.sidebar.checkbox("Suavizado")
st.sidebar.divider()

tabla = st.sidebar.checkbox("Mostrar datos")

#st.write(df_covid.columns)

df_covid.plot(x="date",y=columna,ax=ax,ylabel=columna,linewidth=3,linestyle="dotted")

col1,col2 = st.columns(2)

st.sidebar.divider()

suavizado = st.sidebar.checkbox("Suavizado")

if suavizado:  
    ventana = st.sidebar.slider("Ventana de suavizado [días]", 1,15,7) 
    df_rolling = df_covid[columna].rolling(window=7,center=True).mean()
    df_covid[columna + "_rolling"] = df_rolling
    df_covid.plot(x="date",y=columna + "_rolling",ax=ax)

if tabla: 
    df_covid["date"] = df_covid["date"].dt.strftime("%d-%b-%Y")
    df_tabla = df_covid[["date", columna]]
    col2.write(df_covid)

st.sidebar.divider



st.sidebar.markdown("""Aplicación por: <br>
                    Daviannie Rivera <br>
                    COMP3082""", unsafe_allow_html= True)



st.sidebar.write("Barra Izquierda")




col1.pyplot(fig)

#col2.write(df_covid.head())



#st.write(df_covid.head())

#st.write(df_covid.tail())


