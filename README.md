# Projeto de Consulta de Informações de Usuários da API do X (Twitter)

Este projeto Python demonstra como interagir com a API do X (antigo Twitter) para buscar e exibir informações de perfis de usuários. Ele utiliza a biblioteca `tweepy` para facilitar a comunicação com a API e `pandas` para organizar os dados em formato de tabela. As credenciais da API são gerenciadas de forma segura usando variáveis de ambiente com `python-dotenv`.

**Aviso Importante**: Devido às recentes mudanças e restrições nos níveis de acesso da API do X (Twitter), este projeto pode encontrar limitações significativas (como erros 403 Forbidden) com contas de desenvolvedor gratuitas/básicas. O objetivo principal aqui é demonstrar a estrutura de um projeto que consome API, a organização de código, o gerenciamento seguro de credenciais e a utilização de ferramentas essenciais para análise de dados.

## 📚 Recursos Utilizados

* **Python 3.12**: Linguagem de programação principal.
* **[Tweepy](https://www.tweepy.org/)**: Uma biblioteca Python amigável para a API do X (Twitter).
* **[Pandas](https://pandas.pydata.org/)**: Biblioteca para manipulação e análise de dados, utilizada para exibir as informações dos usuários em formato tabular (DataFrame).
* **[python-dotenv](https://pypi.org/project/python-dotenv/)**: Permite carregar variáveis de ambiente de um arquivo `.env` para manter as chaves da API seguras.
* **Git & GitHub**: Para controle de versão e hospedagem do código.

## ✨ Funcionalidades

* Autenticação segura na API do X (Twitter) usando chaves e tokens de acesso.
* Leitura de credenciais de API a partir de um arquivo `.env` (seguro para não expor no controle de versão).
* Busca de informações públicas de múltiplos usuários do X (Twitter) por meio de seus _handles_.
* Exibição das informações coletadas em um formato de tabela legível (DataFrame do Pandas).
* Tratamento básico de erros durante a autenticação e a busca de usuários.

## 🚀 Como Rodar o Projeto

Siga os passos abaixo para configurar e executar este projeto em sua máquina local.

### Pré-requisitos

Certifique-se de ter o seguinte instalado:

* **[Python 3.12](https://www.python.org/downloads/)** ou superior.
* **[Anaconda](https://www.anaconda.com/products/distribution)** ou **[Miniconda](https://docs.conda.io/en/latest/miniconda.html)** para gerenciamento de ambientes.
* Uma conta de desenvolvedor no [X Developer Platform](https://developer.x.com/) com as **chaves de API (Consumer Key, Consumer Secret, Access Token, Access Token Secret)**.

### Instalação

1.  **Clone o repositório** (se você não estiver trabalhando diretamente nele):
    ```bash
    git clone [https://github.com/ElomMaio98/X_Project.git](https://github.com/ElomMaio98/X_Project.git)
    cd X_Project
    ```
   

2.  **Crie e ative um ambiente Conda**:
    ```bash
    conda create --name twitter-api-env python=3.12
    conda activate twitter-api-env
    ```

3.  **Instale as dependências do projeto**:
    ```bash
    pip install tweepy pandas python-dotenv
    ```

### Configuração das Chaves de API (Secrets)

1.  Crie um novo arquivo chamado `.env` na **raiz do seu projeto** (na mesma pasta de `main.py`).

2.  Dentro do arquivo `.env`, adicione suas credenciais da API do X (Twitter) no seguinte formato (substitua os placeholders pelas suas chaves reais):

    ```
    CONSUMER_KEY=SUA_CONSUMER_KEY_AQUI
    CONSUMER_SECRET=SEU_CONSUMER_SECRET_AQUI
    ACCESS_TOKEN=SEU_ACCESS_TOKEN_AQUI
    ACCESS_TOKEN_SECRET=SEU_ACCESS_TOKEN_SECRET_AQUI
    ```
    **Importante**: Não use aspas nos valores e certifique-se de que não há espaços acidentais.

3.  Verifique o arquivo `.gitignore` para garantir que `.env` esteja listado, prevenindo que suas credenciais sejam enviadas para o GitHub.

### Execução

1.  Com o ambiente Conda `twitter-api-env` ativado, execute o script principal:
    ```bash
    python main.py
    ```

2.  O script tentará autenticar e, em seguida, buscará informações dos usuários definidos na lista `usuarios_para_pesquisar` dentro de `main.py`.

## ⚠️ Limitações Atuais (API do X - Twitter)

Este projeto está sujeito às seguintes limitações da API do X (Twitter) para contas gratuitas/básicas:

* **`403 Forbidden - Your credentials do not allow access to this resource`**: Contas gratuitas podem ter acesso severamente restrito a endpoints da API v1.1 e v2, incluindo a busca de informações de usuários de terceiros. A autenticação completa pode até mesmo ser bloqueada para alguns métodos.
* **Limitação de Taxa**: Mesmo se algumas requisições funcionarem, há limites estritos no número de requisições que podem ser feitas em um determinado período de tempo.

Devido a essas restrições, este projeto serve mais como um exemplo de arquitetura e boas práticas (como gerenciamento de secrets) do que um utilitário funcional para coleta extensiva de dados do X com uma conta gratuita.

## 🤝 Contribuição

Sinta-se à vontade para explorar, modificar e adaptar este código. Sugestões e melhorias são sempre bem-vindas!
