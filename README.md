"# falabella" 
Proceso de instalación del ambiente 

Ejecutar las siguientes líneas de comandos de la raíz de directorios del proyecto en un screen de ejecución Python3
1-	Instalación de las herramientas de ejecución:
pip install -r requirements.txt
2-	Dependiendo del entorno de base de datos que se quiera manejar modificar el archivo settings.py en las conexiones de base de datos al entorno deseado y crear una base de datos vacía con el nombre falabella para más información de modificación de conexiones pueden consultar la documentación https://docs.djangoproject.com/en/3.2/ref/databases/

3-	Para migrar conectar el proyecto a la base de datos ejecutar los siguientes comandos en el screen del proyecto:

Python manage.py makemigrations
Python manage.py migrate


4-	Ejecutar el siguiente comando por consola para crear super usuario y acceder a la plataforma, se solicitará un correo, un nombre de usuario, contraseña y confirmación de la misma:

Python manage.py createsuper user

5-	Una vez realizados los pasos anteriores es necesario subir el proyecto a un puerto de ejecución virtual mediante el siguiente comando (ejecutarlo en el mismo screen del proyecto)

Python manage.py runserver

6-	Como paso final acceder a su navegador web a la siguiente url donde se encontrará con un login solicitando los datos del superusuario cread anterior mente para acceder a este login ingese a http://127.0.0.1:8000/admin/ y una vez la autenticación sea efectiva podrá ver la plataforma de administración.

7- Para acceder al login de usuario y formulario de registro ingrese al siguiente link donde podrá ingresar con los usuarios creados en el sistema.
http://127.0.0.1:8000/accounts/login/

