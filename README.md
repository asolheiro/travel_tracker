# [Travel Tracker](https://github.com/rmndvngrpslhr/travel_tracker)

Bem-vindo ao projeto Travel Tracker! Sou um desenvolvedor apaixonado por aprender e explorar novas tecnologias. Este projeto foi criado com o objetivo de estudar e dominar os conceitos de desenvolvimento web utilizando Flask, SQL, SQLite, HTML e CSS. Abaixo, você encontrará uma visão geral das especificações técnicas e funcionalidades implementadas.

## Sumário:
1. [Descrição do Projeto](#descrição-do-projeto)

2. [Tecnologias utilizadas](#tecnologias-utilizadas)

3. [Funcionalidades do projeto](#funcionalidades-do-projeto)

3. [Estrutura de pastas](#estrutura-de-pastas)

4. [Como executar o projeto](#como-executar-o-projeto)

5. [Como rodar os testes unitários](#como-executar-os-testes-unitários)

6. [Conclusão](#conclusão)


## Descrição do Projeto

O Travel Tracker é uma aplicação web desenvolvida para gerenciar viagens, permitindo que os usuários cadastrem, visualizem, editem e excluam informações sobre suas viagens. Este projeto foi concebido para servir como um estudo prático das seguintes tecnologias:

- **Flask:** Um microframework para Python que facilita a criação de aplicações web robustas e escaláveis.
- **Poetry**: Utilizado para gerenciamento de dependências e ambientes virtuais.
- **SQL e SQLite:** Utilizados para gerenciar e armazenar os dados de forma simples.
- **HTML e CSS:** Para construir e estilizar a interface do usuário de forma atrativa e funcional.


## Tecnologias utilizadas

- **Python**
- **Poetry**
- **Flask**
- **SQL**
- **SQLite**
- **HTML**
- **CSS**


## Funcionalidades do projeto

- **Gerenciamento de Viagens:**
  - Cadastro de novas viagens
  - Visualização de todas as viagens cadastradas
  - Edição de informações das viagens
  - Exclusão de viagens

- **Banco de Dados:**
  - Utilização de SQLite para armazenar os dados de forma persistente
  - Conexão e execução de comandos SQL para manipulação dos dados

- **Front-End:**
  - Construção de páginas web utilizando HTML para estruturação do conteúdo
  - Estilização das páginas utilizando CSS para melhorar a aparência e usabilidade


## Estrutura de pastas
- **.vscode:** Instruções para o vscode deletar automaticamente arquivos e pastas "pycache'
- **init:** Script SQL para criar as tabelas e colunas no banco de dados
- **src/:** Pasta principal do projeto
   - **core/:** Diretório contendo funcionalidades que não devem variar de versão para versão
      - **models/:** Modelos do projeto
         - **settings/:** Gerenciador de conexões com o banco de dados
         - **repositories/:** Operador de instruções no banco de dados 
   - **v1/:** Diretório das funcionalidades da versão 1
      - **controllers/:** Lógica dos processos das funcionalidades
      - **main/:** Diretório principal do servidor
         - **routes/:** Diretório que mapeia as rotas da aplicação
         - **server/:** Diretório com as Blueprints da aplicação
   - **tests/:** Diretório completo de tests, não ignorado por opção
   - **templates/:** Diretório contendo os arquivos HTML.
   - **static/css/:** Diretório contendo os arquivos CSS.
- **database.db:** Arquivo SQLite para armazenamento dos dados.
- **Makefile:** Gerenciador de tasks do projeto
- **poetry.lock** Gerenciador de dependências do Poetry
- **pyproject.toml** Gerenciador do projeto.
- **run.py:** Instruções para o servidor de desenvolvimento


## Como Executar o Projeto
### Pré-requisitos:
- [Poetry](https://python-poetry.org/)
- [Git](https://git-scm.com/)
- [GNU Make](https://www.gnu.org/software/make/)


1. **Clone o repositório:**
   ```bash
   git clone https://github.com/rmndvngrpslhr/travel_tracker
   ```

2. **Navegue até o diretório do projeto e instale as dependências:**
   ```bash
   cd travel_tracker
   make dependencies
   ```
3. **Execute a aplicação:**
   ```bash
   make dev-server
   ```

4. **Acesse a aplicação no navegador:**
   ```
   http://127.0.0.1:3000
   ```


## Como rodar os testes unitários:

1. **Pyteste configurado para rodar sob as tags `-x`, `-s`, `-vv`**
   ```bash
   make test
   ```


## Conclusão

Espero que este projeto sirva como uma base sólida para o estudo e compreensão das tecnologias envolvidas. Sinta-se à vontade para explorar, modificar e expandir o Travel Tracker conforme seu interesse e curiosidade.

Obrigado por ler e aproveitar o projeto!

> Caso precise de mais alguma informação ou ajuste, estou à disposição no e-mail: avgsolheiro@gmail.com!