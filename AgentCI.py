import streamlit as st
import streamlit.components.v1 as components

# Configuración de la página
st.set_page_config(
    page_title="CONSTRUINMUNIZA - Asistente Virtual",
    page_icon="🌲",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilos CSS optimizados para diseño compacto y profesional
st.markdown("""
<style>
    /* Estilos generales */
    .main {
        background-color: #ffffff;
        padding: 0 !important;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    
    /* Eliminar espacios innecesarios */
    .block-container {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
        margin-top: 0 !important;
    }
    .css-18e3th9 {
        padding-top: 0 !important;
    }
    .css-1d391kg {
        padding-top: 0 !important;
    }
    
    /* Header compacto */
    .header-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 1rem 2rem;
        background-color: #f8f9fa;
        border-bottom: 1px solid #eaeaea;
        margin-bottom: 0.5rem;
    }
    .header-left {
        display: flex;
        flex-direction: column;
    }
    .company-name {
        color: #031B4E;
        font-size: 1.8rem;
        font-weight: 700;
        margin: 0;
        line-height: 1.2;
    }
    .tagline {
        color: #555;
        font-size: 0.9rem;
        margin: 0;
    }
    
    /* Contenedor de chatbot */
    .chatbot-container {
        padding: 0;
        margin: 0 auto;
        width: 100%;
    }
    
    /* Productos */
    .products-container {
        display: flex;
        justify-content: center;
        padding: 0.5rem 1rem;
        background-color: #f1f1f1;
        border-radius: 4px;
        margin: 0.5rem 0;
    }
    .product-list {
        display: flex;
        gap: 2rem;
    }
    .product-item {
        margin: 0;
        padding: 0;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: #666;
        font-size: 0.75rem;
        padding: 0.5rem 0;
        border-top: 1px solid #eaeaea;
        margin-top: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Header compacto con información de la empresa
st.markdown("""
<div class="header-container">
    <div class="header-left">
        <h1 class="company-name">CONSTRUINMUNIZA</h1>
        <p class="tagline">Especialistas en procesamiento de madera de pino patula</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Lista de productos en formato horizontal
st.markdown("""
<div class="products-container">
    <div class="product-list">
        <div class="product-item">
            <strong>Madera aserrada</strong>
        </div>
        <div class="product-item">
            <strong>Tablas deck</strong>
        </div>
        <div class="product-item">
            <strong>Tablonería</strong>
        </div>
        <div class="product-item">
            <strong>Tablillas</strong>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Chatbot integrado - sin contenedor adicional para reducir espacio
chatbot_html = """
<script async
  src="https://agent-bc5f7ecd070b4c327aa8-h3546.ondigitalocean.app/static/chatbot/widget.js"
  data-agent-id="39dbb510-f2cd-11ef-bf8f-4e013e2ddde4"
  data-chatbot-id="lGjzrqKBLeaqTW9gfodSSh6IFkvP3xyu"
  data-name="Asesor-CI Chatbot"
  data-primary-color="#031B4E"
  data-secondary-color="#E5E8ED"
  data-button-background-color="#0061EB"
  data-starting-message="Hola!!, soy tu asistente digital de CONSTRUINMUNIZA, en que te puedo ayudar?"
  data-logo="/static/chatbot/icons/default-agent.svg">
</script>
"""
components.html(chatbot_html, height=550)

# Footer minimalista
st.markdown('<div class="footer">© 2025 CONSTRUINMUNIZA - Procesamiento sostenible de madera de pino patula</div>', unsafe_allow_html=True)
