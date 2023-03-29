from django.shortcuts import render
from .models import Todo

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
    return render(request, 'todos/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    priority = request.GET.get('priority')
    deadline = request.GET.get('deadline')
    todo = Todo(title=title, content=content, priority=priority, deadline=deadline)
    todo.save()
    context = {
        'title': title,
        'content': content,
        'priority': priority,
        'deadline': deadline,
    }
    return render(request, 'todos/create.html', context)

def delete(request, todo_pk):
    dlt = Todo.objects.get(pk=todo_pk)
    dlt.delete()
    return render(request, 'todos/delete.html')