from datetime import datetime
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import *

from main.models import *


# Create your views here.
def recommendList(request):
    return render(request,'RecommendPage/recommendList.html')

def details(request):
    if request.method == 'GET':
        store_id = request.GET.get('store_id','0')
        user_id = request.GET.get('user_id', '0')
        store = Store.objects.get(store_id = store_id)
        user = User.objects.get(user_id=user_id)
        review = Review.objects.filter(store_id = store_id)
        images = Cafepicture.objects.filter(store_id = store_id)
        formreview = ReviewForm()
        # a =  Bookmark.objects.exists(store=store, user_id=user)
        # if a:
        #     bookmark = 1
        # else:
        #     bookmark = 0
        
        return render(request,'RecommendPage/details.html',
                      {'store':store,
                      'reviews':review,
                      'images':images,
                      'formreview':formreview,
                      'bookmark':bookmark})
    
def new_review(request):
    form = ReviewForm(request.POST)
    if form.is_valid():
        content = form.cleaned_data['review_content']
        user_id = form.data['user_id']
        store_id = form.data['store_id']
        Review.objects.create(user_id = user_id, 
                                store_id = store_id, 
                                review_content = content,
                                review_reg_date = datetime.now(),
                                review_mod_date = datetime.now())

        return redirect('/details/?store_id=' + form.data['store_id'])
