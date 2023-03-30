from django.shortcuts import render, redirect
from .models import Todo
from datetime import date

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'todos/index.html', context)

def detail(request, pk):
    todo_pk = Todo.objects.get(pk=pk)
    context = {
        'todo_pk': todo_pk,
    }
    return render(request, 'todos/detail.html', context)

def new(request):
    cur_date = date.today()
    context = {
        'cur_date' : cur_date
    }
    return render(request, 'todos/new.html', context)

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    priority = request.POST.get('priority')
    deadline = request.POST.get('deadline')
    todo = Todo(title=title, content=content, priority=priority, deadline=deadline)
    todo.save()
    context = {
        'title': title,
        'content': content,
        'priority': priority,
        'deadline': deadline,
    }
    return redirect('todos:detail', todo.pk)

def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()
    return redirect('todos:index')

def edit(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    cur_date = date.today()
    context = {
        'todo': todo,
        'cur_date' : cur_date
    }
    return render(request, 'todos/edit.html', context)

def update(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.title = request.POST.get('title')
    todo.content = request.POST.get('content')
    todo.priority = request.POST.get('priority')
    todo.deadline = request.POST.get('deadline')
    todo.save()
    return redirect('todos:detail', todo.pk)

def check(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if todo.completed == True:
        todo.completed = False
    else:
        todo.completed = True
    todo.save()
    return redirect('todos:index')