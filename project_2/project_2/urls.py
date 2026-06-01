
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('APP2/',include('APP2.urls')),
    path('',views.mainpage),

]
