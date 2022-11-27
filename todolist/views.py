from calendar import c
from http.client import REQUEST_ENTITY_TOO_LARGE
import re
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
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import json
from django.urls import reverse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
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

@csrf_exempt
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

@csrf_exempt
def logout_user(request):
    logout(request)
    return redirect('todolist:login')

# --------------------------------------- AJAX -------------------------------------------------
# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    return render(request, 'todolist_ajax.html')

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
@csrf_exempt
def update_task(request, pk):
    updated_task = Task.objects.filter(pk=pk, user=request.user).first()
    if updated_task:
        updated_task.is_finished = not updated_task.is_finished
        updated_task.save()
    return redirect("todolist:show_todolist")

# Fungsi untuk memperbarui status task
@csrf_exempt
@login_required(login_url='/todolist/login/')
def delete_task(request, pk):
    if request.method == 'DELETE':
        delete_task = Task.objects.get(pk=pk, user=request.user)
        delete_task.delete() 
        return JsonResponse({"status": "Success delete task"},status=200)
    else:
        return JsonResponse({"status": "Failed delete task"},status=403)

@login_required(login_url='/todolist/login/')
def save_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        task = Task(title=title, description=description, user=request.user)
        task.save()
        return JsonResponse({'status': 'success'}, status=200)
    else:
        return JsonResponse({'status': 'forbidden'}, status=403)


# ---------------------------------------------------------------------------------

@login_required(login_url='/todolist/login/')
# Fungsi untuk memperbarui status task
def edit_task(request, pk):
    task = Task.objects.get(pk=pk, user=request.user)
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


@login_required(login_url='/todolist/login/')
def show_json(request):
    task_list = Task.objects.filter(user = request.user).all()
    return HttpResponse(serializers.serialize("json",task_list), content_type="application/json")

@login_required(login_url='/todolist/login/')
def show_json_by_id(request, pk):
    data = Task.objects.filter(pk=pk)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


