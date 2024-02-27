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
st.title("Probando Streamlit :hand:")
st.text("No Country Proyecto detección de fraudes")

st.image("fraude_imagen.png")

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
