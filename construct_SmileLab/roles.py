from rolepermissions.roles import AbstractUserRole

class Admin(AbstractUserRole):
    available_permissions = {
        'cadastrar_dentistas': True,
        'cadastrar_dentista': True,
        'cadastrar_secretarios': True,
        'cadastrar_secretario': True,

        'dashboard_secretaria': True,
        'dashboard_dentista': True,
        'dashboard_admin': True,


        'cadastrar_pacientes': True,
        'criar_agendamentos': True,
    }


class Dentista(AbstractUserRole):
    available_permissions = {
        'dashboard_dentista': True,
        'criar_agendamentos': False,   
    }


class Secretario(AbstractUserRole):
    available_permissions = {
        'dashboard_secretaria': True,
        'cadastrar_pacientes': True,
        'criar_agendamentos': True,
    }
