from django.shortcuts import render, redirect
from .models import AccountBook
from datetime import date

# Create your views here.
def index(request):
    accountbooks = AccountBook.objects.all()
    context = {
        'accountbooks': accountbooks,
    }
    return render(request, 'accountbooks/index.html', context)

def detail(request, accountbook_pk):
    accountbook = AccountBook.objects.get(pk=accountbook_pk)
    context = {
        'accountbook': accountbook,
    }
    return render(request, 'accountbooks/detail.html', context)

def new(request):
    cur_date = date.today()
    context = {
        'cur_date': cur_date
    }
    return render(request, 'accountbooks/new.html', context)

def create(request):
    note = request.POST.get('note')
    description = request.POST.get('description')
    category = request.POST.get('category')
    amount = request.POST.get('amount')
    date = request.POST.get('date')
    accountbook = AccountBook(note=note, description=description, category=category, amount=amount, date=date)
    accountbook.save()
    context = {
        'note': note,
        'description': description,
        'category': category,
        'amount': amount,
        'date': date,
    }
    return redirect('accountbooks:detail', accountbook.pk)

def edit(request, accountbook_pk):
    accountbook = AccountBook.objects.get(pk=accountbook_pk)
    context = {
        'accountbook': accountbook,
    }
    return render(request, 'accountbooks/edit.html', context)

def update(request, accountbook_pk):
    accountbook = AccountBook.objects.get(pk=accountbook_pk)
    accountbook.note = request.POST.get('note')
    accountbook.description = request.POST.get('description')
    accountbook.category = request.POST.get('category')
    accountbook.amount = request.POST.get('amount')
    accountbook.date = request.POST.get('date')
    accountbook.save()
    return redirect('accountbooks:detail', accountbook.pk)

def delete(request, accountbook_pk):
    accountbook = AccountBook.objects.get(pk=accountbook_pk)
    accountbook.delete()
    return redirect('accountbooks:index')

def copy(request, accountbook_pk):
    accountbook = AccountBook.objects.get(pk=accountbook_pk)
    newaccntbk = AccountBook(note=accountbook.note, description=accountbook.description, category=accountbook.category, amount=accountbook.amount, date=accountbook.date)
    newaccntbk.save()
    return redirect('accountbooks:detail', newaccntbk.pk)