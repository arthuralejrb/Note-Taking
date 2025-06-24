"""Define o padrão de URL para appWebPython"""

from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    
    # Topicos :)
    path('topics/', views.topics, name='topics'),

    # Pagina com as entradas de um único tópico
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    
    # Pagina para o usuário criar um novo tópico
    path('new_topic/', views.new_topic, name='new_topic'),

    # Pagina para o usuário criar uma nova entrada
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    
    # Pagina pra editar uma entrada
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    

]
