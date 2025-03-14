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
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados
st.markdown("""
<style>
    .main {
        background-color: #f9f9f9;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .header {
        display: flex;
        align-items: center;
        padding: 1rem 0;
        border-bottom: 2px solid #031B4E;
        margin-bottom: 2rem;
    }
    .logo {
        max-height: 80px;
        margin-right: 20px;
    }
    .title {
        color: #031B4E;
        font-size: 2.2rem;
        font-weight: 700;
        margin: 0;
    }
    .subtitle {
        color: #555;
        font-size: 1.2rem;
        margin-top: 0.5rem;
    }
    .footer {
        margin-top: 3rem;
        text-align: center;
        color: #555;
        font-size: 0.9rem;
        border-top: 1px solid #ddd;
        padding-top: 1rem;
    }
    .info-box {
        background-color: #E5E8ED;
        padding: 1.5rem;
        border-radius: 8px;
        margin-bottom: 2rem;
        border-left: 5px solid #0061EB;
    }
    .chatbot-container {
        background-color: white;
        padding: 2rem;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-top: 2rem;
        min-height: 500px;
    }
    .contact-info {
        margin-top: 2rem;
        padding: 1rem;
        background-color: #f0f2f5;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# Función para crear un logo provisional (en caso de no tener uno)
def get_default_logo():
    # Crear una imagen simple con texto "CONSTRUINMUNIZA"
    from PIL import Image, ImageDraw, ImageFont
    img = Image.new('RGB', (300, 80), color=(3, 27, 78))
    d = ImageDraw.Draw(img)
    # Usar una fuente predeterminada
    try:
        font = ImageFont.truetype("arial.ttf", 24)
    except IOError:
        font = ImageFont.load_default()
    
    d.text((20, 30), "CONSTRUINMUNIZA", fill=(255, 255, 255), font=font)
    
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    return buffered.getvalue()

# Cargar el logo (reemplazar la ruta por la ubicación real del logo)
try:
    logo_path = "logo.png"  # Reemplazar con el path real
    with open(logo_path, "rb") as f:
        logo = f.read()
except FileNotFoundError:
    logo = get_default_logo()

# Codificar el logo en base64 para mostrarlo
logo_base64 = base64.b64encode(logo).decode()

# Sidebar con información de la empresa
with st.sidebar:
    st.image(f"data:image/png;base64,{logo_base64}", width=200)
    st.markdown("### Sobre CONSTRUINMUNIZA")
    st.write("""
    Somos una empresa especializada en el procesamiento y 
    tratamiento de madera de pino patula, con un enfoque en 
    la sostenibilidad y calidad. Nuestra madera proviene 
    de bosques de reforestación propios certificados FSC.
    """)
    
    st.markdown("### Nuestros Procesos")
    st.write("1️⃣ **Cilindrado**: Corte radial para acabado cilíndrico")
    st.write("2️⃣ **Secado**: Hornos importados con control preciso")
    st.write("3️⃣ **Inmunización**: Sistema de vacío-presión en autoclave")
    
    st.markdown("### Nuestros Productos")
    st.write("- Madera aserrada")
    st.write("- Tablas deck")
    st.write("- Tablonería")
    st.write("- Tablillas")
    
    st.markdown("### Contacto")
    st.write("📞 Teléfono: +52 (XXX) XXX-XXXX")
    st.write("📧 Email: info@construinmuniza.com")
    st.write("🌐 Web: www.construinmuniza.com")
    st.write("📍 Dirección: [Dirección de la empresa]")

# Contenido principal
st.markdown('<div class="header">'
            f'<img src="data:image/png;base64,{logo_base64}" class="logo">'
            '<div><h1 class="title">CONSTRUINMUNIZA</h1>'
            '<p class="subtitle">Especialistas en procesamiento de madera de pino patula</p></div>'
            '</div>', unsafe_allow_html=True)

st.markdown('<div class="info-box">'
            '<h2>Bienvenido a nuestro Asistente Virtual</h2>'
            '<p>Este asistente está diseñado para proporcionarle información ágil y precisa sobre '
            'nuestro proceso de tratamiento de madera de pino patula, desde el cilindrado hasta la inmunización, '
            'así como detalles sobre nuestros productos sostenibles. Utilícelo para resolver sus dudas al instante.</p>'
            '</div>', unsafe_allow_html=True)

# Contenedor para el chatbot
st.markdown('<div class="chatbot-container">', unsafe_allow_html=True)

# Integrar el widget del chatbot usando components.html
chatbot_html = """
<script async
  src="https://agent-3f4373bb9b9e2521b014-cd9qj.ondigitalocean.app/static/chatbot/widget.js"
  data-agent-id="de703369-fcf2-11ef-bf8f-4e013e2ddde4"
  data-chatbot-id="M1iBgnKnoSo7U1LS4gvPlJbUb5VWTaWG"
  data-name="CONSTRUINMUNIZA Asistente"
  data-primary-color="#031B4E"
  data-secondary-color="#E5E8ED"
  data-button-background-color="#0061EB"
  data-starting-message="¡Hola! Soy el asistente virtual de CONSTRUINMUNIZA. Puedo brindarte información sobre nuestros procesos de cilindrado, secado e inmunización de madera de pino patula, así como detalles de nuestros productos. ¿En qué puedo ayudarte hoy?"
  data-logo="/static/chatbot/icons/default-agent.svg">
</script>
"""

components.html(chatbot_html, height=600)
st.markdown('</div>', unsafe_allow_html=True)

# Información adicional
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Nuestras Ventajas")
    st.write("""
    - Bosques de reforestación propios certificados FSC
    - Ubicados en Caldas y Antioquia (Rio Sucio, Manizales, Yarumal, Angostura)
    - Hornos importados de Italia (Termolegno) con capacidad de 1500 m³/mes
    - Inmunizante CCA tipo C importado de OSMOSE (EE.UU.)
    - Garantía de 20 años de protección contra hongos, xilófagos y termitas
    """)

with col2:
    st.markdown("### Horario de atención")
    st.write("""
    **Lunes a Viernes:** 9:00 AM - 6:00 PM  
    **Sábados:** 10:00 AM - 2:00 PM  
    **Domingos:** Cerrado
    
    Nuestro asistente virtual está disponible 24/7 para responder a sus consultas básicas.
    """)

# Pie de página
st.markdown('<div class="footer">'
            '© 2025 CONSTRUINMUNIZA. Todos los derechos reservados.<br>'
            'Desarrollado con tecnología avanzada para brindar el mejor servicio.'
            '</div>', unsafe_allow_html=True)
