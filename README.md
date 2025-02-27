# Desafio-Login

Repositório para o desafio da segunda fase do processo seletivo.

## Passo a Passo para Executar o Site

### 1. Clonar o Repositório

Primeiro, clone o repositório para o seu ambiente local:

```sh
git clone https://github.com/seu-usuario/desafio-login.git
cd desafio-login
```

### 2. Criar e Ativar o Ambiente Virtual

Crie um ambiente virtual para isolar as dependências do projeto:

```sh
python -m venv venv
```

Ative o ambiente virtual:

- No Windows:
  ```sh
  venv\Scripts\activate
  ```
- No macOS/Linux:
  ```sh
  source venv/bin/activate
  ```

### 3. Instalar as Dependências

Instale as dependências necessárias usando o `pip`:

```sh
pip install -r requirements.txt
```

### 4. Configurar o Banco de Dados

Execute as migrações para configurar o banco de dados:

```sh
python manage.py makemigrations
python manage.py migrate
```

### 5. Criar um Superusuário

Crie um superusuário para acessar o painel administrativo do Django:

```sh
python manage.py createsuperuser
```

### 6. Executar o Servidor de Desenvolvimento

Inicie o servidor de desenvolvimento do Django:

```sh
python manage.py runserver
```

### 7. Acessar o Site

Abra o navegador e acesse o site em `http://127.0.0.1:8000/`.

### 8. Acessar o Painel Administrativo

Para acessar o painel administrativo, vá para `http://127.0.0.1:8000/admin/` e faça login com as credenciais do superusuário criado anteriormente.

### 9. Desativar o Ambiente Virtual

Quando terminar de trabalhar no projeto, você pode desativar o ambiente virtual:

```sh
deactivate
```

Pronto! Agora você tem um guia passo a passo para executar o site do Desafio-Login.
