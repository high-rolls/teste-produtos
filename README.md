# teste-produtos
Teste de criação de um CRUD para gerenciar produtos, com nome, descrição e preço.

## Instalação
Com Git, Docker e Docker Compose instalados, execute os seguintes comandos em um shell, no diretório de sua preferência:
```
git clone https://github.com/high-rolls/teste-produtos.git
cd teste-produtos
docker-compose run web python manage.py migrate
```

## Execução
Ainda no diretório do projeto, execute `docker-compose up`, abra um navegador e acesse o caminho http://localhost:8000/products/
