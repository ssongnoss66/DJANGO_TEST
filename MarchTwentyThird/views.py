from django.shortcuts import render

# Create your views here.
def inpt(request):
    return render(request, 'MarchTwentyThird/inpt.html')

def throw(request):
    return render(request, 'MarchTwentyThird/throw.html')

def catch(request):
    data = request.GET.get('message')
    context = {
        'data': data,
    }
    return render(request, 'MarchTwentyThird/catch.html', context)

def number_print(request, number):
    context = {
        'number': number,
    }
    return render(request, 'MarchTwentyThird/number_print.html', context)

def calculate(request, number1, number2):
    context = {
        'number1': number1,
        'number2': number2,
    }
    return render(request, 'MarchTwentyThird/calculate.html', context)