# poo-acolhe
Orientação a Objetos com Python (Projeto Acolhe)

- Descrição
  Essa plataforma é um lugar onde você pode ajudar pessoas que ficaram desabrigadas por algum motivo, ou se você precisa de
  abrigo por algum motivo, pode procurar essas pessoas/instituições que se disporam a ajudar.
  
-Execução

Para iniciar o servidor e ver a aplicação em execução, acesse a página do projeto via terminal e digite:

Comando 1: Ligar o servidor no endereço: http://192.168.0.1:8000

<strong> ~/poo-acolhe$ python manage.py runserver </strong>

Para criar um super usuário, e ser o administrador do sistema, exclua o arquivo em poo-acolhe/db.sqlite3,  digite:

Comando 2: Criando super usuário.

<strong> ~/poo-acolhe$ python manage.py createsuperuser </strong>

Entre com as informações pedidas pelo terminal, inicie a aplicação novamente (Comando 1), e acesse o perfil administrador e faça seu login pelo endereço:  http://192.168.0.1:8000/admin/
 
