import streamlit as st
import logging
from datetime import datetime

st.set_page_config(
    page_title="Fake Pinterest",
    page_icon="®️",
)
fakepinterest_log = logging.getLogger("fakepinterest")
fakepinterest_log.setLevel(logging.INFO)

arquivo_log = logging.FileHandler('logs/fakepinterest.log')
arquivo_log.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
fakepinterest_log.addHandler(arquivo_log)

tempo_real = logging.StreamHandler()
tempo_real.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
fakepinterest_log.addHandler(tempo_real)
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
fakepinterest_log.info(f'Fake Pinterest acessado')

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
st.sidebar.page_link(page="pages/curriculoia.py", label="Currículo com IA")
st.sidebar.page_link(page="pages/mortystock.py", label="Mortystock")
st.sidebar.page_link(page="pages/fakepinterest.py", label="Fake Pinterest")
st.sidebar.page_link(page="pages/calculadoraprecificacao.py", label="Calculadora de Precificação")

st.sidebar.write("----------------------------------------------------------------")

st.sidebar.markdown(
    """
    ### Link do Projeto em produção + GitHub
    - Python + Flask = [Fake Pinterest](https://fakepinterest.mosetech.com.br) - [GitHub](https://github.com/ronaldmedeiiros/sitecompython)
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


