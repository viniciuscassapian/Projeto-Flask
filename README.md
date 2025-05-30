# 🏫 Projeto Flask – Sistema de Gerenciamento Escolar
Este repositório representa o serviço principal do sistema de gerenciamento escolar, desenvolvido com Flask e arquitetura baseada em microsserviços. Ele é responsável por administrar alunos, professores e turmas, integrando-se com os demais microsserviços do ecossistema.

# 🧾 Descrição da API
Esta API gerencia:

Professores – cadastro, consulta, edição e exclusão

Alunos – cadastro, consulta, edição e exclusão

Turmas – criação e associação de professores e alunos às turmas

# 🔗 Principais Endpoints (Exemplos)
Método	Rota	Descrição
GET	/professores	Lista todos os professores
POST	/alunos	Cadastra um novo aluno
GET	/turmas/<id>	Consulta uma turma por ID
PUT	/turmas/<id>	Atualiza informações de uma turma
DELETE	/alunos/<id>	Remove um aluno

# 🐳 Instruções de Execução (com Docker)
Pré-requisitos
Docker instalado

Executar o sistema
bash
Copiar
Editar
# Clone o repositório
git clone https://github.com/viniciuscassapian/Projeto-Flask.git
cd Projeto-Flask

# Construa a imagem
docker build -t escola-service .

# Execute o contêiner
docker run -d -p 5000:5000 --name escola_container escola-service
A aplicação estará acessível em http://localhost:5000

# 🏛️ Arquitetura Utilizada
Este sistema segue o padrão MVC (Model-View-Controller) adaptado para APIs REST:

Model – Representação das entidades (professores, alunos, turmas)

Controller – Manipula lógica de negócio e rotas HTTP

App (app.py) – Entrada da aplicação Flask

Config (config.py) – Centraliza configurações globais

Banco de dados – Utiliza SQLite

# 🔗 Ecossistema de Microsserviços
Este sistema é o serviço orquestrador, centralizando a gestão das entidades e se comunicando com outros microsserviços:

Serviços Relacionados:
servico-atividades – Gerencia atividades dos professores

Outros microsserviços podem ser integrados para funções como reservas de salas, relatórios, etc.

Integração entre serviços
As comunicações entre serviços são feitas via HTTP REST.

Este microsserviço pode consumir ou fornecer dados para os demais por meio de requisições GET/POST.

# 🔧 Futuras Melhorias
Autenticação JWT

Substituição de SQLite por PostgreSQL

Integração com serviço de notificações por e-mail

Docker Compose para orquestração total

# 👤 Autores
Vinícius Cassapian, Beatriz Alves, Janaina Figueiredo
