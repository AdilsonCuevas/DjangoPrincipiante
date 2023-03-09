from django.db import models

# Create your models here.
class Projects (models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) :
        return self.name #definir nombre en el superadmin

class Task  (models.Model):
    title = models.CharField(max_length=200)
    descriptions = models.TextField() #texto medio Corto
    Project = models.ForeignKey(Projects, on_delete=models.CASCADE) #ASOCIACION CON LA TABLA PROJECTS Y CUANDO SE ELIMINE UN PROJECT DE LA ASOCIOACION SE ELIMINE EN CASCADA LAS TAREAS
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title + ' - ' + self.Project.name