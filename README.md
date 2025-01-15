# Code Analyzer: Uma Plataforma de Análise de Código Inteligente

Este repositório contém a **Plataforma de Análise de Código**, projetada para analisar trechos de código e fornecer melhorias com base nos princípios SOLID e padrões de projeto. A aplicação utiliza Python, FastAPI e a integração com CrewAI, com foco em manter a qualidade do código e ajudar desenvolvedores a aprimorar seus projetos.

## Visão Geral

O Code Analyzer oferece as seguintes funcionalidades:
- **Melhoria de Código**: Analisa trechos de código e sugere melhorias estruturais e de design com base nos princípios SOLID.
- **Relatórios Detalhados**: Gera feedback detalhado das análises realizadas.
- **API REST**: Permite interagir com a aplicação de forma prática.

## Principais Funcionalidades

- **Agente Especializado**: Um único agente, `Code Improvement Specialist`, focado em melhorias de código.
- **Foco em SOLID**: O agente sugere mudanças baseadas em princípios como Responsabilidade Única e Inversão de Dependência.
- **Padrões de Projeto**: Recomenda padrões como Factory, Singleton, Strategy e Observer, para melhorar a manutenção e extensibilidade do código.
- **Armazenamento de Histórico**: Resultados das análises são salvos no banco de dados PostgreSQL para consulta futura.

## Estrutura do Projeto

```plaintext
.
├── agents               # Define agentes de IA
│   └── agents.py        # Define o agente de melhoria de código
├── entities             # Modelos e provedores
│   ├── analysis_history.py # Modelo para armazenar histórico de análises
│   └── llm_provider.py  # Provedor do modelo de linguagem LLM
├── repositories         # Acesso ao banco de dados
│   └── analysis.py      # Repositório para histórico de análises
├── routes               # Rotas da API
│   ├── code_analyzer.py # Rota principal para análise de código
│   └── health.py        # Verificação de saúde da aplicação
├── services             # Lógica de negócios
│   └── code_analyzer.py # Serviço que gerencia a análise de código
├── utils                # Funções utilitárias
│   ├── environment.py   # Gerencia variáveis de ambiente
│   └── main.py          # Configurações e inicialização da aplicação
├── migrations           # Migrações do banco de dados (Alembic)
├── Dockerfile           # Configuração da imagem Docker
├── docker-compose.yml   # Orquestração com Docker Compose
├── requirements.txt     # Dependências Python
└── .env                 # Variáveis de ambiente

```
Variáveis de Ambiente
Configure sua aplicação com o arquivo .env. Exemplo:
```plaintext
APPLICATION_TITLE="Code Analyzer"
APPLICATION_URL="http://localhost:8000"
APPLICATION_PORT="8080"
APPLICATION_ORIGINS="*"
APPLICATION_MIGRATE="true"
DATABASE_URL=postgresql://user:password@code-analyzer-db:5432/code-analyzer?client_encoding=utf8
LOGGING_LEVEL="INFO"
OPENAI_API_KEY=" Inserir Chave "
LLM_MODEL="gpt-4"
ENVIRONMENT="development"
LANGUAGE_RESPONSE="Brazilian Portuguese"

```
## Como Executar a Aplicação
### 1. Pré-requisitos
Python 3.11 ou superior
Docker e Docker Compose
### 2. Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/code-analyzer.git
cd code-analyzer
```
### 3. Configurar e Iniciar os Serviços com Docker Compose
A maneira mais fácil de configurar e iniciar a aplicação é utilizando o docker-compose.

```bash
 docker-compose up -d --build
```
Este comando irá:

Criar e iniciar um contêiner para o Code Analyzer.
Configurar e iniciar um contêiner para o banco de dados PostgreSQL.

### 4. Verificar o Status da Aplicação


Após os contêineres serem inicializados, acesse a aplicação em http://localhost:8000.

Acesse a documentação da API no Swagger UI em http://localhost:8000/docs.

## Endpoints
### 1. Analisar Código
- Rota: POST /analyze-code/
- Descrição: Envia um trecho de código para análise e retorna sugestões de melhoria.

Exemplo de Entrada:
```json
{
  "code": "def example_function(): print('Hello World!')"
}
```
Exemplo de Saída:
```json
{
  "message": "Análise concluída com sucesso.",
  "data": "Análise do código"
}
```
### 2. Verificação de Saúde
- Rota: GET /health
- Descrição: Verifica o status da aplicação.

Exemplo de Saída:

```json
{
  "status": "ok"
}
```