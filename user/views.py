from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def regist(request, user_id=None):
    loves = ['H5', 'Java', 'Python', 'Linux', 'Oracle', 'Cookie']
    # 获取参数名相同的多个参数值
    select_loves = request.GET.getlist('love')
    return render(request, 'regist2.html', locals())