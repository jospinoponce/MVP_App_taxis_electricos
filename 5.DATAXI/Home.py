# Librerías
import pandas as pd
import streamlit as st
from PIL import Image
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="Dashboard", page_icon=":car:", layout="wide")

# Carga de datos
df = pd.read_csv("data/TLC_Monthy_Report_NYC.csv")

# Sidebar con secciones
options = ['Home','Goals','Market']
query = st.sidebar.radio('Sección', options)

# =======================
# Sección Home
# =======================
# =======================
# Home Section
# =======================
if query == options[0]:

    image = Image.open('pages/DGRL.png')
    st.image(image, use_container_width=True)

    st.markdown("""
    <h1 style='text-align:center;'>Electric Taxi Fleet – NYC</h1>

    <h3 style='text-align:center; color:#6c757d; margin-top:-10px;'>
    Minimum Viable Product (MVP) to evaluate the feasibility of an electric taxi fleet in New York City
    </h3>

    <br>

    <p style='text-align:justify; font-size:18px;'>
    This project aims to develop a <b>Minimum Viable Product (MVP)</b> designed to assess the feasibility of
    implementing an <b>electric vehicle fleet</b> as a sustainable alternative to the traditional
    <b>yellow taxi system in New York City</b>.
    </p>

    <p style='text-align:justify; font-size:18px;'>
    Through market analysis, demand distribution, revenue projections, and environmental impact metrics,
    this dashboard delivers data-driven insights to support decision-making for investors, operators,
    and public stakeholders.
    </p>

    <h4>Scope of the MVP</h4>
    <ul style='font-size:17px;'>
        <li>Market size and demand analysis by borough</li>
        <li>Revenue projections and profitability assessment</li>
        <li>Operational metrics and key performance indicators (KPIs)</li>
        <li>Environmental impact estimation compared to traditional taxis</li>
    </ul>

    <p style='font-size:17px;'>
    The objective is not to deploy a full-scale solution, but to <b>validate assumptions</b>,
    identify risks, and determine whether an electric taxi fleet represents a
    <b>scalable and sustainable opportunity</b> for New York City.
    </p>
    """, unsafe_allow_html=True)


# =======================
# Sección Goals
# =======================
if query == options[1]:
    st.markdown("""
    <style>
    .objectives {
        display: flex;
        flex-direction: row;
        background-color: #f1f1f1;
        border: 2px solid #f1f1f1;
        text-align: center;
        font-size: 20px;
        padding: 5px;
        border-radius: 10px;
        height: 120px;
        margin-bottom: 20px;
        color:#002b36;
        justify-content: space-between;
        align-items: center;
        align-content:center;
    }
    .objectives h4 {
        padding-left:30px;
        width: 60%;
        text-align: center;
        color:#002b36;
    }
    .objectives p {
        width: 30%;
        text-align: center;
        font-size : 20px;
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h2 align="center"> Goals </h2>
    <h3 align="center">This work aims to answer the following questions:</h3>
    <div class="objectives">
        <h4 align="center">¿What are the dimensions of the market?</h4>
        <p>Market Share</p>
    </div>
    <div class="objectives">
        <h4 align="center">¿What are the market prospects?</h4>
        <p>Trends</p>
    </div>
    <div class="objectives">
        <h4 align="center">¿What are the areas with the highest demand?</h4>
        <p>Metrics</p>
    </div>
    <div class="objectives">
        <h4 align="center">¿What are the projected revenues?</h4>
        <p>KPIs</p>
    </div>
    <div class="objectives">
        <h4 align="center">¿What is the projected positive environmental impact?</h4>
        <p>Calculator</p>
    </div>
    """, unsafe_allow_html=True)

# =======================
# Sección Market
# =======================
if query == options[2]:
    st.subheader('Market')
    col1, col2 = st.columns([1, 3])
    with col1:
        st.write('New York City')
        image = Image.open('pages/NYC.png')
        st.image(image, caption='Boroughs')
    with col2:
        st.write('Boroughs')
        image = Image.open('pages/NYCTable.png')
        st.image(image, caption='Data')

    
    
    
    
    

