# Gerenciador de Tarefas

Aplicação web para gerenciamento de tarefas desenvolvida com Python e Flask.

## Funcionalidades

- Adicionar tarefas
- Editar tarefas
- Excluir tarefas
- Definir prioridade
- Concluir tarefas
- Reabrir tarefas
- Validação de dados
- Testes automatizados
- Integração contínua com GitHub Actions

## Tecnologias

- Python 3.14
- Flask
- HTML5
- CSS3
- Pytest
- Git
- GitHub Actions

## Como executar

Crie o ambiente virtual:

```powershell
python -m venv .venv

Instale as dependências:
.venv\Scripts\python.exe -m pip install flask pytest

Execute o sistema:
.venv\Scripts\python.exe src\app.pyAcesse:

http://127.0.0.1:5000

Testes

Execute:

.venv\Scripts\python.exe -m pytest

O projeto possui 7 testes automatizados.

GitHub Actions

Os testes são executados automaticamente pelo GitHub Actions sempre que alterações são enviadas para a branch main.

Estrutura
gerenciador_tarefas/
├── .github/
│   └── workflows/
│       └── tests.yml
├── src/
│   ├── app.py
│   └── templates/
│       ├── index.html
│       └── editar.html
├── tests/
│   └── test_app.py
└── README.md
Autor

Erik Costa - @eeriicdev (github)

## Mudança de escopo

Durante o desenvolvimento do projeto, foi solicitada uma mudança no escopo inicial para permitir a filtragem das tarefas por status.

A nova funcionalidade permite visualizar:

- Todas as tarefas
- Tarefas pendentes
- Tarefas concluídas

A mudança foi registrada no quadro Kanban por meio de um novo card e implementada no sistema para facilitar a organização e o acompanhamento das atividades.

A alteração foi registrada no histórico de versionamento por meio de um novo commit.