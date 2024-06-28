import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('notebooks\\vehicles_us.csv') # leer los datos
st.header("Bienvenido(a) al Análisis de Vehiculos")


# crear una casilla de verificación
build_histogram = st.checkbox('Histograma')


if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Distancia recorrida por los vehiculos')
            
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


build_dispersion = st.checkbox('Gráfico de dispersión') 
if build_dispersion:
    st.write('Relación entre la Distancia recorrida del vehículo y su Precio actual')
            
            # crear un grafico de dispersion
    fig =px.scatter(car_data, x="odometer", y="price")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
