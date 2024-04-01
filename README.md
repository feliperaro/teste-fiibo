# Teste Fiibo

## Descrição

Este projeto inclui um script que automatiza o processo de leitura de um arquivo Excel e o envio desses dados para uma API. A API é um projeto Django localizado na pasta `api`.

## Primeiros Passos

### Pré-requisitos

- Python 3.x

### Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/feliperaro/teste-fiibo.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd teste-fiibo
    ```

3. Crie um ambiente virtual (se ainda não o tiver feito):

    ```bash
    python -m venv venv
    ```

4. Ative o ambiente virtual:
    No Windows:
        ```
        venv\Scripts\activate
        ```

    No macOS e no Linux:
        ```
        source venv/bin/activate
        ```

6. Instale os requisitos:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

### Executando a API

1. Navegue até o diretório `api`:

    ```bash
    cd api
    ```

2. Aplique quaisquer migrações de banco de dados necessárias:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

3. Inicie o servidor Django:

    ```bash
    python manage.py runserver
    ```

### Executando o Script

1. Coloque seu arquivo Excel na pasta `input`.
2. Execute o script:

    ```bash
    python script.py
    ```

3. Após o processamento, o arquivo Excel será movido para a pasta `output`.
