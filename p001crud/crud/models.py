from django.db import models

#Definiendo como se van a guardar los datos en la base de datos
class Task(models.Model): #El nombre de las tareas tiene que ir SIEMPRE en singular porque luego se le agrega una S
    title = models.CharField(max_length=100) #Título con no más de 100 caracteres
    description = models.TextField(blank=True) #Descripción Opcional
    completed = models.BooleanField(default=False) #Completado o no (falso por defecto)
    created = models.DateTimeField(auto_now=True) #Cuando fue creada la tarea (fecha y hora automatizado)
    
    class Meta: #Como se van a ordenar las tareas (según la fecha de creación, en este caso)
        ordering = ['-created'] 
        
    def __str__(self): #Formateando el título para que sea más legible para nosotros
        return self.title 