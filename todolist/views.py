from django.shortcuts import render

import datetime
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    todolistObjects = Task.objects.filter(user=request.user)
    context = {
        'list_todo': todolistObjects,
        'last_login': request.COOKIES['last_login']
    }
    return render(request, "todolist.html", context)

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
        # Login first, then response & data login terakhir dimasukkan ke cookie dan ditambahkan ke response
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def addtodo(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = datetime.datetime.now()
        is_finished = False
        Task.objects.create(title=title, description=description, date=date, user=request.user, is_finished=is_finished)
        response = HttpResponseRedirect(reverse('todolist:show_todolist'))
        return response
    return render(request, "addtodo.html")

# Do reverse for urls py

def delete(request, id):
    data = Task.objects.filter(user=request.user).get(pk =id)
    data.delete()
    return redirect('todolist:show_todolist')

def status(request, id):
    data_status = Task.objects.filter(user=request.user).get(pk=id)
    if data_status.is_finished == False :
        data_status.is_finished = True
        data_status.save()
    else:
        data_status.is_finished = False
        data_status.save()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def show_json(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

def add_ajax(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    add_todolist = Task(
        user = request.user,
        title = title,
        description = description,
    )
    add_todolist.save()
    return JsonResponse({"task": "new todolist"},status=200)

@csrf_exempt
def delete_ajax(request,id):
    data = Task.objects.filter(pk=id)   
    data.delete()
    return JsonResponse({"data": "removed todolist"},status=200)