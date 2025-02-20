import streamlit as st

st.set_page_config(
    page_title="Calculadora de Precificação",
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

st.markdown("<h1 style='text-align: center; padding: 10px;'>Calculadora de Precificação</h1>", unsafe_allow_html=True)

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

st.sidebar.write("----------------------------------------------------------------")

st.sidebar.markdown(
    """
    ### Link do Projeto em produção + GitHub
    - HTML + CSS + JS = [Calculadora de Precificação](https://calculadoraprecificacao.mosetech.com.br) - [GitHub](https://github.com/ronaldmedeiiros/dashtransforma)
    """
)

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