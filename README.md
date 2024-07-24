# Proyecto Final Dalla Torre Emilio

*Este proyecto se continuo desde la tercera entrega. Se le agregó la aplicación usuarios, con la idea de que sean Profesores y se puedan loguear y llevar un registro de sus alumnos y las materias que cursan.
También se le agregó una aplicación de mensajería. *

*Estas funcionalides solo están disponibles cuando el usuario esta logueado. En caso de no estarlo, lo lleva a la página de Inicio de Sesión y si no tiene cuenta, a la de Registro.*
## Pasos: 

- 1 Creo la carpeta "Proyecto Final" que contendrá mi proyecto
- 2 Agrego los archivos .gitignore y README
- 3 Creo el **entorno virtual** en el que voy a trabajar->(py -m venv venv)
- 4 Inicializo Git y hago el primer commit
- 5 Conecto mi repositorio local al de GitHub y lo pusheo
- 6 Activo el entorno virtual->(. venv/Scripts/activate)
- 7 **Instalo** en mi entorno virtual **Django y Pillow**-> (pip install Django y luego lo mismo con Pillow)
- 8 Hago (pip freeze) y creo el archivo (requirements.txt)
- 9 **Creo el proyecto**-> (django-admin startpoject proyecto3ra)
- 10 **Creo las apps**-> (py manage.py startapp aplicacion, usuarios y mensajeria)
- 11 **Agrego las apps** al archivo settings.py en **INSTALLED_APPS**
- 12 Creo la carpeta (templates) a la misma altura que las apps
- 13 Agrego (BASE_DIR / 'templates') al archivo setting.py en DIRS de TEMPLATE
- 14 Crear un template en la carpeta (templates) 
- 15 Crear vistas en el archivo (views.py)
- 16 Creacion de los **modelos necesarios** dentro de cada app **(Estudiantes, Usuario y Mensaje)**
- 17 **Hacer las migraciones**-> (py manage.py makemigrations) (py manage.py migrate)
- 18 Creo los (forms.py) para crear insertar los datos en el modelo
- 19 Creo los urls necesarios en (urls.py) y nos aseguramos que funcionen
- 20 Crear super usuario. Usuario: admin - Contraseña: 1
- 21 Colecto todos los archivos estáticos para que la Web se pueda levantar sin problemas
con el comando (py manage.py collectstatic)
- 22 Hago correr la web para verificar que todo funcione correctamente con (py manage.py runserver)

Link de Drive con el video: [https://drive.google.com/file/d/1DOIU4LMHQ180IEg2YETQcIaC7bKSC-nf/view?usp=sharing]
