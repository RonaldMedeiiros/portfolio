import streamlit as st
import logging
from datetime import datetime

st.set_page_config(
    page_title="Calculadora de Precificação",
    page_icon="®️",
)

dashtransforma_log = logging.getLogger("calculadoraprecificacao")
dashtransforma_log.setLevel(logging.INFO)

arquivo_log = logging.FileHandler('logs/calculadoraprecificacao.log')
arquivo_log.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
dashtransforma_log.addHandler(arquivo_log)

tempo_real = logging.StreamHandler()
tempo_real.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
dashtransforma_log.addHandler(tempo_real)
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
dashtransforma_log.info(f'Calculadora de Precificação acessada')

st.markdown("""
    <style>
        /* Esconde o botão de Deploy */
        [data-testid="stToolbar"] {
            display: none !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; padding: 10px;'>Calculadora de Precificação</h1>", unsafe_allow_html=True)

st.markdown(""" <p style='text-align: center;'><a style=text-decoration: none; href="https://calculadoraprecificacao.mosetech.com.br";'> https://calculadoraprecificacao.mosetech.com.br </a> - <a style=text-decoration: none; href="https://github.com/ronaldmedeiiros/dashtransforma";'> https://github.com/ronaldmedeiiros/dashtransforma </a>""", unsafe_allow_html=True)
st.markdown("""<img src="https://i.ibb.co/spMg2dZr/dashtransforma.png" alt="calculadoraprecificacao" border="0">""", unsafe_allow_html=True)

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
    - HTML + CSS + JS = [Calculadora de Precificação](https://calculadoraprecificacao.mosetech.com.br) - [GitHub](https://github.com/ronaldmedeiiros/dashtransforma)
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
    ## 📖 Sobre o Projeto

    <p style='text-align: justify;'>O **Dashboard Transforma** é uma aplicação web desenvolvida para auxiliar empresários e gestores na precificação de produtos e serviços. Através de uma interface amigável e cálculos automáticos, o sistema permite identificar o preço ideal de venda, analisando custos fixos, variáveis e margem de lucro, além de calcular o ponto de equilíbrio e exibir gráficos detalhados sobre a composição do preço.</p>

    ## 🚀 Funcionalidades

    A Calculadora de Precificação oferece as seguintes funcionalidades:

    - **Entrada de Dados Financeiros**:
    - Inserção de informações como custos de aquisição, custos variáveis, despesas fixas, receita mensal e margem de lucro desejada.
    - **Cálculo Automático**:
    - Preço de venda ideal, considerando todos os custos e margem de lucro.
    - Ponto de equilíbrio, indicando o volume mínimo de vendas necessário para cobrir os custos.
    - **Visualização Gráfica e Analítica**:
    - Gráficos interativos que mostram a distribuição de custos e margens.
    - Tabelas detalhadas com valores absolutos e percentuais.
    - **Simulação de Cenários**:
    - Comparação entre cenários fixos e variáveis.
    - Ajuste dinâmico de valores para avaliar diferentes estratégias de precificação.

    ## 📋 Como Usar

    ### Etapas para Utilizar a Calculadora:
    1. Acesse a página da calculadora através do menu lateral.
    2. Insira os dados financeiros do seu negócio:
    - **Custo de aquisição** (Ex.: R$ 100,00).
    - **Custos variáveis** (Ex.: 15%).
    - **Despesas fixas mensais** (Ex.: R$ 8.000,00).
    - **Receita mensal** (Ex.: R$ 25.000,00).
    - **Margem de lucro desejada** (Ex.: 25%).
    3. Clique no botão **"CALCULAR"** para obter os resultados.
    4. Analise os resultados:
    - Gráficos e tabelas que detalham o preço de venda ideal e o ponto de equilíbrio.

    ### Exemplo de Resultados:
    - **Preço de Venda Ideal**: R$ 200,00.
    - **Ponto de Equilíbrio Real**: R$ 10.000,00.
    - **Ponto de Equilíbrio por Unidade**: 50 unidades.

    ## 🛠️ Tecnologias Utilizadas

    Este projeto foi construído utilizando as seguintes tecnologias:

    - **HTML5** e **CSS3**: Estruturação e estilização da aplicação.
    - **JavaScript**: Implementação das lógicas de cálculo e manipulação dos dados.
    - **Chart.js**: Criação de gráficos interativos.
    - **Font Awesome**: Ícones para melhoria da interface.
    - **Google Charts**: Visualização adicional de gráficos.


    ## 📈 Funcionalidades da Calculadora (arquivo `formulas.js`)

    As principais funções do código incluem:

    - **Cálculo do Preço de Venda**:
    Determina o preço ideal com base nos custos fixos, variáveis e margem de lucro.
    - **Cálculo do Ponto de Equilíbrio**:
    Identifica o valor ou quantidade mínima de vendas necessárias para cobrir os custos.
    - **Atualização Dinâmica**:
    Exibe os resultados em tabelas e gráficos de forma interativa.
    - **Simulação de Cenários**:
    Avalia os impactos financeiros de diferentes estratégias de venda.

    ## 📊 Benefícios

    - **Decisões Informadas**: Ajudar empresários a tomar decisões baseadas em dados financeiros precisos.
    - **Interface Intuitiva**: Simplicidade no uso, ideal para usuários não técnicos.
    - **Visualização de Dados**: Gráficos detalhados para uma análise clara e objetiva.

    ## 🔗 Links Úteis

    - [Documentação do Chart.js](https://www.chartjs.org/)
    - [Font Awesome](https://fontawesome.com/)
    - [Google Charts](https://developers.google.com/chart) """,unsafe_allow_html=True)

# footer="""<style>
# a:link , a:visited{
# color: #8daec3;
# text-decoration: none;
# background-color: transparent;
# }

# a:hover,  a:active {
# color: red;
# background-color: transparent;
# text-decoration: underline;
# }

# .footer {
# position: fixed;
# left: 0;
# bottom: 0;
# width: 100%;
# color: white;
# text-align: center;
# background-color: #101414;
# }
# </style>
# <div class="footer">
# <p><a style='display: block; text-align: center; text-decoration: none' href="https://www.linkedin.com/in/ronaldo-medeiros-aa33881b9/" target="_blank">Desenvolvido com streamlit.io por Ronaldo de Souza Medeiros</a></p>
# </div>
# """
# st.markdown(footer,unsafe_allow_html=True)