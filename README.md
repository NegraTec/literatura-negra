# literatura-negra

Listar autores e autoras negras, nacionais e internacionais.

Primeiro começarei coletando a informação das pessoas e seus livros em json.
Próximo passo construir website para mostrar essas informações.

## Contribuindo

Faça o clone do repositório em sua máquina.

Na pasta do projeto rode `docker build -t literatura-negra .`

Para rodar o servidor `sh literaturanegra/scripts/run-server.sh`

Rodar o console do django `docker-compose run web python literaturanegra/manage.py shell`

Rodar migrate e makemigrations `docker-compose run web python literaturanegra/manage.py migrate`

`docker-compose run web python literaturanegra/manage.py makemigrations`
