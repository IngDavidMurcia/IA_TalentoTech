import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie
import json

st.set_page_config(page_title="QUBITS PROJET",page_icon="🤖",layout="wide")


def load_Team_animation(animation_url):
    response = requests.get(animation_url)
    if response.status_code != 200:
        return None
    return response.json()

Team_animation=load_Team_animation("https://lottie.host/a06ca6a1-dc6a-484f-9024-660c26f7f2e0/HWp5vx3FZk.json")

#    def load_lottiefile(filepath: str):
#    with open(filepath, "r") as file:
#        return json.load(file)

#animation = load_lottiefile("imagenes\Animation.json")


#intro

with st.container():
    st.title("Proyecto IA TalentoTech - Equipo QUBITS")
#   st.header("Este proyecto es un requerimiento para optar por la certificación en el bootcamp de IA TalentoTech")
    st.subheader("MODELOS PREDICTIVOS BASADOS EN INTELIGENCIA ARTIFICIAL PARA LA ESTIMACIÓN DE DEMANDA Y PRECIOS EN EL MERCADO DE ENERGÍA ELÉCTRICA EN COLOMBIA")
    st.write("##")
    st.write("### Introducción")
    st.write("""El alcance de este proyecto es netamente academico, los derechos de autor se estipulan en los acuerdos establecidos por la Union temporal de UI training como operador contratado por
MinTic, asi como se indica en las clausulas de registro al bootcamp a cargo de la Universidad de Antiqouia y de la Universidad de Manizales, el proyecto busca aplicar conocimientos
previos y adquiridos durante el bootcamp, en este caso, implementando modelos de IA para predecir precios de la energía tomando como base los datos abiertos de XM sinergox.""")
    st.write("## Metodología :trollface:")
    st.write("""Para la predicción de los precios futuros de la energía se procedera con metodos estadisticos de análisis sobre series temporales atraves de modelos de IA, aprovechando el uso de 
    datos dispuestos cronologicamente en el sitio web de xm sinergox para lograr visualizar como evolucionan dichos datos en funcion del tiempo, las variables a considerar estan dentro
    del conjunto de la demanda, reservas energeticas, consumos y otras. dentro de las tecnologías usadas en el proyecto tenemos,
    - VisualStudioCode como editor 📝
    - python cómo lenguaje 🐍
    - Docker y venv python como entorno virtual para el desarrollo. 🐳
    - librerias python para modelos IA como pandas numpy y tensrflow 🤖
    - streamlit como interfaz de usuario y despliegue ☁️
    - github como repositorio 🐙
    - para el desarrollo se uso ágil scrum con trello como tablero para backlog 💨
    - otras herramientas para la comunicación y almacenamiento en nube, como google drive, whastapp. 🚬 """)
    st.write("##")
    
#Sobre Nosotros

with st.container():
    st.write("---")
    text_column, animation_column = st.columns((2))
    with text_column:
        st.header("Sobre Nosotros 🔎")
        st.subheader("Grupo ✨ QUBITS ✨")
        st.write("""Somos un grupo de estudiantes participantes del programa de IA TalentoTech, Nivel 3, Innovador.
            ## Nuestro grupo se llama QUBITS :punch:
            ### Integrantes :family:
                - David Rodolfo Murcia Peralta - davidmurcia001@gmail.com - @ingdavidmurcia
                - Joe Alexander Jimenez - alexjh765@gmail.com
                - Sebastian Gomez - espacaro@gmail.com
                - Jose Jorge Muñoz - jojotalentech@gmail.com""")
    with animation_column:
        st_lottie(Team_animation, speed=1, width=400, height=400)
    # st.empty()
        
    #Modelo
    
    with st.container():
        st.write("---")
        st.header("PREDICCIÓN DE PRECIO DE LA ENERGÍA ELÉCTRICA EN COLOMBIA 🤖 🪙")
        st.write("##")
        image_column, model_column = st.columns((1,2))
        with image_column:
            #image = Image.open("imagenes/coins.jpg")
            #st.image(image, caption="Monedas del mundo",use_container_width=True)
            st.image("https://randall-romero.github.io/econometria/_images/serie-no-estacionaria.png")
            st.write("Serie de tiempo no estacionaria.")
        with model_column:
            st.write("### Análisis de series de tiempo 📈 atraves de modelos de IA")
            st.write("""Los modelos de IA aplicados en series de tiempo son sistemas computacionales que utilizan técnicas
                    de aprendizaje automático y aprendizaje profundo para procesar datos secuenciales, identificar patrones
                    no lineales, capturar dependencias temporales y realizar predicciones precisas. A diferencia de los
                    métodos estadísticos tradicionales, estos modelos pueden manejar grandes volúmenes de datos, aprender 
                    automáticamente características relevantes y adaptarse a estructuras complejas en los datos.""")
            st.write("##")
#            st.subheader("Estructura:")
#            st.write("##")
        model2_column, model3_column = st.columns((1,2))
            
        with model2_column:
            st.write("##")
        with model3_column:
            # st.empty()
            #st_lottie(animation, width=600)
            Team_animation=load_Team_animation("https://lottie.host/efba96b9-6d02-4465-94d1-31c546368882/sAI9W7HPvJ.json")
            st_lottie(Team_animation, speed=1, width=400, height=400)
    
    #contactenos
    with st.container():
        st.write("---")
        st.header("Contactenos 📧")
        st.write("Si deseas contactarnos para más información o colaboración, por favor llena el siguiente formulario:")
        form = st.form(key="my_form")
        name = form.text_input("Nombre")
        email = form.text_input("Correo Electrónico")
        message = form.text_area("Mensaje")
        submit = form.form_submit_button("Enviar")
        if submit:
            st.write(f"Gracias {name} por tu mensaje, te responderemos a la brevedad posible.")
    