from datetime import datetime
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from .forms import ReviewForm
import json

from .task import tags
from django.db.models import Q
from main.models import Store, User, Bookmark, Review, Cafepicture, StoreTag

# Create your views here.


def recommendList(request):
    if request.method == 'POST':
        cate_name = request.POST.get('category', '')
        sido = request.POST.get('sido')
        sigg = request.POST.get('sigg')
        emdong = request.POST.get('emdong')
        size = request.POST.get('size', 0)
        road_address = request.POST.get('adress')
        imgcate = ['모던', '자연 친화적(natural)', '빈티지', '클래식']
        if cate_name == '전체':
            if size == '2':
                stores = Store.objects.filter(store_sinum=sido,
                                              store_sggnum=sigg)

            elif size == '3':
                stores = Store.objects.filter(store_sinum=sido)

            else:
                size = '1'
                stores = Store.objects.filter(store_sinum=sido,
                                              store_sggnum=sigg,
                                              store_emdnum=emdong)

        elif ',' in cate_name:
            cate_names = str.split(cate_name, ',')
            if size == '2':
                stores = Store.objects.filter(
                    Q(store_sinum=sido,
                      store_sggnum=sigg,
                      tag__tag_name=cate_names[0]) |
                    Q(store_sinum=sido,
                      store_sggnum=sigg,
                      tag__tag_name=cate_names[1]))

            elif size == '3':
                stores = Store.objects.filter(
                    Q(store_sinum=sido,
                      tag__tag_name=cate_names[0]) |
                    Q(store_sinum=sido,
                      store_sggnum=sigg,
                      tag__tag_name=cate_names[1]))

            else:
                size = '1'
                stores = Store.objects.filter(
                    Q(store_sinum=sido,
                      store_sggnum=sigg,
                      store_emdnum=emdong,
                      tag__tag_name=cate_names[0]) |
                    Q(store_sinum=sido, store_sggnum=sigg,
                      tag__tag_name=cate_names[1]))
            print(cate_names[0], cate_names[1])
            cate_name = ','.join(cate_names)

        elif cate_name in imgcate:
            if size == '2':
                stores = Store.objects.filter(store_sinum=sido,
                                              store_sggnum=sigg,
                                              tag__tag_name=cate_name)
            elif size == '3':
                stores = Store.objects.filter(store_sinum=sido,
                                              tag__tag_name=cate_name)
            else:
                size = '1'
                stores = Store.objects.filter(store_sinum=sido,
                                              store_sggnum=sigg,
                                              store_emdnum=emdong,
                                              tag__tag_name=cate_name)
        else:
            if size == '2':
                stores = Store.objects\
                    .filter(store_sinum=sido,
                            store_sggnum=sigg)\
                    .prefetch_related('storetag_set')\
                    .filter(storetag__tag__tag_name=cate_name)
            elif size == '3':
                stores = Store.objects.filter(store_sinum=sido)\
                    .prefetch_related('storetag_set')\
                    .filter(storetag__tag__tag_name=cate_name)
            else:
                size = '1'
                stores = Store.objects\
                    .filter(store_sinum=sido,
                            store_sggnum=sigg,
                            store_emdnum=emdong)\
                    .prefetch_related('storetag_set')\
                    .filter(storetag__tag__tag_name=cate_name)
        print(size, cate_name)
        return render(request, 'RecommendPage/recommendList.html', {
            'stores': stores,
            'size': size,
            'category': cate_name,
            'sido': sido,
            'sigg': sigg,
            'emdong': emdong,
            'adress': road_address})


def details(request):
    if request.method == 'GET':
        store_id = request.GET.get('store_id', '0')
        page = int(request.GET.get("page", 1))
        store = Store.objects.get(store_id=store_id)
        review = Review.objects.filter(store_id=store_id)\
            .order_by('-review_id')
        paginator = Paginator(review, 7)
        page_numbers_range = 10
        max_index = paginator.num_pages
        currnet_page = int(page) if page else 1
        start_index = int((currnet_page-1) / page_numbers_range) \
            * page_numbers_range
        end_index = start_index + page_numbers_range

        if end_index >= max_index:
            end_index = max_index
        paginator_range = paginator.page_range[start_index:end_index]
        reviews = paginator.get_page(page)
        images = Cafepicture.objects.filter(store_id=store_id)
        tags = StoreTag.objects.filter(store=store)
        try:
            user_id = request.session['user_id']
            user = User.objects.get(user_id=user_id)
            bookmark = False
            if Bookmark.objects.filter(user=user, store=store).exists():
                bookmark = True
        except Exception:
            user_id = 0
            user = User.objects.filter(user_id=user_id)
            bookmark = False
        formreview = ReviewForm()
        return render(request, 'RecommendPage/details.html',
                      {'store': store,
                       'user': user,
                       'reviews': reviews,
                       'paginator_range': paginator_range,
                       'images': images,
                       'formreview': formreview,
                       'tags': tags,
                       'bookmark': bookmark})


def new_review(request):
    form = ReviewForm(request.POST)
    if form.is_valid():
        content = form.cleaned_data['review_content']
        user_id = form.data['user']
        store_id = form.data['store']
        user = User.objects.get(user_id=user_id)
        store = Store.objects.get(store_id=store_id)
        Review.objects.create(user=user,
                              store=store,
                              review_content=content,
                              review_reg_date=datetime.now(),
                              review_mod_date=datetime.now()
                              )
        reviews = Review.objects.filter(store_id=store_id)\
            .values_list('review_content', flat=True)
        lst = []
        for i in reviews:
            lst.append(i)
        reviews = json.dumps(lst)

        tags.delay(reviews, store_id)

    return redirect('/details/?store_id=' + form.data['store'])


@csrf_exempt
def reg_bookmark(request):
    if request.method == 'POST':
        jsonObject = json.loads(request.body)
        user_id = jsonObject.get('user_id')
        store_id = jsonObject.get('store_id')
        user = User.objects.get(user_id=user_id)
        store = Store.objects.get(store_id=store_id)
        Bookmark.objects.create(user=user,
                                store=store,
                                bookmark_reg_date=datetime.now()
                                )
        return JsonResponse(jsonObject)


@csrf_exempt
def del_bookmark(request):
    if request.method == 'POST':
        jsonObject = json.loads(request.body)
        user_id = jsonObject.get('user_id')
        store_id = jsonObject.get('store_id')
        user = User.objects.get(user_id=user_id)
        store = Store.objects.get(store_id=store_id)
        bookmark = Bookmark.objects.filter(user=user, store=store)
        bookmark.delete()
        return JsonResponse(jsonObject)
