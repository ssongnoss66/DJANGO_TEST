from django.shortcuts import render
import random

# Create your views here.
def throw(request):
    return render(request, 'apps/throw.html')

def catch(request):
    data = request.GET.get('message')
    context = {
        'data': data,
    }
    return render(request, 'apps/catch.html', context)

def lotto_create(request):
    return render(request, 'apps/lotto_create.html')

def lotto(request):
    data = int(request.GET.get('number'))
    LottorLi = []
    for i in range(data):
        LottorNum = []
        while len(LottorNum) < 6 :
            V = random.randint(1,45)
            if V not in LottorNum:
                LottorNum.append(V)
        LottorLi.append(LottorNum)
    context = {
        'data': data,
        'LottorLi': LottorLi,
    }
    return render(request, 'apps/lotto.html', context)

def detail(request, num):
    context = {
        'num': num,
    }
    return render(request, 'apps/detail.html', context)

def greeting(request, name):
    context = {
        'name': name,
    }
    return render(request, 'apps/greeting.html', context)