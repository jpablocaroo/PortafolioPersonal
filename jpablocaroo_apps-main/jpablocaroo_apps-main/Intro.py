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
    "en clase, donde podremos explorar diversos sitios web, pensados para aprender un "
    "poco respecto a la optimizacion de codigo usando estrategias interesantes."
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
 st.write("En el siguiente enlace veremos cómo las derivadas y el gradiente permiten optimizar un problema matematico.") 
 url = "https://proyecto2cajp.streamlit.app/"
 st.write(f"Descenso de Gradiente: [Enlace]({url})")

 st.subheader("Proyecto 3")
 image = cargar('ptf3.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace veremos la cadena causal entre la lógica, la complejidad (Big-O) y la vectorización.") 
 url = "https://proyecto3ca.streamlit.app/"
 st.write(f"Detector de anomalías: [Enlace]({url})")

 st.subheader("Proyecto 4")
 image = cargar('ptf4.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace, aprenderemos a preparar datos antes de construir cualquier modelo.") 
 url = "https://proyecto4ca.streamlit.app/"
 st.write(f"Preparacion de Datos: [Enlace]({url})")

with col2: 

 st.subheader("Proyecto 5")
 image = cargar('ptf5.jpg')
 st.image(image, width=190)
 st.write("En el siguiente enlace veremos el uso de una APIs y endpoints para traer informacion de MARCO") 
 url = "https://dataagente.streamlit.app/"
 st.write(f"Portafolio MARCO [Enlace]({url})")

 st.subheader("Proyecto 6")
 image = cargar('ptf6.jpg')
 st.image(image, width=200)
 st.write("En el siguiente enlace aprenderemos a evaluar la calidad de las predicciones mediante métricas como R², MAE y RMSE") 
 url = "https://transcript-whisper.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")

 st.subheader("Proyecto 7")
 image = cargar('ptf7.png')
 st.image(image, width=190)
 st.write("En el siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://chatpdf-cc.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("Proyecto 8")
 image = cargar('ptf8.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de análisis en Imágenes.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")
    
with col3: 

 st.subheader("Proyecto 9")
 image = cargar('ptf9.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")
    

 st.subheader("Proyecto 10")
 image = cargar('ptf10.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")

 st.subheader("Proyecto 11")
 image = cargar('ptf11.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")

 st.subheader("Proyecto 12")
 image = cargar('ptf12.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")

 st.subheader("Proyecto 13")
 image = cargar('ptf13.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")

