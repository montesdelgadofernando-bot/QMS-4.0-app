import streamlit as st
import pandas as pd
from datetime import datetime
import time

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Nexus QMS 4.0 - Magna Scale",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --- ESTILOS PERSONALIZADOS (DARK INDUSTRIAL) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #020617;
        color: #f8fafc;
    }
    
    .main {
        background-color: #020617;
    }
    
    /* Estilo de Tarjetas */
    .metric-card {
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(255,255,255,0.1);
        padding: 1.5rem;
        border-radius: 1rem;
        text-align: center;
    }
    
    /* Botones Grandes */
    .stButton>button {
        width: 100%;
        border-radius: 0.75rem;
        height: 3.5rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        background: linear-gradient(135deg, #d97706 0%, #b45309 100%);
        border: none;
        color: white;
    }
    
    /* Alertas */
    .alert-banner {
        background: linear-gradient(90deg, #ef4444 0%, #991b1b 100%);
        padding: 1rem;
        border-radius: 0.75rem;
        border-left: 5px solid #ffffff;
        margin-bottom: 1rem;
    }
    
    /* Chat IA */
    .chat-bubble-ai {
        background: rgba(30, 58, 138, 0.4);
        border: 1px solid #3b82f6;
        padding: 1rem;
        border-radius: 0.75rem 0.75rem 0.75rem 0px;
        margin: 0.5rem 0;
    }
    
    /* Formato Oficial SOP */
    .sop-official {
        background: white;
        color: #1e293b;
        padding: 2rem;
        border: 2px solid #0f172a;
        border-radius: 0.25rem;
        font-family: 'Courier New', Courier, monospace;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR / NAVEGACIÓN ---
with st.sidebar:
    st.image("https://www.magna.com/ResourcePackages/Magna/assets/dist/images/magna-logo.svg", width=150)
    st.title("Nexus Control Panel")
    menu = st.radio("Ir a:", [
        "🏠 Dashboard Gemba", 
        "🚨 Alertas y Actualizaciones", 
        "🖊️ Aprobaciones y Firmas", 
        "📂 Visor de Documentos",
        "🛠️ Dueño de Proceso (AI Studio)"
    ])
    st.info("Usuario: Fernando Montes\nRol: Strategist")

# --- LÓGICA DE LA APP ---

if menu == "🏠 Dashboard Gemba":
    st.markdown('<h1 style="color:white; margin-bottom:0;">NEXUS <span style="color:#d97706;">QMS</span></h1>', unsafe_allow_html=True)
    st.caption("Planta Magna Norte | Línea 2 | Turno B")
    
    # KPIs
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="metric-card"><p style="font-size:0.7rem; color:#94a3b8;">SCRAP ACTUAL</p><h2 style="color:#10b981; margin:0;">0.4%</h2></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><p style="font-size:0.7rem; color:#94a3b8;">OEE L2</p><h2 style="color:white; margin:0;">88%</h2></div>', unsafe_allow_html=True)
    
    st.write("---")
    
    # QMSChat 4.0
    st.subheader("🤖 QMSChat 4.0")
    user_query = st.text_input("Pregunta a la IA sobre parámetros o estándares:", placeholder="Ej: ¿Tolerancia de espesor pieza A-102?")
    
    if user_query:
        with st.spinner('Extrayendo dato de la Bóveda Cloud...'):
            time.sleep(1.5)
            st.markdown(f"""
                <div class="chat-bubble-ai">
                    <p style="font-size:0.9rem; margin:0;"><strong>Nexus AI:</strong> Según el <b>SOP-102 Rev. 5</b> (Aprobado hoy 08:15 AM), la tolerancia es:</p>
                    <h3 style="color:#10b981; margin:0.5rem 0;">2.5mm ± 0.1mm</h3>
                    <p style="font-size:0.7rem; color:#94a3b8; font-style:italic;">Dato validado por Ingeniería de Procesos.</p>
                </div>
            """, unsafe_allow_html=True)

elif menu == "🚨 Alertas y Actualizaciones":
    st.title("Centro de Respuesta")
    
    st.markdown("""
        <div class="alert-banner">
            <h4 style="margin:0; color:white;">⚠️ Q-ALERT ACTIVA: #892</h4>
            <p style="font-size:0.8rem; margin:0;">Derrame en Lote 45X. Inspección visual 100% requerida en sellos.</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("Confirmar Lectura y Continuar Operación"):
        st.success("Lectura registrada en el Audit Trail IATF.")
        
    st.write("### Actualizaciones Recientes")
    st.info("🔄 **SOP-102:** Nueva revisión 5 liberada hoy. (Cambio en parámetros de temperatura).")
    st.warning("📅 **Auditoría Interna:** Programada para mañana 09:00 AM en Línea 3.")

elif menu == "🖊️ Aprobaciones y Firmas":
    st.title("Bandeja Directiva")
    st.write("Documentos pendientes de su firma criptográfica:")
    
    with st.expander("SOP-204: Ensamble de Puertas Lateral (Rev. 2)"):
        st.write("**Solicitante:** Ing. Ricardo Salinas")
        st.write("**Cambio:** Ajuste en torque de tornillos de seguridad de 12Nm a 15Nm.")
        st.markdown("[Ver Documento Adjunto PDF]")
        if st.button("Firmar y Liberar a Piso"):
            st.balloons()
            st.success("Documento firmado digitalmente. Notificación enviada a Línea 1.")

elif menu == "📂 Visor de Documentos":
    st.title("Biblioteca Digital")
    search_doc = st.text_input("Buscar procedimiento...", placeholder="Ej: Control Plan, AMEF...")
    
    st.write("### Resultados")
    docs = {
        "SOP-102": "Procedimiento de Inyección Plástica",
        "CP-L2": "Plan de Control Línea 2",
        "AMEF-CH": "Análisis de Modo y Efecto de Falla - Chassis"
    }
    for code, name in docs.items():
        col_d1, col_d2 = st.columns([3, 1])
        col_d1.write(f"**{code}**: {name}")
        if col_d2.button("Ver", key=code):
            st.image("https://via.placeholder.com/600x800.png?text=VISOR+SOP+VIGENTE+MAGNA", caption=f"Visualizando {code} Rev. Actual")

elif menu == "🛠️ Dueño de Proceso (AI Studio)":
    st.title("Nexus Studio")
    st.write("Actualice estándares en segundos usando IA.")
    
    st.markdown("### 1. Ingrese el cambio")
    raw_text = st.text_area("Describa la actualización en lenguaje natural:", 
                            placeholder="El cliente pidió que ahora la temperatura no pase de 115 grados y que el operador use guantes de nitrilo.")
    
    st.markdown("### 2. Seleccione el Prompt de Formateo")
    prompt_type = st.selectbox("Formato Destino:", ["IATF Official Standard", "Visual Work Instruction", "Safety Alert"])
    
    if st.button("Generar Borrador de Estándar"):
        with st.spinner('La IA está estructurando el documento oficial...'):
            time.sleep(2)
            st.markdown("### 3. Vista Previa del Documento Generado")
            st.markdown(f"""
                <div class="sop-official">
                    <table style="width:100%; border-bottom: 2px solid black;">
                        <tr>
                            <td><b>MAGNA INTERNATIONAL</b></td>
                            <td style="text-align:right;"><b>CÓDIGO: SOP-AI-01</b></td>
                        </tr>
                    </table>
                    <h2 style="text-align:center;">ESTÁNDAR OPERATIVO</h2>
                    <p><b>FECHA:</b> {datetime.now().strftime("%Y-%m-%d")}</p>
                    <p><b>DESCRIPCIÓN DEL CAMBIO:</b></p>
                    <p style="background:#f1f5f9; padding:10px;">{raw_text}</p>
                    <hr>
                    <h4>Puntos Críticos de Control:</h4>
                    <ul>
                        <li><b>Temperatura Máxima:</b> 115°C (Requisito de Cliente).</li>
                        <li><b>EPP Requerido:</b> Guantes de Nitrilo.</li>
                    </ul>
                    <p style="margin-top:50px; border-top:1px solid black; width:200px;">Firma del Dueño de Proceso</p>
                </div>
            """, unsafe_allow_html=True)
            st.download_button("Descargar PDF para Aprobación", "Contenido del PDF simulado", file_name="SOP_Draft.pdf")

# --- FOOTER ---
st.markdown("---")
st.markdown('<p style="text-align:center; font-size:0.7rem; color:#64748b;">NEXUS QMS 4.0 | INTELIGENCIA OPERATIVA TIER 1</p>', unsafe_allow_html=True)