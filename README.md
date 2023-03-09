# DjangoPrincipiante
programa de inicio al framework de Django

comandos: 

	maquina virtual -> 
		pip install virtualenv
		virtualenv venv
		.\venv\Scripts\activate
	instalar django -> 
		pip install django
		django-admin startproject curso .
		python manage.py runserver <3000> cancelar serve contrl+c
	Django apps -> 
		python manage.py startapp store
	
	
inclusion de rutas en diferentes aplicaciones teniendo en cuenta la principal y/o anidadas
descargar mysqlite browser portable para visualizar la base de datos por defecto
agregar las apps en settings.py installed_apps


	migraciones DB -> 
		python manage.py makemigrations <app_especifica>
		python manage.py migrate 
	interactuar con la base de datos por consola
		python manage.py shell  
		from myapps.model import Project, Task
		p = Project(name="aplicativo")
		p.save()
		Projects.objects.all() o Projects.objects.get(id=1)
		p.task_set.create(title="desarrollo app", )
	super admin -> 
		python manage.py createsuperuser 
		->adilson cuevasadilson@gmail.com  adilson1234
	templates -> render


secciones del curso 
	- instalacion de python y django.
	- crear apps dentro del mismo proyecto.
	- realizar migraciones a la base de datos y visualizarlas o incluirla en un servidor de base de datos.
	- realizar rutas url. 
	- incorporar templates y envio de varialbles al frontend (documentacion jinja https://jinja.palletsprojects.com/en/3.1.x/).
	- creacion de formularios con django y guardar en la base de datos.
	- archivos estaticos.
