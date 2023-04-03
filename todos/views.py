from django.shortcuts import render, redirect
from .models import Todo
from datetime import date
from .forms import TodoForm

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

def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            return redirect('todos:detail', todo.pk)
    else:
        cur_date = date.today()
        form = TodoForm()
    context = {
        'cur_date' : cur_date,
        'form' : form,
    }
    return render(request, 'todos/create.html', context)


def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()
    return redirect('todos:index')

def update(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todos:detail', todo.pk)
    else:
        form = TodoForm(instance=todo)
    context = {
        'todo': todo,
        'form': form,
    }
    return render(request, 'todos/update.html', context)

def check(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if todo.completed == True:
        todo.completed = False
    else:
        todo.completed = True
    todo.save()
    return redirect('todos:index')