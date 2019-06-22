<h1>poo-acolhe</h1> <h5>Orientação a Objetos com Python (Projeto Acolhe)</h5>

- Descrição
  Essa plataforma é um lugar onde você pode ajudar pessoas que ficaram desabrigadas por algum motivo, ou se você precisa de
  abrigo por algum motivo, tal como estar localizado em zona de risco, pode procurar essas pessoas/instituições que se disporam a ajudar.
  
 <h2>Dependencias</h2>
 <ul>
  <li> python >3</li>
  <li> django >2.1 >3</li>
  <li> crispy_forms >3</li>
 </ul>
 
-Execução

Para iniciar o servidor e ver a aplicação em execução, acesse a página do projeto via terminal e digite:

Comando 1: Ligar o servidor no endereço: http://192.168.0.1:8000

<strong> ~/poo-acolhe$ python manage.py runserver </strong>

Para criar um super usuário, e ser o administrador do sistema, exclua o arquivo em poo-acolhe/db.sqlite3,  digite:

Comando 2: Criando super usuário.

<strong> ~/poo-acolhe$ python manage.py createsuperuser </strong>

Entre com as informações pedidas pelo terminal, inicie a aplicação novamente (Comando 1), e acesse o perfil administrador e faça seu login pelo endereço:  http://192.168.0.1:8000/admin/
 
