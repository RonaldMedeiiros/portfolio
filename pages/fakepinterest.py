import streamlit as st

st.set_page_config(
    page_title="Fake Pinterest",
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

st.markdown("<h1 style='text-align: center; padding: 10px;'>Fake Pinterest</h1>", unsafe_allow_html=True)

st.markdown(""" <p style='text-align: center;'><a style=text-decoration: none; href="https://fakepinterest.mosetech.com.br";'> https://fakepinterest.mosetech.com.br </a> - <a style=text-decoration: none; href="https://github.com/ronaldmedeiiros/sitecompython";'> https://github.com/ronaldmedeiiros/sitecompython </a>""", unsafe_allow_html=True)
st.markdown("""<img src="https://i.ibb.co/h1C5N0TB/fakepinterest.png" alt="fakepinterest" border="0">""", unsafe_allow_html=True)


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
    - Python + Flask = [Fake Pinterest](https://fakepinterest.mosetech.com.br) - [GitHub](https://github.com/ronaldmedeiiros/sitecompython)
    """
)

st.markdown(""" 

Aplicação feita em Python, usando Flask como Framework e sqlite como banco de dados, rodando em um docker, via link http://fakepinterest.mosetech.com.br. 

Entre, crie o usuário e envie imagens em seu perfil. 

Ná página inicial, você pode ver todos as imagens enviadas, tanto por você quanto por outros usuários.

## Rodando com Docker

- Buildando a imagem

```bash
docker build -t sitecompython .
```

- Executando o Container

```bash
docker run -d -p 5010:5010 sitecompython
```

Após rodar, entrar em http://localhost:5010 

## Para rodar sem o Docker

- Iniciar o ambiente virtual do python no terminaal:

```bash
python -m venv venv
```
```bash
./venv/script/activate
```

- Após ativar, instalar os pacotes:

```bash
pip install requirementes.txt
```

- Rodando a aplicação:

```bash
python main.py
```

Aplicação feita junto com o Curso da Hashtag, porém com algumas atualizações pois os módulos estavam desatualizados.""", unsafe_allow_html=True)


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