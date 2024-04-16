
import streamlit as st
import pandas as pd
from datetime import datetime
import webbrowser
import numpy as np


#Configuração da página
st.set_page_config(
    page_title="Home",
    page_icon="🏠",
)


#Carregamento/ tratamento dos dados
if "data" not in st.session_state:
    #df = pd.read_csv(r"C:\dev\gtp_python\gemini\notif_dengue_2024_final.csv", sep=';', encoding='latin-1', index_col=0)
    df = pd.read_csv("notif_dengue_2024_final.csv", sep=';', encoding='latin-1', index_col=0)
    
    # Seleciona uma amostra aleatória linhas do DataFrame
    df = df.sample(n=200, random_state=42)

    #Ajustando o formato do campo para idade
    df['IDADE'] = df['IDADE'].replace([np.inf, -np.inf], np.nan).fillna(0)
    df['IDADE'] = df['IDADE'].astype(int)

    #Para compartilhar o mesmo dataframe entre as páginas
    st.session_state["data"] = df

#opção para adicionar textos
st.write("## Uso de inteligência artifical para analisar casos de dengue 2024-BR!🦟")

#opção para adicionar filtro ou outras informações na parte esquerda da página
st.sidebar.markdown("codígo fonte - [github] (https://github.com/)")


#opção para adicionar botão com link
bt = st.button("Acesse os dados no Kaggle")
if bt:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/jadsonrafael/notificao-de-casos-de-dengue-2024-br?resource=download")

#opção para adicionar texto na página formatado
st.markdown(
    """
Este projeto visa utilizar a **inteligência artificial do Chat-GPT** para analisar um conjunto de dados
de casos de dengue no **Brasil em 2024**, este conjunto de dados contém **237.172** registros, porem para o modelo  de teste foi utilizado **200 registros aleatórios**
"""
)
