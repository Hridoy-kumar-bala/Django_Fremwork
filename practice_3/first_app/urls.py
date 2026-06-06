from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='from'),
    path('all/', views.all_data, name='all_data'),
    path('show/<int:pk>', views.show, name='show')
]