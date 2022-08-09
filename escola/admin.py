from atexit import register

from django.contrib import admin

from escola.models import Aluno


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg')
    list_display_links = ('id','nome')
    search_fields = ('nome',)

#@admin.site.register(Aluno, AlunoAdmin)
