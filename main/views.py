from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

# Create your views here.

def main(request):
    return render(request, 'main/index.html', {})

def mypage(request):
    return render(request,'main/mypage.html',{})