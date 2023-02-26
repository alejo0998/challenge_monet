*Instalacion y ejecucion del proyecto*

1) Crear un entorno virtual
	1.1) python3 -m venv venv
	1.2) source venv/bin/activate

2) Una vez dentro del entorno virtual, ejecutar
	2.1) pip install -r requirements.txt
	(Para instalar lo necesario)

3) Finalizado esto, ejecutar.
	3.1) python manage.py migrate
	3.2) python manage.py runserver

4) Ya deberia estar corriendo el servidor en local 

5) Se agrega una collection postman, con los ejemplos de los endpoints y lo que recibe cada uno.

6) En la collection postman hay que setear 3 variables
token -> El jwt access
token_refresh -> Jwt refresh
url -> La url en donde corre el servidor, en este caso es http://localhost:8000


*ACLARACIONES MODELADO*

1) Se creo el modelo estudiante, el cual tiene una relacion uno a uno con un usuario, esto se decidio asi, debido a que en un futuro puede extenderse y podrian existir profesores, o demas, los cuales tambien serian otros tipos de usuario, por esta razon el estudiante no hereda de usuario, y tiene una foreign key hacia usuario.

2) Para crear un estudiante, primero debemos crear nuestro usuario, una vez creado dicho usuario.

3) Todos los endpoints, exceptuando el de creacion de usuario y el de obtencion del token, solicitan permiso de autenticacion, para el cual se autentican con el JWT.

4) El jwt tiene un tiempo configurable de duracion, una vez finalizado hay que refrescarlo.

5) Una vez creado el usuario, se procede a obtener el jwt con las credenciales y luego se puede crear un estudiante.

6) En esta primera version, cualquier usuario autenticado puede crear Examenes, y Preguntas, pero queda facilmente extensible para adicionar permisos, y que solo ciertos usuarios puedan crear examenes y crear preguntas.

7) Respecto al modelado de examenes y preguntas, se modelo un examen por estudiante, separado a esto se modelaron las preguntas, las cuales no tienen relacion directa con el examen, se creo una tabla intermedia para relacionar examenes con preguntas.

8) Ademas los examenes tienen una hora de inicio y una hora de fin en el modelado, y una nota final, estos 3 campos, deberian ser unicamente completados por usuarios que tengan los permisos necesarios.

9) Respecto a las respuestas de las preguntas, el usuario puede responder unicamente las preguntas que tienen su examen, no puede responder otras, y estas preguntas no tienen un endpoint con un update.

10) Se agrego redundancia en cuanto a la respuesta, ya que desde la respuesta podemos acceder al estudiante, seria respuesta->preguntaXexamen->examen->estudiante, por un tema de performance decidi agregar el campo estudiante en la respuesta.



