from django.urls import path
from .views import profile, register_game, update_game, delete_game, login, sign_up, account_create
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', login, name='login'),
    path('cadastro', register_game, name='register_game'),
    path('update/<int:id>/', update_game, name='update_game'),
    path('delete/<int:id>/', delete_game, name='delete_game'),
    path('perfil', profile, name='profile'),
    path('criarconta', sign_up, name='sign_up'),
    path('contacriada', account_create, name='account_create')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)