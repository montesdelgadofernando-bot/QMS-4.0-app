import streamlit as st
import pandas as pd
from datetime import datetime
import time

# --- CONFIGURACIÓN DE PÁGINA (OPTIMIZADO PARA MÓVIL Y TABLET) ---
st.set_page_config(
    page_title="Nexus QMS 4.0 - Magna Scale",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --- DISEÑO UI PREMIUM (DARK INDUSTRIAL) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');
    
    .stApp {
        background-color: #020617;
        color: #f8fafc;
        font-family: 'Inter', sans-serif;
    }

    /* Tarjetas de Métricas de Planta */
    .metric-card {
        background: #0f172a;
        border: 1px solid #1e293b;
        padding: 1.2rem;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }

    /* Banner de Alerta Crítica IATF */
    .q-alert-banner {
        background: linear-gradient(90deg, #ef4444 0%, #7f1d1d 100%);
        color: white;
        padding: 1rem;
        border-radius: 8px;
        border-left: 6px solid #ffffff;
        margin-bottom: 1.5rem;
    }

    /* Burbujas de Chat IA (QMSChat) */
    .ai-bubble {
        background: rgba(30, 58, 138, 0.4);
        border: 1px solid #3b82f6;
        padding: 1rem;
        border-radius: 12px 12px 12px 0px;
        margin-bottom: 1rem;
    }

    /* Formato de Documento Oficial Magna (Simulación) */
    .official-sop-document {
        background: white;
        color: #1e293b;
        padding: 2.5rem;
        border: 2px solid #000;
        font-family: 'Courier New', Courier, monospace;
        margin-top: 1.5rem;
        box-shadow: 8px 8px 0px #1e293b;
    }

    /* Botones Interactivos */
    .stButton>button {
        background: linear-gradient(135deg, #d97706 0%, #b45309 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.8rem;
        font-weight: bold;
        width: 100%;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(217, 119, 6, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVEGACIÓN DE LA APP ---
st.sidebar.image("https://www.magna.com/ResourcePackages/Magna/assets/dist/images/magna-logo.svg", width=150)
menu = st.selectbox("--- SELECCIONAR MÓDULO ---", [
    "🏠 Dashboard de Producción", 
    "🚨 Centro de Alertas", 
    "🖋️ Firmas y Aprobaciones", 
    "📂 Visor Documental",
    "🛠️ Studio: Dueño de Proceso (IA)"
])

# --- MÓDULO 1: DASHBOARD ---
if menu == "🏠 Dashboard de Producción":
    st.markdown("<h1 style='text-align: center;'>NEXUS <span style='color: #d97706;'>QMS 4.0</span></h1>", unsafe_allow_html=True)
    st.caption("Visibilidad Global | Basado en Microsoft 365 / Google Workspace")
    
    # Contexto de Línea
    c1, c2, c3 = st.columns(3)
    with c1:
        st.selectbox("Línea", ["L-01", "L-02", "L-03"], index=1)
    with c2:
        st.selectbox("Turno", ["1ero (A)", "2do (B)", "3ero (C)"], index=1)
    with c3:
        st.selectbox("Operador", ["450 - J. Pérez", "322 - M. Luna"])

    # KPIs Reales
    kpi1, kpi2, kpi3 = st.columns(3)
    with kpi1:
        st.markdown('<div class="metric-card"><p style="font-size:0.7rem; color:#94a3b8;">SCRAP</p><h3 style="color:#10b981; margin:0;">0.4%</h3></div>', unsafe_allow_html=True)
    with kpi2:
        st.markdown('<div class="metric-card"><p style="font-size:0.7rem; color:#94a3b8;">OEE</p><h3 style="color:white; margin:0;">88%</h3></div>', unsafe_allow_html=True)
    with kpi3:
        st.markdown('<div class="metric-card"><p style="font-size:0.7rem; color:#94a3b8;">APEGO IATF</p><h3 style="color:white; margin:0;">98%</h3></div>', unsafe_allow_html=True)

    st.write("---")
    
    # QMSChat 4.0
    st.subheader("🤖 QMSChat 4.0")
    pregunta = st.text_input("Consultar estándar técnico:", placeholder="Ej: ¿Cuál es el torque para la pieza A-102?")
    
    if pregunta:
        with st.spinner("Consultando Bóveda Documental Segura..."):
            time.sleep(1.2)
            st.markdown(f"""
                <div class="ai-bubble">
                    <b>Nexus AI:</b> El torque especificado en el <b>SOP-204 Rev. 5</b> para la pieza A-102 es de <b>15Nm ± 1.5Nm</b>.<br>
                    <small style="color: #94a3b8;">(Dato validado por Ingeniería el {datetime.now().strftime("%d/%m/%Y")})</small>
                </div>
            """, unsafe_allow_html=True)

# --- MÓDULO 2: ALERTAS ---
elif menu == "🚨 Centro de Alertas":
    st.title("Control de Contenciones")
    
    st.markdown("""
        <div class="q-alert-banner">
            <h3 style="margin:0;">⚠️ Q-ALERT ACTIVA: #892</h3>
            <p style="margin:0; font-size:0.9rem;">Derrame Lote 45X detectado. Inspección visual 100% obligatoria en sellos críticos.</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("CONFIRMAR LECTURA (REGISTRO IATF)"):
        st.success("Confirmación registrada en el Audit Trail. Operación autorizada.")

    st.write("### Actualizaciones Recientes")
    st.info("🔄 **SOP-102:** Nueva revisión liberada hoy por cambio de material.")
    st.warning("📅 **Auditoría Externa:** Próxima visita de IATF programada.")

# --- MÓDULO 3: APROBACIONES ---
elif menu == "🖋️ Firmas y Aprobaciones":
    st.title("Bandeja Directiva")
    st.write("Aprobaciones pendientes de su firma electrónica:")
    
    with st.expander("📝 SOP-305: Cambio de Herramental (Rev. 2)"):
        st.write("**Ingeniero:** Ricardo Salinas")
        st.write("**Justificación:** Reducción de tiempos de set-up en un 12%.")
        if st.button("FIRMAR Y LIBERAR A LÍNEA"):
            st.balloons()
            st.success("Documento firmado. Se ha notificado automáticamente a las pantallas de piso.")

# --- MÓDULO 5: AI STUDIO (LA MAGIA) ---
elif menu == "🛠️ Studio: Dueño de Proceso (IA)":
    st.title("Nexus AI Studio")
    st.write("Actualice estándares de planta en segundos usando lenguaje natural.")
    
    raw_input = st.text_area("Describa el cambio técnico:", 
                             placeholder="Ej: A partir de hoy el torque sube a 20 Nm y hay que usar guantes azules.")
    
    prompt_style = st.selectbox("Formato de Salida Oficial:", ["IATF Master Standard", "Visual Work Instruction", "Safety Alert (OPL)"])
    
    if st.button("GENERAR DOCUMENTO OFICIAL"):
        with st.spinner("La IA está estructurando el documento bajo normas Magna..."):
            time.sleep(2.5)
            st.markdown("### Vista Previa del Estándar Generado:")
            st.markdown(f"""
                <div class="official-sop-document">
                    <div style="border-bottom: 2px solid black; padding-bottom: 5px;">
                        <span style="font-size:1.1rem; font-weight:bold;">MAGNA INTERNATIONAL</span>
                        <span style="float:right;"><b>ID: SOP-AI-NEW</b></span>
                    </div>
                    <h2 style="text-align:center; margin: 1.5rem 0;">ESTÁNDAR OPERATIVO DE CALIDAD</h2>
                    <p><b>FECHA:</b> {datetime.now().strftime("%d/%m/%Y")}</p>
                    <p><b>RESUMEN DEL CAMBIO:</b></p>
                    <div style="background:#f8fafc; padding:15px; border: 1px dashed #000; font-size: 0.9rem;">
                        {raw_input}
                    </div>
                    <br>
                    <table style="width:100%; border-collapse: collapse;">
                        <tr style="border: 1px solid black;">
                            <td style="padding: 10px; border: 1px solid black;"><b>Especificación:</b></td>
                            <td style="padding: 10px; border: 1px solid black;"><b>Detalle:</b></td>
                        </tr>
                        <tr>
                            <td style="padding: 10px; border: 1px solid black;">Torque de Ensamble</td>
                            <td style="padding: 10px; border: 1px solid black;">20 Nm ± 2</td>
                        </tr>
                        <tr>
                            <td style="padding: 10px; border: 1px solid black;">EPP Crítico</td>
                            <td style="padding: 10px; border: 1px solid black;">Guantes Nitrilo Azules</td>
                        </tr>
                    </table>
                    <div style="margin-top: 50px; border-top: 1px solid black; width: 220px; text-align:center;">
                        Firma Electrónica Dueño Proceso
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.download_button("DESCARGAR PDF PARA APROBACIÓN", "Data simulada", file_name="SOP_Draft_Magna.pdf")

# --- FOOTER ---
st.markdown("<br><hr><p style='text-align: center; color: #64748b; font-size: 0.8rem;'>NEXUS QMS 4.0 | PROTOTIPO TIER 1 | FERNANDO MONTES</p>", unsafe_allow_html=True)
