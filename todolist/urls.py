from django.urls import path
from todolist.views import create_task, edit_task, register, login_user, logout_user,show_todolist, update_task, delete_task
 #sesuaikan dengan nama fungsi yang dibuat

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist' ),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create'),
    path('update-task/<int:pk>/', update_task, name='update'),
    path('delete-task/<int:pk>/', delete_task, name='delete'),
    path('edit-task/<int:pk>/', edit_task, name='edit'),
    
]
