from datetime import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect,Http404
from django.shortcuts import redirect, render
from main.models import *
from .forms import *
from django.core.paginator import Paginator

# Create your views here.
def Aut(request):
    if request.method == 'GET':
        store_id = request.GET.get('store_id','0')
        user_id = request.session['user_id']
        review = Review.objects.filter(store_id = store_id)
        tags = StoreTag.objects.filter(store_id = store_id)
        boards = AuthBoard.objects.filter(user_id = user_id)
        
        return render(request,'AuthManagedPage\AuthManagedPage.html',
                      {
                       'reviews':review,
                       'tags':tags,
                       'boards':boards
                       }
                    )

def post(request): #글작성
    if request.method=='POST':
        ab_title = request.POST['title']
        ab_content = request.POST['content']
        ab_reg_date = datetime.now()
        ab_reply_yn = 0
        user_id = request.session['user_id']
        AuthBoard.objects.create(ab_title=ab_title,
                                    ab_content=ab_content,
                                    ab_reg_date=ab_reg_date,
                                    ab_reply_yn = ab_reply_yn,
                                    user_id = user_id
        )
        return HttpResponseRedirect(reverse('board')) #수정
    return render(request,'AuthManagedPage\post.html')

def contents(request, id): # 글 작성 후 확인
    try:
        board = AuthBoard.objects.get(pk=id)
        reply = Reply.objects.filter(authboard_id=id)
        Replyform = ReplyForm()
    except AuthBoard.DoesNotExist:
        raise Http404("Does not exist!")
    return render(request, 'AuthManagedPage\contents.html',
                    {'board':board,
                        'replys':reply,
                        'replyform':Replyform
                    })

def contents_delete(id): #삭제
    del_post = AuthBoard.objects.get(pk=id)
    del_post.delete()
    return HttpResponseRedirect(reverse('board')) #수정

def new_reply(request):
    form = ReplyForm(request.POST)
    if form.is_valid():
        content = form.cleaned_data['reply_content']
        user_id = form.data['user']
        authboard_id = form.data['authboard']
        user = User.objects.get(user_id = user_id)
        authboard = Store.objects.get(authboard_id = authboard_id )
        Reply.objects.create(
                                reply_content = content,
                                reply_date = datetime.now(),
                                authboard = authboard,
                                user = user
                            )

    return redirect('/post' + form.data['authboard'])