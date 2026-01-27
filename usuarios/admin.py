from django.contrib import admin
from django.contrib.auth import admin as admin_auth_django
from .models import Users, Paciente, Agendamento
from .forms import UserChangeForm, UserCreationForm


@admin.register(Users)
class UsersAdmin(admin_auth_django.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Users
    
    fieldsets = tuple(admin_auth_django.UserAdmin.fieldsets) + (
        ('Cargo', {'fields': ('cargo',)}),
    )



@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'telefone', 'data_nascimento')
    search_fields = ('nome', 'cpf')
    list_filter = ('data_nascimento',)
    ordering = ('nome',)



@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'dentista', 'data', 'horario', 'procedimento')
    list_filter = ('data', 'dentista')
    search_fields = ('paciente__nome', 'procedimento')
    ordering = ('-data', 'horario')
