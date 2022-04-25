from datetime import datetime
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import *
import json

from main.models import *


# Create your views here.
def recommendList(request):
    stores = Store.objects.all()
    return render(request,'RecommendPage/recommendList.html',
                  {'stores':stores})

def details(request):
    if request.method == 'GET':
        store_id = request.GET.get('store_id','0')
        user_id = request.GET.get('user_id', '0')
        store = Store.objects.get(store_id = store_id)
        user = User.objects.get(user_id=user_id)
        review = Review.objects.filter(store_id = store_id)
        images = Cafepicture.objects.filter(store_id = store_id)
        tags = StoreTag.objects.filter(store=store)
        bookmark = False
        if Bookmark.objects.filter(user=user, store=store).exists():
            bookmark = True
        
        formreview = ReviewForm()

        return render(request,'RecommendPage/details.html',
                      {'store':store,
                      'reviews':review,
                      'images':images,
                      'formreview':formreview,
                      'tags':tags,
                      'bookmark':bookmark})
    
def new_review(request):
    form = ReviewForm(request.POST)
    if form.is_valid():
        content = form.cleaned_data['review_content']
        user_id = form.data['user']
        store_id = form.data['store']
        user = User.objects.get(user_id = user_id)
        store = Store.objects.get(store_id = store_id)
        Review.objects.create(user = user, 
                                store = store, 
                                review_content = content,
                                review_reg_date = datetime.now(),
                                review_mod_date = datetime.now())

    return redirect('/details/?store_id=' + form.data['store'] + '&user_id=' + form.data['user'])

@csrf_exempt
def reg_bookmark(request):
    if request.method == 'POST':
        jsonObject = json.loads(request.body)
        user_id = jsonObject.get('user_id')
        store_id = jsonObject.get('store_id')
        user = User.objects.get(user_id = user_id)
        store = Store.objects.get(store_id = store_id)
        Bookmark.objects.create(user = user, store = store)
        return JsonResponse(jsonObject)

@csrf_exempt
def del_bookmark(request):
    if request.method == 'POST':
        jsonObject = json.loads(request.body)
        user_id = jsonObject.get('user_id')
        store_id = jsonObject.get('store_id')
        user = User.objects.get(user_id = user_id)
        store = Store.objects.get(store_id = store_id)
        bookmark = Bookmark.objects.filter(user=user, store=store)
        bookmark.delete()
        return JsonResponse(jsonObject)
        