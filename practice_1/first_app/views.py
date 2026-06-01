from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d={
        'name':'hridoy kumar bala',
        'age': 22,
        'hobby': 'programming',
        'skills': ['python', 'django', 'javascript'],
        'description': "I am a passionate programmer. I love to learn new technologies and work on exciting projects. I am always eager to improve my skills and contribute to the tech community. I believe in continuous learning and growth, and I am committed to becoming a better developer every day. I am excited to be a part of this journey and look forward to the opportunities that lie ahead.",
        'is_student': '2022-2026',
        'is_employed': False,
        'lst': ['python','is','best'],'birthday': datetime.datetime.now(), 'publication':'', 'course': [
        {'id': 1, 'name': 'Python', 'price': 1000},
        {'id': 2, 'name': 'Django', 'price': 2000},
        {'id': 3, 'name': 'React', 'price': 3000},],
        'value' : '123456789',
    
        }
    return render(request, 'index.html',d)
