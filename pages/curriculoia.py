import streamlit as st
import time
from openai import OpenAI
from decouple import config
import logging
from datetime import datetime

api_key = config("OPENAI_API_KEY")
assistant_id = config("OPENAI_ASSISTANT_ID")

st.set_page_config(
    page_title="Currículo com IA",
    page_icon="®️",
)

logging.basicConfig(level=logging.INFO)
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
logging.info(f'Currículo com IA acessado em {current_time}')

st.markdown("""
    <style>
        /* Esconde o botão de Deploy */
        [data-testid="stToolbar"] {
            display: none !important;
        }
        .center {
            display: flex;
            justify-content: center;
            align-items: center;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; padding: 10px;'>Currículo com IA</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Baixe o PDF após digitar sua pergunta sobre o currículo do Ronaldo Medeiros!</h4>", unsafe_allow_html=True)

with open("curriculo.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.write("----------------------------------------------------------------")

st.markdown("""
    <style>[data-testid="stSidebarNav"] ul {
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.page_link(page="home.py", label="Home")
st.sidebar.page_link(page="pages/mortystock.py", label="Mortystock")
st.sidebar.page_link(page="pages/fakepinterest.py", label="Fake Pinterest")
st.sidebar.page_link(page="pages/calculadoraprecificacao.py", label="Calculadora de Precificação")
st.sidebar.page_link(page="pages/curriculoia.py", label="Currículo com IA")

st.sidebar.write("----------------------------------------------------------------")
st.sidebar.markdown(
     """
     ### Outros Projetos no GitHub
    - ZapDocker - Node.js + WppConnect + API Openai: [GitHub](https://github.com/ronaldmedeiiros/zapdocker)
    - Liberação de Alunos - Python + Flask (Em Construção): [GitHub](https://github.com/ronaldmedeiiros/sistemaliberacaoalunos)
    - Filmes Paradigma (Trabalho Faculdade) - HTML + JS + CSS: [GitHub](https://github.com/ronaldredeiiros/filmesparadigma)
    """
)
st.sidebar.write("----------------------------------------------------------------")

@st.cache_resource
def load_openai_client_and_assistant():
    client = OpenAI(api_key=api_key)
    my_assistant = client.beta.assistants.retrieve(assistant_id)
    thread = client.beta.threads.create()

    return client, my_assistant, thread

def wait_on_run(client, run, thread):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(0.5)
    return run

def get_assistant_response(user_input=""):
    client, my_assistant, assistant_thread = load_openai_client_and_assistant()
    message = client.beta.threads.messages.create(
        thread_id=assistant_thread.id,
        role="user",
        content=user_input,
    )

    run = client.beta.threads.runs.create(
        thread_id=assistant_thread.id,
        assistant_id=assistant_id,
    )

    run = wait_on_run(client, run, assistant_thread)

    messages = client.beta.threads.messages.list(
        thread_id=assistant_thread.id, order="asc", after=message.id
    )

    return messages.data[0].content[0].text.value

if 'user_input' not in st.session_state:
    st.session_state.user_input = ''
if 'response' not in st.session_state:
    st.session_state.response = ''

def submit():
    st.session_state.user_input = st.session_state.query
    st.session_state.query = ''
    st.session_state.response = get_assistant_response(st.session_state.user_input)

st.text_input("O que precisa saber sobre o currículo do Ronaldo Medeiros?", key='query', on_change=submit)

user_input = st.session_state.user_input

st.write("Você digitou: ", user_input)

if user_input:
    with st.spinner('Aguarde, estou processando sua solicitação...'):
        logging.info(f'Usuário digitou: {user_input} às {current_time}')
        resposta = st.session_state.response
        st.header('Assistente Mosetech', divider='orange')
        st.markdown(resposta)
        logging.info(f'Assistente respondeu: {resposta} às {current_time}')

        botao_clicado = st.download_button(label="Download Currículo",
                                        data=PDFbyte,
                                        file_name="curriculo.pdf",
                                        mime='application/octet-stream')
        if botao_clicado:
            logging.info(f'Usuário baixou o currículo em {current_time}')