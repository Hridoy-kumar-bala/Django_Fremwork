from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name="homepage"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.user_login, name="login"),
    path('profile/', views.profile, name="profile"),
    path('logout/', views.user_logout, name="logout"),
    path('change_password/', views.change_password, name="change_password"),
    path('change_password2/', views.change_password_without_old, name="change_password2"),
    
]
