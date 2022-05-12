from django.http import HttpResponse
from django.shortcuts import render
from .models import Course

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
