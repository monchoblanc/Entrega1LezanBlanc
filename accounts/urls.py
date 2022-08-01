from django.urls import path
from accounts.views import *
from django.contrib.auth.views import LogoutView
#agrego los paths de esta app accounts
urlpatterns = [
    path('', inicio, name='inicio'), #este seria el home de accounts..
    path('login/', login_request, name='login'),
    path('signup/', register, name='signup'), #ojo notar la vista es register, no signup. por si pincha.
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('profile/', editarPerfil, name='editarPerfil'),
    path('usuario/', usuario, name='usuario'),
    path('eliminarUsuario/<usuario>', eliminarUsuario, name='eliminarUsuario'),#ver si rompe con el parametro
]