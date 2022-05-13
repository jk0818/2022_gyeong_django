from django.shortcuts import render
from .models import Shop
from .models import JejuOlle


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