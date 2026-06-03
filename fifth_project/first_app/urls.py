from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    # path('submit_form1/', views.submit_form1, name='submit_form1'),
    # path('get_about/', views.about1, name='get_about')
    path('submit_form/', views.submit_form, name='submit_form'),
    path('django_form/', views.DjangoForm, name='django_form'),
    # path('django_home/',views.StudentFrom, name='django_home')
    path('django_home/', views.PasswordValidation, name='django_home')
    ]