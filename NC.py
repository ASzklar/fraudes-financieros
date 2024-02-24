import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from google.oauth2 import service_account
from googleapiclient.discovery import build
import io

# ID del archivo CSV
file_id = '1YvSbFLTblzd7kfYxW6IMNT9JIM_8WHLv'

# Clave de API (pega tu clave aquí)
api_key = "AIzaSyBxZk18sBSo0GMrzJgjzHV1FsCSYLrAji4"

# Servicio Drive
service = build('drive', 'v3', developerKey=api_key)

# Descargar el archivo CSV a un buffer
request = service.files().get_media(fileId=file_id)
file_buffer = request.execute()

# Convert the bytes object to a string
text_buffer = file_buffer.decode("utf-8")

# Create an in-memory StringIO object
string_io = io.StringIO(text_buffer)

# Read the CSV with pandas
df = pd.read_csv(string_io)

print(df.head())

print('Hello World')

st.title("Probando Streamlit :hand:")
st.text("No Country Proyecto detección de fraudes")
st.image("fraude_imagen.png")

st.radio("Elige una opción", df.columns)

#fraudes = df[df['isFraud'] == 1]

#fraudes_por_tipo = fraudes.groupby('type').size()
st.write("***Fraudes***")
#fig, ax = plt.subplots()
#fraudes_por_tipo.plot(kind='bar', ax=ax)
#ax.set_title('Fraudes por tipo de transacción')
#ax.set_xlabel('Tipo de transacción')
#ax.set_ylabel('Cantidad')
#st.pyplot(fig)


#@st.cache