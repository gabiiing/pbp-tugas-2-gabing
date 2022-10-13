from django.urls import path
from todolist.views import *
#sesuaikan dengan nama fungsi yang dibuat

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('json/', show_json, name='show_json'),
    path('json/<int:pk>/', show_json_by_id, name='json_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create'),
    path('add/', save_task, name='add'),
    path('update-task/<int:pk>/', update_task, name='update'),
    path('delete-task/<int:pk>/', delete_task, name='delete'),
    path('edit-task/<int:pk>/', edit_task, name='edit')
]
