from encodings import search_function
from unittest import result
from django.shortcuts import render

from main.models import Searchpicture

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
        img = request.FILES.get('upload_file1')
        Searchpicture.objects.create(searchpicture_url = img)
        data={
            'sido' : sido,
            'sigg': sigg,
            'emdong':emdong,
            'road_address':road_address
        }
        return render(request,'ChoicePage\ImageSearchPage.html',data)
