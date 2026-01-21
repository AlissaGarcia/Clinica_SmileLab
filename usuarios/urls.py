
from django.urls import path
from . import views
urlpatterns = [
    path('cadastrar_dentistas/', views.cadastrar_dentistas, name='cadastrar_dentistas'),
    path('login/', views.login, name="login"),
    path('sair/', views.logout, name = "sair"),
    path('excluir_usuario/<str:id>/', views.excluir_usuario, name="excluir_usuario")
]
