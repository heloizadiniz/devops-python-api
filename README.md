Perfeito! Bora deixar o README com cara de projeto final de DevOps e alinhado com o que você realmente entregou.

Você pode substituir o README atual por algo como:

API Python - CI/CD com GitHub Actions, Docker, ECR e EC2
Descrição

Projeto desenvolvido para demonstrar práticas de DevOps utilizando:

FastAPI
Docker
GitHub Actions
Amazon EC2
Amazon ECR

A aplicação disponibiliza endpoints para gerenciamento de tarefas e um endpoint de verificação de saúde utilizado pelo pipeline e pelo deploy.

Arquitetura da Solução
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

Tecnologias Utilizadas
Python 3.13
FastAPI
Pytest
Ruff
Docker
Docker Compose
GitHub Actions
Amazon EC2
Amazon ECR
Pipeline CI/CD

O pipeline executa automaticamente:

Integração Contínua (CI)
Checkout do código
Instalação de dependências
Análise estática com Ruff
Verificação de formatação
Execução dos testes automatizados
Geração de relatórios
Entrega Contínua (CD)
Build da imagem Docker
Teste do container
Deploy automático na instância EC2
Executar Localmente

Criar ambiente virtual:

python -m venv .venv


Ativar:

Linux/macOS

source .venv/bin/activate


Windows

.venv\Scripts\Activate.ps1


Instalar dependências:

pip install -r requirements-dev.txt


Executar aplicação:

uvicorn app.main:app --reload

Docker

Build da imagem:

docker build -t devops-python-api .


Executar:

docker run -p 8000:8000 devops-python-api


Ou utilizando Docker Compose:

docker compose up --build

Endpoints
Health Check
GET /health


Resposta:

{
  "status": "ok",
  "version": "1.0.0"
}

Listar Tarefas
GET /tasks

Criar Tarefa
POST /tasks

Concluir Tarefa
PATCH /tasks/{id}/done

Deploy na AWS

A aplicação é implantada em uma instância Amazon EC2 através do GitHub Actions.

Infraestrutura utilizada:

Amazon EC2
Amazon ECR
Docker
Docker Compose
Evidências
EC2

Instância executando com deploy ativo.

ECR

Repositório criado para armazenamento de imagens Docker.

Aplicação

Container executando com status:

healthy

Endpoint Health

Retorno:

{
  "status": "ok",
  "version": "1.0.0"
}

Autora

Heloiza Diniz Figueredo

Depois disso eu partiria para a próxima pendência do trabalho:

✅ Prints (feito)
 ✅ README (vamos atualizar)
 🔜 Verificar se precisa entregar Pull Request
 🔜 Verificar se precisa fazer a segunda alteração da aplicação (nova versão)

Essa segunda alteração costuma ser a última parte antes da entrega final. 🚀
