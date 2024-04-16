import streamlit as st
import pandas as pd
import altair as alt
import google.generativeai as genai

# Configuração da página
st.set_page_config(
    page_title="Resultados",
    page_icon="✨",
)

# Header da página
st.write("## Utilizando IA para analisar os dados!🤖")

# Carregando os dados de home
df = st.session_state.get("data", pd.DataFrame())

# Adiciona uma opção para selecionar todos os estados
if 'ESTADO' in df.columns:
    estado_options = ['Todos os estados'] + df["ESTADO"].unique().tolist()
else:
    estado_options = ['Todos os estados']

# Filtro para selecionar o estado
uf = st.sidebar.selectbox("Estado", estado_options)

# Filtra os dados com base na seleção do estado
if uf != 'Todos os estados':
    df_filtered = df[df["ESTADO"] == uf]
else:
    df_filtered = df.copy()  # Cópia do DataFrame original

# Criando métricas
contagem_casos = len(df_filtered)
media_casos_por_data = int(df_filtered.groupby('DATA').size().mean())
total_estado = df_filtered['ESTADO'].nunique()

# Gráficos evolutivos
df_count = df_filtered.groupby('DATA').size().reset_index(name='TOTAL_REGISTROS')

# Inserindo as métricas
col1, col2, col3 = st.columns(3)
col1.metric("Total de casos", contagem_casos)
col2.metric("Nº médio de casos por dia", media_casos_por_data)
col3.metric("Total de estados", total_estado)

st.write("--------------------------------------------------")

# Gráfico evolutivo de casos por data
st.altair_chart(
    alt.Chart(df_count)
    .mark_line()
    .encode(
        x='DATA',   
        y='TOTAL_REGISTROS'
    )
    .properties(
        width=800, 
        height=300,
        title='Evolução do número de casos de dengue por data'
    )
)

# Inserindo as informações para input de dados para o GTP
st.write('#### Abaixo faça perguntas para a Inteligência Artificial responder!')
dados_para_gtp = st.text_input('Inserir informações')

# Verifica se dados_para_gtp está preenchido
if dados_para_gtp:
    # Carregando informações para acesso API IA gemini
    GOOGLE_API_KEY='AIzaSyDwgK91t5yCB_a3fhX4CZurdkMgzGjSDX4'  
    genai.configure(api_key=GOOGLE_API_KEY)

    # Modelo API
    model = genai.GenerativeModel('gemini-1.0-pro')
    df_dict = df_filtered.to_dict(orient='records')

    completion = model.generate_content(
        f"o dataset a seguir se refere sobre o numero total de casos de dengue no Brasil no ano de 2024,poderia responder essa pergunta: {dados_para_gtp} sobre este dataset {df_dict}, utilizar somente os dados do dataset compartilhado"
        )

    # Exibe a resposta
    #st.markdown(completion.choices[0].message.content)
    st.markdown(completion.text)

