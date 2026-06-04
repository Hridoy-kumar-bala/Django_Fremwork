from django import forms
from .models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel  
        # fields = '__all__'
        fields=['roll','name','father_name']
        labels ={
            'name':"enter your name",
            'roll': "enter your roll",
            'father_name': "enter your father's name"
        }
        help_texts={
            'name':"write your full name"
        }
        error_messages={
            'name': {'required':'your name is required'}
        }