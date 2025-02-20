import streamlit as st

st.set_page_config(
    page_title="Mortystock",
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

st.markdown("<h1 style='text-align: center; padding: 10px;'>Mortystock</h1>", unsafe_allow_html=True)

st.write("----------------------------------------------------------------")

st.markdown(""" <p style='text-align: center;'><a style=text-decoration: none; href="https://mortystock.mosetech.com.br";'> https://mortystock.mosetech.com.br </a> - <a style=text-decoration: none; href="https://github.com/ronaldmedeiiros/mortystock";'> https://github.com/ronaldmedeiiros/mortystock </a>""", unsafe_allow_html=True)
st.markdown("""<img src="https://i.ibb.co/C3nXQzxb/mortystock.png" alt="mortystock" border="0">""", unsafe_allow_html=True)

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
    - PHP + SQlite = [Mortystock](https://mortystock.mosetech.com.br) - [GitHub](https://github.com/ronaldmedeiiros/mortystock)
    """
)

st.markdown("""

### Sobre
<p style='text-align: justify;'>MortyStock é um programa de gestão de estoque desenhado para facilitar o cadastro e monitoramento de produtos em diversas categorias. Com funcionalidades que permitem registrar detalhes importantes como nome do produto, setor, status, tipo de embalagem, quantidade ideal, data da última entrada, estoque atual, preço de custo, preço de venda, quantidade vendida e tipo de etiqueta, MortyStock é a ferramenta ideal para gerenciar eficientemente seu inventário. Além disso, oferece um dashboard interativo com gráficos para uma visualização rápida do estado do estoque e das vendas.</p>

#### Pré-requisitos
Para executar MortyStock, você precisará de:

* PHP (com suporte ao PDO_MySQL para integração com banco de dados)
* Servidor local ou de hospedagem que suporte PHP
* Banco de dados MySQL
* Instalar driver sqlite (linux sudo apt-get install php-sqlite3)

#### Instalação
1. Certifique-se de que o PHP e o MySQL estão instalados e configurados em seu ambiente de desenvolvimento.
2. Clone ou baixe o código-fonte do MortyStock para o seu ambiente local.
3. Configure o acesso ao banco de dados editando o arquivo de configuração do PDO_MySQL com suas credenciais de banco de dados.
4. Configurar o .env para ler o banco sem problema.
4. Rodar o comando:
```bash 
composer install
``` 
5. Inicie o servidor PHP no vscode com o comando:
```bash 
php -S localhost:3333
``` 
6. Criar um arquivo .env

7. Acesse o sistema via navegador através do endereço: http://localhost:3333

#### Funcionalidades
<p style='text-align: justify;'>Cadastro de Produtos: Permite inserir novos produtos no estoque, especificando detalhes como nome, setor, status, e outros atributos importantes.
Dashboard: Visualize gráficos e análises sobre o estoque atual, vendas, e outras métricas importantes para a gestão de inventário.</p>
""",unsafe_allow_html=True)

