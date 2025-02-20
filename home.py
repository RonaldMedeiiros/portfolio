import streamlit as st
import webbrowser

url_linkedin = 'https://www.linkedin.com/in/ronaldo-medeiros-aa33881b9/'
url_github = 'https://github.com/ronaldmedeiiros'
url_instagram = 'https://www.instagram.com/ronaldmedeiiros/'
url_whatsapp = 'https://whatsa.me/5567981289537/?t=Ol%C3%A1,%20vim%20do%20Portf%C3%B3lio.%20Podemos%20conversar?'
email = 'ronaldmedeiiros@gmail.com'


st.set_page_config(
    page_title="Portfólio Ronaldo Medeiros",
    page_icon="®️",
)
st.sidebar.title("Página dos Projetos")
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

st.sidebar.write("----------------------------------------------------------------")
st.sidebar.markdown(
    """
    ### Link dos Projetos em produção + GitHub
    - PHP + SQlite = [Mortystock](https://mortystock.mosetech.com.br) - [GitHub](https://github.com/ronaldmedeiiros/mortystock)
    - Python + Flask = [Fake Pinterest](https://fakepinterest.mosetech.com.br) - [GitHub](https://github.com/ronaldmedeiiros/sitecompython)
    - HTML + CSS + JS = [Calculadora de Precificação](https://calculadoraprecificacao.mosetech.com.br) - [GitHub](https://github.com/ronaldmedeiiros/dashtransforma)
    """
)
st.sidebar.markdown(
     """
     ### Outros Projetos no GitHub
    - ZapDocker - Node.js + WppConnect + API Openai: [GitHub](https://github.com/ronaldmedeiiros/zapdocker)
    - Liberação de Alunos - Python + Flask (Em Construção): [GitHub](https://github.com/ronaldmedeiiros/sistemaliberacaoalunos)
    - Filmes Paradigma (Trabalho Faculdade) - HTML + JS + CSS: [GitHub](https://github.com/ronaldredeiiros/filmesparadigma)
    """
)
st.sidebar.write("----------------------------------------------------------------")

st.markdown("<h1 style='text-align: center;'>Ronaldo de Souza Medeiros</h1>", unsafe_allow_html=True)

st.write("----------------------------------------------------------------")

col1, col2 = st.columns(2)
with col1:
    st.image("https://i.ibb.co/vxkSK5yq/Ronaldo-2.png", width=300)
with col2:
    st.markdown(
        """
        <p style='text-align: justify; padding-top: 10px;'>Sou desenvolvedor fullstack com experiência e noção em Node.js, PHP, Python e TypeScript, atuando tanto no backend quanto no frontend. 
        Tenho conhecimento em bancos de dados SQL e NoSQL (MySQL, PostgreSQL, MongoDB), além de integração de APIs e automação com Inteligência Artificial. 
        Trabalho com deploy de aplicações em VPS utilizando Docker, incluindo projetos em Flask (Python) e aplicações web em HTML/CSS distribuídas via subdomínios. 
        Busco sempre aprimorar minhas habilidades e contribuir para soluções eficientes, escaláveis e acessíveis.</p>
        """
        , unsafe_allow_html=True
    )

st.write("----------------------------------------------------------------")

st.markdown("<h3 style='text-align: center; padding: 10px;'>Contatos</h3>", unsafe_allow_html=True)


st.write("----------------------------------------------------------------")



botao_linkedin, botao_github, botao_instagram, botao_whats = st.columns(4)

with botao_linkedin:
    if st.button("LinkedIn"):
        webbrowser.open_new_tab(url_linkedin)
with botao_github:
    if st.button("GitHub"):
        webbrowser.open_new_tab(url_github)
with botao_instagram:
    if st.button("Instagram"):
        webbrowser.open_new_tab(url_instagram)
with botao_whats:
    if st.button("WhatsApp"):
        webbrowser.open_new_tab(url_whatsapp)

# st.sidebar.markdown(
#     """
#     ### Contatos:
#     - [LinkedIn](https://www.linkedin.com/in/ronaldo-medeiros-aa33881b9/)
#     - [GitHub]("https://github.com/ronaldmedeiiros)
#     - [Instagram](https://www.instagram.com/ronaldmedeiiros/)
#     - [E-mail](ronaldmedeiiros@gmail.com)
#     - [WhatsApp](https://whatsa.me/5567981289537/?t=Ol%C3%A1,%20vim%20do%20Portf%C3%B3lio.%20Podemos%20conversar?)
#     """
# )












footer="""<style>
a:link , a:visited{
color: #8daec3;
text-decoration: none;
background-color: transparent;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
color: white;
text-align: center;
background-color: #101414;
}
</style>
<div class="footer">
<p><a style='display: block; text-align: center; text-decoration: none' href="https://www.linkedin.com/in/ronaldo-medeiros-aa33881b9/" target="_blank">Desenvolvido com streamlit.io por Ronaldo de Souza Medeiros</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
