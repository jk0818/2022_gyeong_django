from lib2to3.pgen2.token import NAME
import re
from django.shortcuts import render
from .models import Shop
from .models import JejuOlle
from .models import Owner
from django.http import HttpResponse
from .models import Hospital


def shop(request):
    shop_list = Shop.objects.all()
    return render(
        request,
        'thirdapp/shop.html',
        {'shop_list': shop_list}
    )

def jeju_olle(request):
    # jeju_olle_list = JejuOlle.objects.all()
    
    time = request.GET.get("time")
    if not time: time = ''
    jeju_olle_list = JejuOlle.objects.filter(time_info__contains = time)


    return render(
        request,
        'thirdapp/jeju_olle.html',
        {'jeju_olle_list': jeju_olle_list}
    )


def owner(request):
    if request.method == 'POST':
        name = request.POST.get("name")

        owner = Owner(name=name)
        owner.save()

        return HttpResponse('주인 정보 등록 완료')
    return render(request, 'thirdapp/owner.html', {})


def jeju_olle_ajax(request):
    return render(
        request, 'thirdapp/jeju_olle_ajax.html')


def hospital(request):
    hospital_list = Hospital.objects.all()
    return render(
        request,
        'thirdapp/hospital.html',
        {'hospital_list': hospital_list}
    )


from django.http import HttpResponse
# from firstapp.models import Curriculum
from .models import Owner
from django.shortcuts import render

from django.shortcuts import redirect
from .forms import OwnerForm
def form_owner(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    c = Owner(name=name)
    c.save()

    form = OwnerForm(request.POST)
    if form.is_valid():
      # commit False 사용 시 Curriculum 모델클래스로 반환
      c = form.save(commit=False)
      c.save()      
      return redirect('/third/form/owner/')

  else:
    form = OwnerForm()

  return render(
    request, 'thirdapp/form_owner.html',
    { 'form': form }
  )


