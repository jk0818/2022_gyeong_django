from django.http import HttpResponse
from django.shortcuts import render
from .models import Course, ArmyShop

def show(request):
    course = Course.objects.all()
    result = ''
    for c in course:
        result += c.name + '<br>'
    return render(request, 'secondapp/show.html', {'data':course})

def insert(request):
    Course(name='데이터 분석', cnt = 30).save()
    Course(name='데이터 수집', cnt = 20).save()
    Course(name='웹개발', cnt = 25).save()
    Course(name='인공지능', cnt = 20).save()
    return HttpResponse('완료')

def main(request):
    return HttpResponse("<h1><u>Main</u></h1>")

    
def army_shop(request):
    # shops = ArmyShop.objects.all()
    # print(shops)
    prd = request.GET.get('prd')
    if not prd:  #prd의 값이 업을 경우
        prd = ""
    shops = ArmyShop.objects.filter(
        name__contains=prd)

    return render(
        request, 'secondapp/army_shop.html',
        { 'data' : shops}
    )

def army_shop2(request, year, month):
    shops = ArmyShop.objects.filter(year=year, month=month)
    return render(
        request, 'secondapp/army_shop.html',
        { 'data' : shops}
    )

def course(request):
    return render(
        request, 'secondapp/course.html')
