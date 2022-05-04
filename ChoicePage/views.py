from encodings import search_function
from unittest import result
from django.shortcuts import redirect, render
from RecommendPage.views import recommendList
from main.models import Searchpicture
from main.models import *

# Create your views here.
def Cho(request):
    return render(request,'ChoicePage\ChoicePage.html')

def Cat(request):
    sido = request.POST['sido']
    sigg = request.POST['sigg']
    emdong = request.POST['emdong']
    road_address = request.POST['road_address']
    data={
        'sido' : sido,
        'sigg': sigg,
        'emdong':emdong,
        'road_address':road_address
    }
    return render(request,'ChoicePage\CategoryPage.html',data)

def Img(request):  
    if request.method == 'POST':
        sido = request.POST['sido']
        sigg = request.POST['sigg']
        emdong = request.POST['emdong']
        road_address = request.POST['road_address'] 
        data={
            'sido' : sido,
            'sigg': sigg,
            'emdong':emdong,
            'road_address':road_address
        }
        return render(request,'ChoicePage\ImageSearchPage.html',data)

def Imgadd(request):
    if request.method == 'POST':
        sido = request.POST['sido']
        sigg = request.POST['sigg']
        emdong = request.POST['emdong']
        road_address = request.POST['adress']
        img = request.FILES.get('upload_file1')
        cate_name ='유아동반'                                   # 이부분 이미지  모델과 연결해서 cate_name 받을것
        Searchpicture.objects.create(searchpicture_url = img)
    
        stores = Store.objects.filter(store_sinum=sido,store_sggnum=sigg,store_emdnum=emdong)\
                .prefetch_related('storetag_set').filter(storetag__tag__tag_name = cate_name)
        return render(request,'RecommendPage/recommendList.html',
                    {'stores':stores})