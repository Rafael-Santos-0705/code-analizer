# Code Analyzer

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

O projeto está organizado em uma estrutura modular e bem definida para facilitar a manutenção e a escalabilidade:
 
```plaintext
.
├── app
│   ├── adapters                 # Camada de adaptação para serviços externos
│   │   ├── dtos                 # Objetos de Transferência de Dados (DTOs)
│   │   │   ├── code.py          # DTO para análise de código
│   │   │   ├── response.py      # DTO para respostas da API
│   │   │   └── __init__.py      # Inicializador do módulo DTOs
│   │   └── api_client.py        # Cliente HTTP para APIs externas
│   ├── agents                   # Definição de agentes de IA
│   │   ├── agents.py            # Agente para melhoria de código
│   │   ├── tasks.py             # Definição de tarefas para os agentes
│   │   └── __init__.py          # Inicializador do módulo de agentes
│   ├── entities                 # Modelos de dados e provedores de entidades
│   │   ├── analysis_history.py  # Modelo para armazenar histórico de análises
│   │   ├── llm_provider.py      # Provedor de modelo de linguagem (LLM)
│   │   └── __init__.py          # Inicializador do módulo de entidades
│   ├── repositories             # Acesso a dados e persistência
│   │   ├── analysis.py          # Repositório para histórico de análises
│   │   ├── base_db.py           # Repositório base para acesso ao banco de dados
│   │   └── __init__.py          # Inicializador do módulo de repositórios
│   ├── routes                   # Definição das rotas da API
│   │   ├── code_analyzer.py     # Rotas principais para análise de código
│   │   ├── health.py            # Rota para verificação de saúde
│   │   └── __init__.py          # Inicializador do módulo de rotas
│   ├── services                 # Lógica de negócios da aplicação
│   │   ├── code_analyzer.py     # Serviço de análise de código
│   │   └── __init__.py          # Inicializador do módulo de serviços
│   └── utils                    # Ferramentas e utilitários
│       ├── checkers.py          # Validações utilitárias
│       ├── environment.py       # Gerenciamento de variáveis de ambiente
│       ├── initialize.py        # Configuração inicial do sistema
│       ├── logger.py            # Configuração de logging
│       ├── policy.py            # Gerenciamento de políticas CORS
│       └── __init__.py          # Inicializador do módulo de utilitários
├── migrations                   # Migrações do banco de dados (Alembic)
│   ├── versions                 # Arquivos de versões de migrações
│   └── env.py                   # Configuração do ambiente Alembic
├── .env                         # Arquivo de variáveis de ambiente
├── .gitignore                   # Arquivo para ignorar arquivos no Git
├── alembic.ini                  # Configuração do Alembic
├── docker-compose.yml           # Orquestração com Docker Compose
├── Dockerfile                   # Configuração da imagem Docker
├── main.py                      # Ponto de entrada da aplicação
├── README.md                    # Documentação principal do projeto
├── requirements.txt             # Dependências do Python


```
Variáveis de Ambiente
Configure sua aplicação com o arquivo .env. 

Exemplo:
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
git clone https://github.com/Rafael-Santos-0705/code-analizer
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