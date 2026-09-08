# CodeFactory To-Do API

## Descrição do projeto
Projeto desenvolvido como parte da atividade prática das disciplinas de **DevOps e Integração Contínua** (UNINTER). Simula a adoção da Cultura DevOps pela empresa fictícia **CodeFactory Solutions**, aplicando versionamento com Git/GitHub, containerização com Docker e um pipeline de Integração Contínua.

A aplicação em si é uma **API REST de lista de tarefas (To-Do List)**, simples o suficiente para não desviar o foco do que está sendo avaliado (as práticas de DevOps), mas completa o bastante para ter testes automatizados, dependências e persistência em banco de dados.

## Objetivo
Demonstrar, na prática, como um fluxo de trabalho DevOps resolve os problemas relatados pela CodeFactory Solutions: falta de padronização, dificuldade de colaboração entre desenvolvedores, ambientes demorados para configurar e ausência de automação/testes antes da entrega.

## Tecnologias utilizadas
- **Python 3.12** + **Flask** — API REST
- **SQLite** — persistência simples dos dados
- **Pytest** — testes automatizados
- **Docker** e **Docker Compose** — containerização da aplicação
- **Git & GitHub** — versionamento e colaboração
- **GitHub Actions** — pipeline de Integração Contínua

## Estrutura de pastas
```
codefactory-todo-api/
├── app/
│   ├── __init__.py
│   └── main.py            # API Flask (rotas de tarefas)
├── tests/
│   └── test_api.py        # Testes automatizados (pytest)
├── .github/
│   └── workflows/
│       └── ci.yml         # Pipeline de Integração Contínua
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## Instruções de instalação
Pré-requisitos: Python 3.12+ ou Docker instalado.

### Rodando localmente (sem Docker)
```bash
git clone https://github.com/<seu-usuario>/codefactory-todo-api.git
cd codefactory-todo-api
pip install -r requirements.txt
```

### Rodando com Docker
```bash
git clone https://github.com/<seu-usuario>/codefactory-todo-api.git
cd codefactory-todo-api
docker compose build
```

## Instruções de execução

### Sem Docker
```bash
python -m app.main
# API disponível em http://localhost:5000
```

### Com Docker
```bash
docker compose up
# API disponível em http://localhost:5000
```

### Rodando os testes
```bash
pytest -v
```

## Endpoints da API
| Método | Rota            | Descrição                    |
|--------|-----------------|-------------------------------|
| GET    | /health         | Verifica se a API está no ar |
| GET    | /tasks          | Lista todas as tarefas       |
| POST   | /tasks          | Cria uma nova tarefa         |
| PUT    | /tasks/{id}     | Atualiza o status da tarefa  |
| DELETE | /tasks/{id}     | Remove uma tarefa            |

## Por que utilizar container neste projeto?
O container resolve diretamente um dos problemas relatados pela CodeFactory: o tempo gasto por novos colaboradores para configurar o ambiente de desenvolvimento. Com o `Dockerfile` e o `docker-compose.yml`, qualquer desenvolvedor sobe a aplicação com um único comando (`docker compose up`), sem precisar instalar Python, dependências ou configurar variáveis manualmente. Isso garante que a aplicação rode da mesma forma na máquina de qualquer integrante da equipe e também no ambiente de CI, eliminando o clássico problema de "na minha máquina funciona".

## Pipeline de Integração Contínua
O workflow em `.github/workflows/ci.yml` é executado automaticamente a cada `push` ou `pull request` para as branches `main` e `desenvolvimento`. Ele:
1. Faz o checkout do código;
2. Configura o Python;
3. Instala as dependências do `requirements.txt`;
4. Executa os testes automatizados com `pytest`;
5. Builda a imagem Docker da aplicação.

Isso garante que nenhum código quebrado ou sem testes chegue às branches principais, resolvendo o problema de aumento de erros após atualizações relatado pela empresa.

## Licença
Este projeto está sob a licença MIT — veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Versão
v1.0.0 — versão inicial do projeto.
