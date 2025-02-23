import streamlit as st
import logging
from datetime import datetime

url_linkedin = 'https://www.linkedin.com/in/ronaldo-medeiros-aa33881b9/'
url_github = 'https://github.com/ronaldmedeiiros'
url_instagram = 'https://www.instagram.com/ronaldmedeiiros/'
url_whatsapp = 'https://whatsa.me/5567981289537/?t=Ol%C3%A1,%20vim%20do%20Portf%C3%B3lio.%20Podemos%20conversar?'
email = 'ronaldmedeiiros@gmail.com'

st.set_page_config(
    page_title="Portfólio Ronaldo Medeiros",
    page_icon="®️",
)

REMOVE_PADDING_FROM_SIDES="""
<style>
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        
    }
    stSidebar {
        padding-top: 0rem;
        padding-bottom: 0rem;
    }
</style>
"""

st.markdown(REMOVE_PADDING_FROM_SIDES, unsafe_allow_html=True)
st.sidebar.markdown(REMOVE_PADDING_FROM_SIDES, unsafe_allow_html=True)


logging.basicConfig(level=logging.INFO)
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
logging.info(f'Portfólio acessado às {current_time}')



st.markdown("""
    <style>
        /* Esconde o botão de Deploy */
        [data-testid="stToolbar"] {
            display: none !important;
        }
        .main .block-container { padding-top: 1rem; } /* Reduz espaço do topo */
        h1 { margin-top: -30px; } /* Ajusta o título */
    </style>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
    ### Projetos
    """)
st.sidebar.write("")

# CSS para esconder as páginas do menu lateral
st.markdown("""
    <style>
        [data-testid="stSidebarNav"] ul {
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.page_link(page="pages/mortystock.py", label="Mortystock")
st.sidebar.page_link(page="pages/fakepinterest.py", label="Fake Pinterest")
st.sidebar.page_link(page="pages/calculadoraprecificacao.py", label="Calculadora de Precificação")
st.sidebar.page_link(page="pages/curriculoia.py", label="Currículo com IA")

st.sidebar.write("----------------------------------------------------------------")
st.sidebar.markdown(
    """
    ### Contatos:
    - [LinkedIn](https://www.linkedin.com/in/ronaldo-medeiros-aa33881b9/)
    - [GitHub]("https://github.com/ronaldmedeiiros)
    - [Instagram](https://www.instagram.com/ronaldmedeiiros/)
    - [E-mail](ronaldmedeiiros@gmail.com)
    - [WhatsApp](https://whatsa.me/5567981289537/?t=Ol%C3%A1,%20vim%20do%20Portf%C3%B3lio.%20Podemos%20conversar?)
    """
)
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
st.sidebar.markdown(
    """
    ### Link dos Projetos diretos em produção + GitHub
    - PHP + SQlite = [Mortystock](https://mortystock.mosetech.com.br) - [GitHub](https://github.com/ronaldmedeiiros/mortystock)
    - Python + Flask = [Fake Pinterest](https://fakepinterest.mosetech.com.br) - [GitHub](https://github.com/ronaldmedeiiros/sitecompython)
    - HTML + CSS + JS = [Calculadora de Precificação](https://calculadoraprecificacao.mosetech.com.br) - [GitHub](https://github.com/ronaldmedeiiros/dashtransforma)
    """
)

st.markdown("<h1 style='text-align: center; margin-bottom: 10px;'>Portfólio Ronaldo</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; margin-top: -10px;'>Desenvolvedor Fullstack Jr</p>", unsafe_allow_html=True)
st.write("----------------------------------------------------------------")

st.markdown("<h3 style='text-align: center; padding: 10px;'>Projetos</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Aqui estão alguns dos projetos que desenvolvi:</p>", unsafe_allow_html=True)


# st.write("----------------------------------------------------------------")



curriculo_ia, mortystock, fake_pinterest, calculadora_precificacao  = st.columns(4)

with curriculo_ia:
        st.page_link(page = "pages/curriculoia.py", label = "Curriculo com IA")
with mortystock:
        st.page_link(page = "pages/mortystock.py", label = "Mortystock")
with fake_pinterest:
        st.page_link(page = "pages/fakepinterest.py", label = "Fake Pinterest")
with calculadora_precificacao:
        st.page_link(page = "pages/calculadoraprecificacao.py", label = "Calc. Precificação")

st.write("----------------------------------------------------------------")


col1, col2 = st.columns(2)
with col1:
    st.image("https://i.ibb.co/vxkSK5yq/Ronaldo-2.png", width=400)
with col2:
    st.markdown(
    """
    <div style='text-align: justify; max-width: 800px; margin: auto; font-size: 18px; margin-top: -10px;'>
        <p>Meu nome é Ronaldo de Souza Medeiros, tenho 7 anos de  experiência em suporte técnico, mas atualmente estou me dedicando ao 
        desenvolvimento de software. Estou cursando Análise e Desenvolvimento de Sistemas no Instituto Federal do Mato Grosso do Sul. Em 2024 comecei a trilhar minha experiência como desenvolvedor
        de software, atuando em projetos pessoais e profissionais, atuando como desenvolvedor fullstack jr na Transforma Empresas, tenho experiência e noção em Node.js + Typescript/VueJS, PHP + Express, Python + Django e HTML + CSS, atuando tanto no backend quanto no frontend. 
        Tenho conhecimento em bancos de dados SQL e NoSQL (MySQL, PostgreSQL, MongoDB), além de integração de APIs e automação com Inteligência Artificial. 
        Trabalho com deploy de aplicações em VPS utilizando Docker, incluindo projetos em Flask (Python) e aplicações web em HTML/CSS distribuídas via subdomínios. 
        Busco sempre aprimorar minhas habilidades e contribuir para soluções eficientes, escaláveis e acessíveis.</p>
    </div>
    """, 
    unsafe_allow_html=True
)






