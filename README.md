🚀 **API PYTHON - DEVOPS NA AWS**

📖 **DESCRIÇÃO**

Projeto desenvolvido para demonstrar práticas de DevOps utilizando:

◦  FastAPI
◦  Docker
◦  GitHub Actions
◦  Amazon EC2
◦  Amazon ECR

A aplicação disponibiliza endpoints para gerenciamento de tarefas e um endpoint de health check utilizado pelo pipeline e pelo deploy.

🛠️ **TECNOLOGIAS UTILIZADAS**

▪  Python 3.13
▪  FastAPI
▪  Pytest
▪  Ruff
▪  Docker
▪  Docker Compose
▪  GitHub Actions
▪  Amazon EC2
▪  Amazon ECR

⚙️ **PIPELINE CI/CD**

🔄 **INTEGRAÇÃO CONTÍNUA (CI)**

• Checkout do código

• Instalação de dependências

• Análise estática com Ruff

• Verificação de formatação

• Execução dos testes automatizados

• Geração de relatórios

🚚 **ENTREGA CONTÍNUA (CD)**

▸  Build da imagem Docker

▸  Teste do container

▸  Deploy automático para EC2

🏗️ **ARQUITETURA DA SOLUÇÃO**

GitHub ➜ GitHub Actions ➜ Testes Automatizados ➜ Build da Imagem Docker ➜ Amazon ECR ➜ Deploy na EC2 ➜ Aplicação Executando

💻 **EXECUÇÃO LOCAL**

🔹 **Criar ambiente virtual**

python -m venv .venv

🔹 **Linux/macOS**

source .venv/bin/activate

🔹 **Windows**

.venv\Scripts\Activate.ps1

🔹 **Instalar dependências**

pip install -r requirements-dev.txt

🔹 **Executar aplicação**

uvicorn app.main:app --reload


🐳 **DOCKER**

▪ **Build da imagem**

docker build -t devops-python-api .

▪ **Executar container**

docker run -p 8000:8000 devops-python-api

▪ **Docker Compose**

docker compose up --build

🌐 **ENDPOINTS**

▪ **HEALTH CHECK**

GET /health

**Resposta:**

{
  "status": "ok",
  "version": "1.0.0"
}

▪ **TAREFAS**

GET /tasks

POST /tasks

PATCH /tasks/{id}/done

☁️ **INFRAESTRUTURA AWS**

▪ Amazon EC2 para execução da aplicação

▪ Amazon ECR para armazenamento das imagens Docker

📸 **EVIDÊNCIAS**

▪ Instância EC2 em execução

▪ Repositório ECR criado

▪ Pipeline CI/CD executado com sucesso

▪ Container Docker em estado healthy

▪ Endpoint /health respondendo corretamente

👩‍💻 **AUTORA**

**HELOIZA DINIZ FIGUEREDO**


