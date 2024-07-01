from django import forms
from .models import Task

class TaskForm(forms.ModelForm): #Definiendo el Formulario
    class Meta:
        model = Task #Modelo a usar 
        fields = ['title', 'description'] #Campos que tiene nuestro formulario
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
        }    
    