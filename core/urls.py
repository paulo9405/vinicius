from django.urls import path
from .views import (
    home,
    lista_pessoas, 
    pessoa_novo,
    editar_pessoa, 
    deletar, 
    funny
)

urlpatterns = [
    path('home', home, name='home'),
    path('pessoas', lista_pessoas, name='core_lista_pessoas'),
    path('pessoa-novo', pessoa_novo, name='core_pessoa_novo'),
    path('editar/<int:id>', editar_pessoa, name='editar_pessoa'),
    path('deletar/<int:id>', deletar, name='deleta_pessoa'),
    path('funny', funny, name='core_funny'),



]