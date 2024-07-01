from django.shortcuts import render, redirect, get_object_or_404
from .models import Task #Importamos nuestro modelo para recibir las tareas
from .forms import TaskForm

def task_list_and_create(request): #La request es obligatoria, siempre la tenemos que agregar
    #haciendo la distinción entre POST y GET
    
    if request.method == "POST":
        form = TaskForm(request.POST) #Obteniendo la info
        if form.is_valid():
            form.save() #Si es correcta, la guardamos
            return redirect("crud:crud_list")
    else:
        form = TaskForm()
    
    #tasks = Task.objects.all()
    #Diferenciando entre tareas completadas y sin completar
    
    completed_tasks = Task.objects.filter(completed = True)
    uncompleted_tasks = Task.objects.filter(completed = False)
    
    return render(request, "task_list.html", { #Creando un archivo .html para mostrar las tareas
        "form": form,
        #"tasks": tasks
        "completed_tasks": completed_tasks,
        "uncompleted_tasks": uncompleted_tasks
    })
    
def update_task(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(id=task_id) #Obteniendo la tarea sobre la que el usuario quiere cambiar su estado
        task.completed = not task.completed #Haciendo el cambio (si es True, lo cambiamos a False y viceversa)
        task.save() #Guardando el cambio
        return redirect("crud:crud_list") #Redirecciona a la lista de tareas nuevamente (para que no crashee)
    

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id) #Le decimos de donde sacar la tarea y cual es su ID (si encuentra el objeto, lo guarda en la variable y si no arroja Error 404)
    initial_data = {
        "title": task.title,
        "description": task.description
    }
    if request.method == "POST":
        form =TaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
            return redirect("crud:crud_list")
    else:
        form = TaskForm(instance = task,initial=initial_data)
    return render(request, "edit_task.html", {"form": form})

#Acá estamos haciendo la distinción entre un petición GET (cuando el usuario quiere editar una tarea) y una POST (cuando ya la editó y la quiere actualizar)

def delete_task(request, task_id):
    if request.method == "POST":
        task = Task.objects.get(id=task_id)
        task.delete()
        return redirect('crud:crud_list')
    
    