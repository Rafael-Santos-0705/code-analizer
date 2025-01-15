# Use a imagem base do Python 3.11
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /

# Copia os arquivos do projeto para o contêiner
COPY ./app /app
COPY ./requirements.txt /app/requirements.txt

# Instala as dependências
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

# Exponha a porta usada pelo FastAPI
EXPOSE 8000

# Comando para rodar o servidor FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
