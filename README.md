[![CircleCI](https://circleci.com/gh/NegraTec/literatura-negra.svg?style=svg)](https://circleci.com/gh/NegraTec/literatura-negra)

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

Executar os testes unitários: `docker-compose run web python -m unittest`

Testes de integração: `docker-compose run web python manage.py test`

Analises de segurança e estática:

`docker-compose run web bandit -r .`

`docker-compose run web prospector`

`docker-compose run web safety check`

## Esquema do banco de dados

https://drive.google.com/file/d/1xM9DAc6WUjQp5XyFI7opsGnNEY8t-Km8/view?usp=sharing
