import streamlit as st
import streamlit.components.v1 as components
import base64
from PIL import Image
import io

# Configuración de la página
st.set_page_config(
    page_title="CONSTRUINMUNIZA - Asistente Virtual",
    page_icon="🌲",
    layout="wide",
    initial_sidebar_state="collapsed"  # Sidebar colapsado inicialmente para más espacio central
)

# Estilos CSS personalizados (simplificados)
st.markdown("""
<style>
    .main {
        background-color: #ffffff;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .logo-container {
        display: flex;
        justify-content: center;
        margin: 2rem 0;
    }
    .logo {
        max-height: 150px;
    }
    .company-name {
        text-align: center;
        color: #031B4E;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .tagline {
        text-align: center;
        color: #555;
        font-size: 1.4rem;
        margin-bottom: 2.5rem;
    }
    .chatbot-container {
        background-color: white;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem auto;
        width: 100%;
        min-height: 500px;
    }
    .footer {
        margin-top: 2rem;
        text-align: center;
        color: #555;
        font-size: 0.9rem;
        padding-top: 1rem;
    }
    /* Eliminar bordes de los widgets de Streamlit */
    .block-container {
        padding-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Encabezado con logo centralizado
st.markdown('<h1 class="company-name">CONSTRUINMUNIZA</h1>', unsafe_allow_html=True)
st.markdown('<p class="tagline">Especialistas en procesamiento de madera de pino patula</p>', unsafe_allow_html=True)


# Breve descripción
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.write("""
    ### Madera de pino patula sostenible
    
    Procesamos madera de bosques de reforestación propios certificados FSC, 
    con procesos de cilindrado, secado e inmunización que garantizan 
    productos de alta calidad y durabilidad.
    """)

# Contenedor para el chatbot (simplificado y centrado)
st.markdown('<div class="chatbot-container">', unsafe_allow_html=True)

# Nuevo snippet del chatbot actualizado
chatbot_html = """
<script async
  src="https://agent-bc5f7ecd070b4c327aa8-h3546.ondigitalocean.app/static/chatbot/widget.js"
  data-agent-id="39dbb510-f2cd-11ef-bf8f-4e013e2ddde4"
  data-chatbot-id="lGjzrqKBLeaqTW9gfodSSh6IFkvP3xyu"
  data-name="Asesor-CI Chatbot"
  data-primary-color="#031B4E"
  data-secondary-color="#E5E8ED"
  data-button-background-color="#0061EB"
  data-starting-message="Hola !!, en que te puedo ayudar?"
  data-logo="/static/chatbot/icons/default-agent.svg">
</script>
"""

components.html(chatbot_html, height=600)
st.markdown('</div>', unsafe_allow_html=True)

# Información básica de productos en formato simple
st.subheader("Nuestros Productos")
col1, col2 = st.columns(2)
with col1:
    st.write("• Madera aserrada")
    st.write("• Tablas deck")
with col2:
    st.write("• Tablonería")
    st.write("• Tablillas")

# Pie de página simplificado
st.markdown('<div class="footer">'
            '© 2025 CONSTRUINMUNIZA. Todos los derechos reservados.'
            '</div>', unsafe_allow_html=True)
