import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('notebooks\\vehicles_us.csv') # leer los datos

st.header("Bienvenido(a) al Análisis de Vehiculos")

hist_button = st.button('Histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Distancia recorrida por los vehiculos')
            
            # crear un histograma
            fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Gráfico de dispersión') # crear un botón
        
if disp_button: # al hacer clic en el botón
            # escribir un mensaje
            st.write('Relación entre la Distancia recorrida del vehículo y su Precio actual')
            
            # crear un histograma
            fig =px.scatter(car_data, x="odometer", y="price")
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)


