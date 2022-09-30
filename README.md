# Boas-vindas ao repositório do Tech News

  Projeto feito durante o curso de desenvolvimento web na trybe.

  Esse projeto tem como objetivo fazer consultas em notícias sobre tecnologia.
  As notícias podem ser obtidas através da raspagem do [_blog da Trybe_](https://blog.betrybe.com).

## Habilidades:
-Utilizar o terminal interativo do Python
    
-Escrever seus próprios módulos e importá-los em outros códigos
    
-Aplicar técnicas de raspagem de dados
    
-Extrair dados de conteúdo HTML
    
-Armazenar os dados obtidos em um banco de dados

<details>
  <summary>
    <h3>
      Antes de começar a desenvolver
    </h3>
    </summary>

  1. Clone o repositório

  - Use o comando: `git clone git@github.com:mabiiak/tech-news.git`
  - Entre na pasta do repositório que você acabou de clonar:
    - `tech-news`

  2. Crie o ambiente virtual para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`
  
  3. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`
  
  4. Crie uma branch a partir da branch `main`

  - Verifique que você está na branch `main`
    - Exemplo: `git branch`
  - Se não estiver, mude para a branch `main`
    - Exemplo: `git checkout main`
  - Agora crie uma branch à qual você vai submeter os `commits` do seu projeto
    - Você deve criar uma branch no seguinte formato: `nome-github-nome-do-projeto`
    - Exemplo: `git checkout -b nome-tech-news`

  5. Adicione as mudanças ao _stage_ do Git e faça um `commit`

  - Verifique que as mudanças ainda não estão no _stage_
    - Exemplo: `git status` (deve aparecer listada a pasta _joaozinho_ em vermelho)
  - Adicione o novo arquivo ao _stage_ do Git
    - Exemplo:
      - `git add .` (adicionando todas as mudanças - _que estavam em vermelho_ - ao stage do Git)
      - `git status` (deve aparecer listado o arquivo _joaozinho/README.md_ em verde)
  - Faça o `commit` inicial
    - Exemplo:
      - `git commit -m 'descrição commit'` (fazendo o primeiro commit)
      - `git status` (deve aparecer uma mensagem tipo _nothing to commit_ )

  6. Adicione a sua branch com o novo `commit` ao repositório remoto

  - Usando o exemplo anterior: `git push -u origin nome-tech-news`

  7. Crie um novo `Pull Request` _(PR)_

  - Vá até a página de _Pull Requests_ do [repositório no GitHub](https://github.com/mabiiak/tech-news/pulls)
  - Clique no botão verde _"New pull request"_
  - Clique na caixa de seleção _"Compare"_ e escolha a sua branch **com atenção**
  - Coloque um título para a sua _Pull Request_
    - Exemplo: _"Cria tela de busca"_
  - Clique no botão verde _"Create pull request"_
  - Adicione uma descrição para o _Pull Request_ e clique no botão verde _"Create pull request"_
  - **Não se preocupe em preencher mais nada por enquanto!**
  - Volte até a [página de _Pull Requests_ do repositório](https://github.com/mabiiak/tech-news/pulls) e confira que o seu _Pull Request_ está criado

</details>

<details>
  <summary><strong> Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando "deactivate". Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.
</details>

<details>
  <summary><strong>🛠 Testes</strong></summary><br />

  Para executar os testes certifique-se de que você está com o ambiente virtual ativado

  <strong>Executar os testes</strong>

  ```bash
python3 -m pytest
  ```

  O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv
  ```

  Caso precise executar apenas um arquivo de testes basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py
  ```

  Caso precise executar apenas uma função de testes basta executar o comando:

  ```bash
  python3 -m pytest -k nome_da_func_de_tests
  ```

  Se desejar que os testes parem de ser executados quando acontecer o primeiro erro, use o parâmetro `-x`

  ```bash
  python3 -m pytest -x tests/nomedoarquivo.py
  ```

  Caso queria executar um teste especifico de um arquivo basta executar o comando:

  ```bash
  python3 -m pytest -x tests/nomedoarquivo.py::test_nome_do_teste
  ```

  Se quiser saber mais sobre a instalação de dependências com `pip`, veja esse [artigo](https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1).

  <strong>✍️ Teste Manual</strong>
  
  Abra um terminal Python importando as funções de interesse através do comando:

  <code>python3 -i tech_news/arquivo_de_interesse.py</code> 

</details>

<details>
  <summary><strong>Docker</strong></summary>
  Caso queria executar os seus testes de projeto via `Docker-compose`, substituindo o ambiente virtual, execute o comando:

  ```bash
  docker-compose run --rm news pytest
  ```
</details>

## Requisitos

    ✅ 1 - Crie a função `fetch`
    local: `tech_news/scraper.py`

    ✅ 2 - Crie a função `scrape_novidades`
    local: `tech_news/scraper.py`

    ✅ 3 - Crie a função `scrape_next_page_link`
    local: `tech_news/scraper.py`

    ✅ 4 - Crie a função `scrape_noticia`
    local: `tech_news/scraper.py`

    ✅ 5 - Crie a função `get_tech_news` para obter as notícias!
    local: `tech_news/scraper.py`

    ✅ 6 - Crie a função `search_by_title`
    local: `tech_news/analyzer/search_engine.py`

    ✅ 7 - Crie a função `search_by_date`
    local: `tech_news/analyzer/search_engine.py`

    ✅ 8 - Crie a função `search_by_tag`,
    local: `tech_news/analyzer/search_engine.py`

    ✅ 9 - Crie a função `search_by_category`
    local: `tech_news/analyzer/search_engine.py`

    ❌ 10 - Crie a função `top_5_news`
    local: `tech_news/analyzer/ratings.py`

    ❌ 11 - Crie a função `top_5_categories`
    local: `tech_news/analyzer/ratings.py`

# Requisitos bônus:

    ❌ 12 - Crie a função `analyzer_menu`
    local: `tech_news/menu.py`

    ❌ 13 - Implemente as funcionalidades do menu
    local: `tech_news/menu.py`
