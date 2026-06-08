from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.musician, name='add_musician'),
]
