from django.shortcuts import render
import random

# Create your views here.
def today_dinner(request):
    foods = ['치킨', '삼겹살', '짜장면', '비빔밥', '햄버거']
    picked = random.choice(foods)
    context = {
        'foods': foods,
        'picked': picked,
    }
    return render(request, 'articles/today_dinner.html', context)
