from django.urls import path
from accounts.views import *
from django.contrib.auth.views import LogoutView
#agrego los paths de esta app accounts
urlpatterns = [
    path('', inicio, name='inicio'), #este seria el home de accounts..
    path('login/', login_request, name='login'),
    path('signup/', register, name='signup'), #ojo notar la vista es register, no signup. 
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('profile/', update_perfil, name='update_perfil'), #cambio el path a /profile/ xq lo pide la consigna
    path('deleteUser/<usuario>', deleteUser, name='deleteUser'),#ver si rompe con el parametro
    
]