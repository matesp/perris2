from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from . import views

# Rutas del REST
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r"users", views.PersonaViewSet)
router.register(r"rescatado", views.RescatadoViewSet)

urlpatterns = [
    path('', views.index, name="index"),
    path('Contactanos', views.contactanos, name="contactanos"),
    path('Galeria', views.galeria, name="galeria"),
    path('Galeria/Crear', views.nuevoRescate, name="nuevoRescate"),
    path('Galeria/Adoptar/<int:id>', views.adoptarRescate,name="adoptarRescate"),
    path('Galeria/Editar/', views.editarRescate,name="editarRescate"),
    path('Galeria/Borrar/<int:id>', views.borrarRescate, name="borrarRescate"),
    path('Registro', views.registro, name="registro"),
    path('Registro/Crear', views.crear, name="crear"),
    path('Login', views.login, name="login"),
    path('Login/Iniciar',views.loginIniciar,name="loginIniciar"),
    path('Logout',views.cerrarSession,name="cerrarSession"),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
    path('accounts/', include('allauth.urls')),
    path('api/', include(router.urls))
]