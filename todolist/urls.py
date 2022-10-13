from django.urls import path

from todolist.views import delete, show_todolist, status, show_json, add_ajax
from todolist.views import register
from todolist.views import login_user

from todolist.views import logout_user
from todolist.views import addtodo
from todolist.views import delete
from todolist.views import status, delete_ajax

from audioop import add

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create_task/', addtodo, name='create_task'), 
    path('delete/<int:id>', delete, name='delete'),
    path('status/<int:id>', status, name='status'),

    path('deleteTask/<int:id>', delete_ajax, name='delete_ajax'),
    path('add_ajax/', add_ajax, name='add_ajax'),
    path('json/', show_json, name='show_json'),
]