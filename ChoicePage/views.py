from encodings import search_function
from unittest import result
from django.shortcuts import redirect, render
from RecommendPage.views import recommendList
from main.models import Searchpicture
from main.models import *
from imagemodel.image_predict import img_predict
from django.db.models import Q

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
        
        pic = Searchpicture.objects.create(searchpicture_url = img)
        tags = img_predict(pic.searchpicture_url)
        cn = {'modern':'모던빈티지', 
              'eco_friendly':'자연 친화적(natural)', 
              'vintage':'인더스트리얼 빈티지', 
              'classic':'클래식'}
        cate_names = []
        for tag in tags:
            cate_names.append(cn[tag])
        stores = Store.objects.filter(store_sinum=sido,store_sggnum=sigg,store_emdnum=emdong)\
            .prefetch_related('storetag_set')\
                .filter(Q(storetag__store__tag__tag_name = cate_names[0])|Q(storetag__store__tag__tag_name = cate_names[1]))\
                    .order_by('storetag__store__store_id').distinct()
        cate_names = ','.join(cate_names)
        print(cate_names)
        return render(request,'RecommendPage/recommendList.html',
                    {'stores':stores,
                    'size':'1',
                    'category':cate_names,
                    'sido':sido,
                    'sigg':sigg,
                    'emdong':emdong,
                    'adress':road_address})