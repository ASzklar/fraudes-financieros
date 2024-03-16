import pandas as pd
import streamlit as st
# import matplotlib.pyplot as plt
# from google.oauth2 import service_account
# from googleapiclient.discovery import build
# import io
# import logging

# Error handling and logging
# logging.basicConfig(level=logging.DEBUG)

# ID of your CSV file
# file_id = '1YvSbFLTblzd7kfYxW6IMNT9JIM_8WHLv'

# Replace with your actual API key
# api_key = "***************************"

# Service Drive
# try:
#     service = build('drive', 'v3', developerKey=api_key)
# except Exception as e:
#     logging.error("Error building Drive service:", e)
#     st.error("An error occurred while connecting to Google Drive. Please check your API key and network connectivity.")
#     exit()

# Download and process the CSV
# try:
#     request = service.files().get_media(fileId=file_id)
#     file_buffer = request.execute()
#     text_buffer = file_buffer.decode("utf-8")
#     string_io = io.StringIO(text_buffer)
#     df = pd.read_csv(string_io)
# except Exception as e:
#     logging.error("Error downloading or processing CSV:", e)
#     st.error("An error occurred while processing the CSV file. Please check the file ID and format.")
#     exit()

# Display the DataFrame head
# st.header("Primeros registros del DataFrame")
# st.dataframe(df.head())

# User interface elements

# Título y banner
st.title("Detección de fraudes en transacciones bancarias")
st.image("fraude_imagen.png")

# Sección 1: Distribuciones
with st.container():
    st.markdown('### **En el análisis exploratorio de datos encontramos las siguientes distribuciones:**')
    st.image("Distr_tipo_transacc.png")
    st.image("Distr_fraude_tipo_transacc.png")

# Sección 2: Proporción de fraudes
with st.container():
    st.markdown("### ***Proporción de transacciones fraudulentas sobre el total***")
    st.image("Torta_proporc_fraud.png")

# Sección 3: Distribución de montos
with st.container():
    st.markdown("### *Es útil observar la distribución de los montos de las transacciones, tanto en general como filtrados por fraude.*")
    st.image("Distr_mont_por_transacc.png")
    st.image("Distr_mont_transacc_fraud.png")

# Sección 4: Boxplots de montos
with st.container():
    st.markdown("### ***Boxplot de Montos por Tipo de Transacción y Fraude***")
    st.image("boxplot_mont_tipo_y_fraud.png")
    st.markdown("### *Exploramos los montos involucrados en las transacciones fraudulentas*")
    st.image("Boxplot_mont_transacc_fraud_y_no_fraud.png")

# Sección 5: Saldos antes y después
with st.container():
    st.markdown("### Comparar cómo cambian los saldos antes y después de las transacciones, distinguiendo entre transacciones fraudulentas y legítimas.")
    st.image("Comparac_saldos.png")

# Sección 6: Relación monto-fraude por tipo
with st.container():
    st.markdown("### Análisis de la Relación entre Montos de Transacción y Fraude por Tipo de Transacción Analizar cómo se relacionan los montos de transacción con el fraude, segmentado por tipo de transacción.")
    st.image("Boxplot_mont_tipo_y_fraud_2.png")

# Sección 7: Fraude por día y hora
with st.container():
    st.markdown("### Cantidad de transacciones fraudulentas por día y por hora")
    st.image("Cant_transacc_fraud_por_dia.png")
    st.image("Cant_transacc_fraud_por_horario.png")



# Display image if it exists
# try:
#     st.image("fraude_imagen.png")
# except FileNotFoundError:
#     logging.warning("Image 'fraude_imagen.png' not found.")

# Radio button for selecting a column
# selected_column = st.radio("Elige una opción", df.columns)

# Calculate and display fraud statistics
# try:
#     fraudes = df[df['isFraud'] == 1]
#     fraudes_por_tipo = fraudes.groupby('type').size()
#     st.header("Fraudes agrupados por tipo de transacción")
#     st.dataframe(fraudes_por_tipo.to_frame(name="Cantidad"))

    # Display a bar chart if matplotlib is installed
#     if plt:
#         fig, ax = plt.subplots()
#         fraudes_por_tipo.plot(kind='bar', ax=ax)
#         ax.set_title('Fraudes por tipo de transacción')
#         ax.set_xlabel('Tipo de transacción')
#         ax.set_ylabel('Cantidad')
#         st.pyplot(fig)
# except Exception as e:
#     logging.error("Error displaying fraud statistics:", e)
#     st.error("An error occurred while calculating or displaying fraud statistics.")

# Add a placeholder for future analysis
# st.markdown("Texto"

# Streamlit cache (optional)
#@st.cache(allow_output_mutation=True)

# Run the app
#if __name__ == "__main__":
#   st.run()
