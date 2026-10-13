import streamlit as st
from PIL import Image
from pathlib import Path

BASE = Path(__file__).parent

def cargar(nombre):
    return Image.open(BASE / nombre)
  
st.title("Aplicaciones Realizadas.")

with st.sidebar:
  st.subheader("Aplicaciones Realizadas en Clase.")
  parrafo = (
    "En este sitio web podremos observar el portafolio de aplicaciones desarrolladas "
    "en clase, donde podremos explorar diversos sitios wep, pensados para aprender un "
    "poco respecto a la optimizacion de codigo, vectores, matrices, entre muchos otros."
  )
  st.write(parrafo)

url_ia="https://sites.google.com/view/computacinavanzada/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("Proyecto 1")
 image = cargar('ptf1.jpg')
 st.image(image, width=190)
 st.write("En el siguiente enlace usaremos vectores y matrices para buscar la fruta más parecida.") 
 url = "https://proyecto1ca.streamlit.app/"
 st.write(f"Fruta más parecida: [Enlace]({url})")

 st.subheader("Proyecto 2")
 image = cargar('ptf2.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace veremos cómo las derivadas y el gradiente permiten transformar un problema matemático en un proceso computacional de búsqueda y optimización.") 
 url = "https://proyecto2cajp.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("Entrenando Modelos")
 image = cargar('OIG5.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace veremos como puedes usar tu modelo entrenado.") 
 url = "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"
 st.write(f"YOLO: [Enlace]({url})")

with col2: 
 st.subheader("Conversión de voz a texto")
 image = cargar('OIG8.jpg')
 st.image(image, width=200)
 st.write("En el siguiente veremos una aplicación que usa la conversión de voz a texto.") 
 url = "https://traductorw.streamlit.app/"
 st.write(f"Voz a texto: [Enlace]({url})")

 st.subheader("Análisis de Datos")
 image = cargar('data_analisis.png')
 st.image(image, width=190)
 st.write("En el siguiente enlace veremos como se pueden analizar datos usando agentes.") 
 url = "https://dataagente.streamlit.app/"
 st.write(f"Datos: [Enlace]({url})")

 st.subheader("Trasnscriptor Audio y Video")
 image = cargar('OIG3.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace veremos como realizamos transcripciones de audio/video.") 
 url = "https://transcript-whisper.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")


with col3: 
 st.subheader("Generación en Contexto")
 image = cargar('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En el siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://chatpdf-cc.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("Análisis de Imagen")
 image = cargar('OIG4.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de análisis en Imágenes.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("Sistema Ciberfísico")
 image = cargar('OIG6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")


