# Use uma imagem base oficial do Python
FROM python:3.9-slim

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código da aplicação para o diretório de trabalho
COPY . .

# Exponha a porta que o Streamlit usará
EXPOSE 8501

# Comando para rodar a aplicação Streamlit
CMD ["streamlit", "run", "home.py", "--server.port=8501", "--server.address=0.0.0.0"]