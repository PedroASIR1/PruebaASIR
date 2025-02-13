import streamlit as st

st.title("😎 Mi aplicación")
st.write("esto es una prueba")
st.header("esto es una cabecera")


cantidad = st.slider("elija un valor")

for i in range(cantidad):
    st.button(f'Botón {i}')

#st.checkbox(f'opcion {i}')