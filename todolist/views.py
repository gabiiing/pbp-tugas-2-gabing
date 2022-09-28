from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.form import CreateTask
from todolist.models import Task

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    task_list = Task.objects.filter(user = request.user)
    context = {
        'task_list': task_list,
        'last_login': request.COOKIES['last_login']
    }
    return render(request, 'todolist.html', context)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

@login_required(login_url='/todolist/login/')
def create_task(request):
    form = CreateTask()
    if request.method == 'POST':
        form = CreateTask(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('todolist:show_todolist')
    else:
        form = CreateTask(initial={'user': request.user})
    context = {'form': form}
    return render(request, 'create_task.html', context)

@login_required(login_url='/todolist/login/')
# Fungsi untuk memperbarui status task
def update_task(request, pk):
    updated_task = Task.objects.get(id=pk)

    if updated_task.is_finished:
        updated_task.is_finished = False
    else:
        updated_task.is_finished = True
    
    updated_task.save() 
    return redirect("todolist:show_todolist")

@login_required(login_url='/todolist/login/')
# Fungsi untuk memperbarui status task
def delete_task(request, pk):
    delete_task = Task.objects.get(id=pk)
    delete_task.delete() 
    return redirect("todolist:show_todolist")

@login_required(login_url='/todolist/login/')
# Fungsi untuk memperbarui status task
def edit_task(request, pk):
    task = Task.objects.get(id=pk)
    form = CreateTask(instance=task)
    if request.method == 'POST':
        form = CreateTask(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('todolist:show_todolist')
    context = {'form': form}
    return render(request, 'create_task.html', context)
        
