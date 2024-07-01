from django.urls import path
from . import views

#Definiendo las URLs para la app

app_name = "crud" #Definiendo el nombre de las URLs

urlpatterns = [
    path('', views.task_list_and_create, name="crud_list"),
    path('update_task/<int:task_id>',views.update_task, name="update_task"),
    path('edit_task/<int:task_id>', views.edit_task, name="edit_task"),
    path('delete_task/<int:task_id>', views.delete_task, name ="delete_task")
]

