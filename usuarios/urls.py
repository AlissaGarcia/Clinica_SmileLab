from django.urls import path
from . import views

urlpatterns = [

    # ================= USUÁRIOS =================
    path('cadastrar_dentistas/', views.cadastrar_dentistas, name='cadastrar_dentistas'),
    path('cadastrar_secretarios/', views.cadastrar_secretarios, name='cadastrar_secretarios'),
    path('excluir_usuario/<int:id>/', views.excluir_usuario, name="excluir_usuario"),

    path('login/', views.login, name="login"),
    path('sair/', views.logout, name="sair"),

    # ================= DASHBOARDS =================
    path('dashboard/secretaria/', views.dashboard_secretaria, name='dashboard_secretaria'),
    path('dashboard/dentista/', views.dashboard_dentista, name='dashboard_dentista'),

    # ================= PACIENTES =================
    path('pacientes/', views.cadastrar_pacientes, name='cadastrar_pacientes'),
    path('pacientes/excluir/<int:id>/', views.excluir_paciente, name='excluir_paciente'),

    # ================= AGENDAMENTOS =================
    path('agendamentos/', views.agendamentos, name='agendamentos'),
    path('agendamentos/excluir/<int:id>/', views.excluir_agendamento, name='excluir_agendamento'),
    
    path('admin-dashboard/', views.dashboard_admin, name='dashboard_admin'),

]
