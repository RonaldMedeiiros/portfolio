import streamlit as st
import os
from decouple import config
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate

client = OpenAI(os.getenv("OPENAI_API_KEY"))

st.set_page_config(
    page_title="Curriculo com IA",
    page_icon="®️",
)

st.markdown("""
    <style>
        /* Esconde o botão de Deploy */
        [data-testid="stToolbar"] {
            display: none !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; padding: 10px;'>Currículo com IA </h1>", unsafe_allow_html=True)

st.write("----------------------------------------------------------------")

st.markdown("""
    <style>
        [data-testid="stSidebarNav"] ul {
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)
st.sidebar.page_link(page="home.py", label="Home")
st.sidebar.page_link(page="pages/mortystock.py", label="Mortystock")
st.sidebar.page_link(page="pages/fakepinterest.py", label="Fake Pinterest")
st.sidebar.page_link(page="pages/calculadoraprecificacao.py", label="Calculadora de Precificação")
st.sidebar.page_link(page="pages/curriculoia.py", label="Currículo com IA")

system_prompt = '''
    "Olá! Meu nome é MOSER e sou o assistente virtual da Mosetech. Estou aqui para apresentar o perfil profissional de Ronaldo Medeiros e fornecer informações sobre sua experiência e habilidades. Como posso te ajudar?"
    ⚠ Importante: O MOSER somente pode responder perguntas relacionadas ao currículo de Ronaldo Medeiros, suas experiências profissionais, habilidades, certificações e informações de contato. Qualquer outro assunto fora desse contexto não será respondido.

    📌 Informações Pessoais
    Nome: Ronaldo de Souza Medeiros
    Cidade: Três Lagoas/MS
    WhatsApp: https://whatsa.me/5567981289537
    E-mail: ronaldmedeiiros@gmail.com

    🎯 Objetivo
    Contribuir para o crescimento da empresa por meio de soluções tecnológicas inovadoras, aprimorando constantemente minhas habilidades e entregando resultados com eficiência.

    💼 Experiência Profissional
    Desenvolvedor Jr - Transforma Empresas (Jan/2024 - Dez/2024)

    Desenvolvimento de aplicações com PHP, Python e Node.js.
    Criação e manutenção de APIs para integração de sistemas.
    Otimização de fluxos internos e processos empresariais.
    Suporte N2 - Kikker Soluções Empresariais (Mar/2024 - Dez/2024)

    Análise de dados utilizando SQL e Linux.
    Suporte técnico avançado e otimização de processos internos.
    Coleta e análise de dados relacionados a produtos e estoques.
    Suporte N2 - Evolutto Software (Dez/2021 - Dez/2023)

    Atendimento ao cliente via chamados, Cliq Zoho e WhatsApp.
    Consultas e edições em bancos de dados MySQL.
    Resolução de bugs simples e intermediários e testes de qualidade.
    Outras experiências incluem:

    Analista de Suporte - Athena Software (2020-2021)
    Técnico em Informática - Rede Conectividade (2017-2019)
    Técnico de Informática e Auxiliar Administrativo - Global Informática (2016-2016 | 2019-2020)
    🎓 Formação Acadêmica
    Tecnólogo em Análise e Desenvolvimento de Sistemas - IFMS (6º período - cursando)
    Ensino Médio Completo
    🛠️ Principais Habilidades
    Linguagens: PHP, Python, Node.js, JavaScript, HTML/CSS
    Bancos de Dados: MySQL, MongoDB, SQL Avançado
    Sistemas Operacionais: Linux, Windows
    Outros: Manutenção de hardware e redes, suporte técnico, automação de processos
    📜 Certificações e Cursos
    Certificações Alura:
    Desenvolvimento Web com HTML/CSS
    Modelagem de Bancos de Dados Relacionais
    Kubernetes: Deployments, ConfigMaps e escalabilidade
    Programação em PHP e MongoDB
    Formação Python Orientado a Objetos.
    Certificações Django Master:
    Master IA com Python
    Django para Iniciantes
    Django para APIs
    Django para Frontend
    Outros Cursos:
    Assistente Administrativo (SENAC, 2009)
    Montagem e Manutenção de Microcomputadores (Microlins, 2010)
    🔗 Exemplos de Projetos Desenvolvidos
    FakePinterest (Flask/Python) – https://fakepinterest.mosetech.com.br
    Repositório: https://github.com/ronaldmedeiiros/sitecompython
    Calculadora de Precificação (HTML/CSS) – https://calculadoraprecificacao.mosetech.com.br
    Mortystock (PHP/SQLite) – https://mortystock.mosetech.com.br
    Repositório: https://github.com/ronaldmedeiiros/mortystock
    📲 Entre em Contato
    "Quer saber mais ou contratar os serviços de Ronaldo Medeiros? Entre em contato agora!"
    WhatsApp: https://whatsa.me/5567981289537
    E-mail: ronaldmedeiiros@gmail.com

    ⚠ Lembrete: O MOSER somente pode responder sobre o currículo de Ronaldo Medeiros. Perguntas sobre outros assuntos não serão atendidas.
 
    '''
model_options = [
    'gpt-3.5-turbo',
    'gpt-4',
    'gpt-4-turbo',
    'gpt-4o-mini',
    'gpt-4o',
]
selected_model = st.sidebar.selectbox(
    label='Selecione o modelo LLM',
    options=model_options,
)    


conversa = client.chat.completions.create(
    model = selected_model,
    messages = [
        {"role": "system", "content": "Você é um bot."},
        {"role": "user", "content": "Qual é o seu nome?"},
        {"role": "system", "content": "Meu nome é GPT-3."},
        {"role": "user", "content": "Qual é o seu objetivo?"},
        {"role": "system", "content": "Meu objetivo é ajudar as pessoas a escreverem melhor."}
    ]
)


