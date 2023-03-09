from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from .models import Projects, Task
from .forms import CreateNewProject

# Create your views here.
def index(request):
    return render(request, 'index.html')

def hello(request, username):
    print(username) #imprime la variable de la ruta
    return HttpResponse ("<h2> hello %s </h2>" % username)

def projects(request):
    project = list(Projects.objects.values())
    return JsonResponse(project, safe=False)

def task(request):
    #task = get_object_or_404(Task, id=id) #buscar tareas por id de lo contrario genera una pagina 404
    if request.method == 'GET':
        task = Task.objects.all()
        return render(request, 'project.html', {
            'tasks' : task,
            'form' : CreateNewProject()
        })
    else:
        Projects.objects.create(name=request.POST['name'])
        return redirect('/task/')
