from rolepermissions.roles import AbstractUserRole

class Admin(AbstractUserRole):
    avaible_permissions = {
        'cadastrar_dentistas': True,
        'cadastrar_secretaria': True,
        'cadastrar_serviços': True,
        'cadastrar_paciente': True,
    }


class Dentista(AbstractUserRole):
    avaible_permissions = {
        'ver_agenda_individual': True,
        'confirmacao_de_consulta': True,
        'inserir_historico_paciente':True,
        'ver_historico_paciente': True,
    }

class Secretaria(AbstractUserRole):
    avaible_permissions = {
        'cadastrar_paciente':True,
        'agendar_paciente': True,
        'confirmar_pagamento':True,
    }