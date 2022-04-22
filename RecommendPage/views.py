from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

from main.models import *


# Create your views here.
def recommendList(request):
    return render(request,'RecommendPage/recommendList.html')

def details(request):
    if request.method == 'GET':
        store_id = request.GET.get('store_id','0')
        store = Store.objects.get(store_id = store_id)
        review = Review.objects.filter(store_id = store_id)
        images = Cafepicture.objects.filter(store_id = store_id)
        return render(request,'RecommendPage/details.html',
                      {'store':store,
                      'reviews':review,
                      'images':images})
    
    else:
        form = ReplyForm(request.POST)
