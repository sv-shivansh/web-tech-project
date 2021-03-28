from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name= 'home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^registered$', views.handleRegister, name='handleRegister'),
    url(r'^logined$', views.handleLogin, name='handleLogin'),
    url(r'^logout$', views.handleLogout, name='handleLogout'),
]
