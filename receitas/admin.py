from django.contrib import admin
from .models import Receita


#INcluido classe ListandoReceitas para que o django admin mostrei mais informações
#serão essas:
#       'id', 'nome_receita', 'categoria', 'tempo_preparo'
class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'tempo_preparo', 'publicada') #informações de cada linha do banco
    list_display_links = ('id', 'nome_receita')# colunas clickaveis para abrir linha no cdud
    search_fields = ('nome_receita',) # adicionando campo de busca por nome da receita a "," serve para que seja um tupla
    list_filter = ('categoria',) # adicionando filto por categoria "," novamente tupla
    list_per_page = 5 #paginação do django admin
    list_editable = ('publicada',)# definindo o que pode ser editável diretamente na lista de edição, sem abrir a receitad
admin.site.register(Receita, ListandoReceitas)

# Register your models here.
