import streamlit as st
from PIL import Image
import io

import modelvision
from modelvision import analizar_frigorifico, obtener_ingredientes_ingles

# Configuración de la página
st.set_page_config(
    page_title="The Fridge Survival",
    page_icon="🥗",
    layout="wide"
)

st.markdown("""
<h1 style='text-align: center;'>The Fridge Survival 🥗</h1>
<h4 style='text-align: center;'>Upload a picture of your refrigerator and we'll suggest recipes.</h4>
""", unsafe_allow_html=True)

# Subir imagen
uploaded_file = st.file_uploader("Upload an image to get started", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded Image", width=700)

    # Análisis de la imagen
    with st.spinner("Detecting ingredients..."):
        resultado = analizar_frigorifico(img)

    if resultado:
        st.success("Ingredients detected successfully!")
        st.write("### Found ingredients:")
        ingredientes_ingles = obtener_ingredientes_ingles(resultado)
        for ingrediente in ingredientes_ingles:
            st.write(f"- {ingrediente}")

        # Simulación de recetas recomendadas (aquí puedes implementar tu lógica de recomendación)
        st.write("### Recommended Recipes:")
        recetas = [
            {"nombre": "Tortilla con queso", "score": 0.89},
            {"nombre": "Ensalada cesar", "score": 0.76},
            {"nombre": "Huevos al plato", "score": 0.64}
        ]

        for receta in recetas:
            st.write(f"{receta['nombre']} (Compatibility: {receta['score']*100:.1f}%)")
            st.progress(receta["score"])

    else:
        st.error("Error detecting ingredients. Please try again with another image.")
