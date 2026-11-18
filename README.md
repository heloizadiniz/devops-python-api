##API Python - CI/CD com GitHub Actions, Docker, ECR e EC2
Descrição

Projeto desenvolvido para demonstrar práticas de DevOps utilizando:

FastAPI
Docker
GitHub Actions
Amazon EC2
Amazon ECR

A aplicação disponibiliza endpoints para gerenciamento de tarefas e um endpoint de verificação de saúde utilizado pelo pipeline e pelo deploy.


##Arquitetura da Solução
Plain Text
GitHub
↓
GitHub Actions
↓
Testes Automatizados
↓
Build da Imagem Docker
↓
Amazon ECR
↓
Deploy na EC2
↓
Aplicação Executando

##Tecnologias Utilizadas
*Python 3.13
*FastAPI
*Pytest
*Ruff
*Docker
*Docker Compose
*GitHub Actions
*Amazon EC2
*Amazon ECR

##Pipeline CI/CD
O pipeline executa automaticamente:

#Integração Contínua (CI)
*Checkout do código
*Instalação de dependências
*Análise estática com Ruff
*Verificação de formatação
*Execução dos testes automatizados
*Geração de relatórios

#Entrega Contínua (CD)
*Build da imagem Docker
*Teste do container
*Deploy automático na instância EC2

#Executar Localmente
Criar ambiente virtual:

#Shell
python -m venv .venv

#Ativar:
Linux/macOS
source .venv/bin/activate

#Instalar dependências:
Shell
source .venv/bin/activate

#Windows
PowerShell
.venv\Scripts\Activate.ps1

#Instalar dependências:
Shell
pip install -r requirements-dev.txt

#Executar aplicação:
Shell
uvicorn app.main:app --reload
