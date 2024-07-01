from django.contrib import admin
from .models import Task

@admin.register(Task) #Registrando el modelo
class TaskAdmin(admin.ModelAdmin): #Define que columnas queremos mostrar
    list_display=["title", "completed"]



