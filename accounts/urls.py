from django.urls import path
from accounts.views import *
from django.contrib.auth.views import LogoutView
#agrego los paths de esta app accounts
urlpatterns = [
    path('', inicio, name='inicio'), #este seria el home de accounts..
    path('login/', login_request, name='login'),
    path('signup/', register, name='signup'), #ojo notar la vista es register, no signup. por si pincha.
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    #path('editUser/', editUser, name='editUser'), #solo edita el de UserRegisterForm
    #path('profile/', editProfile, name='editProfile'), #las dejo igual x ahora...
    #path('registerPerfil', registerPerfil, name='registerPerfil'),
    path('update_perfil', update_perfil, name='update_perfil'),
    path('delteUser/<usuario>', deleteUser, name='deleteUser'),#ver si rompe con el parametro
]