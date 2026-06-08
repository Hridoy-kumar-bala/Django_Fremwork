from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.musician, name='add_musician'),
    path('edit/<int:id>/', views.edit, name='edit_musician'),
    path('delete/<int:id>/', views.delete, name='delete_musician'),
]