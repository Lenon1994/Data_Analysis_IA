**Introdução**
O modelo da aplicação foi separado em 3 páginas.
Página 1: Home
    Nesta página foi feito o processamento dos dados e tratativas, alem de inserir um descritivo do projeto

Página 2: Resultados
    Disponibilizado ao usuário a possibilidade de fazer perguntas para IA - Chat_GTP responder referente ao Dateset limitado em 200 registros.
    Obs: Limitação API gratuita.

**Deploy**
Para fazer o deploy foi utilizado o servido do streamilt "https://streamlit.io/", neste servidor é possivel disponibilizar até 3 projetos de forma gratuita, abaixo passo a passo para fazer o deploy do modelo


**Execução local**

Caso desejar rodar o modelo em ambiente local, será necessário clonar as informações do github e no terminal de comando no local aonde estiver realizar do clone do repositório executar o seguinte comando
"streamlit run 'nome do arquivo'" 

Exemplo: streamlit run 1_Home.py


**Links uteis**

Links:
Video exemplo:
 - "https://www.youtube.com/watch?v=6dsUQfsovCw&t=609s"

Documentação streamilt
 - "https://docs.streamlit.io/library/api-reference/charts/st.altair_chart"

API
 - "https://platform.openai.com/api-keys"  - credenciais
 - "https://platform.openai.com/docs/api-reference/chat/create?lang=python" - utilização 