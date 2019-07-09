from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup, name="signup"),
    path('logout/', auth_views.LogoutView.as_view(), name="user_logout"),
    path('login/', views.user_login, name="user_login"),
    path('about/', views.about, name="about"),
    path('report/', views.feedback, name="report"),
    path('profile/', views.profile, name="profile"),
    path('reports/', views.list_reports, name="list_reports"),
]
