from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout', views.handleLogout, name='handleLogout'),
    path('addTodo', views.addTodo, name='addTodo'),
    path('deletecomplete', views.deletecomplete, name='deletecomplete'),
    path('deleteAll', views.deleteAll, name='deleteAll'),
    path('markasComplete', views.markasComplete, name='markasComplete'),
]
