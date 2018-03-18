# literatura-negra

Listar autores e autoras negras, nacionais e internacionais.

Primeiro começarei coletando a informação das pessoas e seus livros em json.
Próximo passo construir website para mostrar essas informações.

Layout feito com bootstrap theme [creative](https://github.com/BlackrockDigital/startbootstrap-creative).

Imagens devem ter no maximo 350 de altura.

## Contribuindo

Faça o clone do repositório em sua máquina.

Para rodar o servidor `sh scripts/run-server.sh`

Rodar o console do django `docker-compose run web python manage.py shell`

Rodar migrate e makemigrations `docker-compose run web python manage.py migrate`

`docker-compose run web python manage.py makemigrations`

Criar usuária admin: `docker-compose run web python manage.py createsuperuser`

Executar os testes: `docker-compose run web python -m unittest`