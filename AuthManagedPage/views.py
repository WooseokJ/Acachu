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
        page = int(request.GET.get("page",1))
        user_id = request.session['user_id']
        store_info = StoreAuth.objects.get(user_id = user_id)
        user_info=User.objects.get(user_id=user_id)
        review = Review.objects.filter(store_id = store_info.store_id).order_by('-review_reg_date')[:3]
        tags = StoreTag.objects.filter(store_id = store_info.store_id)[:20]
        boards = AuthBoard.objects.filter(user_id = user_info.user_id).order_by('-ab_reg_date') #글
        paginator = Paginator(boards,5) # 글 5개
        posts = paginator.get_page(page) # url에 있는 현재 page값 get_page로 전달

        return render(request,'AuthManagedPage\AuthManagedPage.html',
                      {'store_id':store_info.store_id,
                       'reviews':review,
                       'tags':tags,
                       'boards':boards,
                       'posts':posts
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
        return HttpResponseRedirect(reverse('board'))
    return render(request,'AuthManagedPage\post.html')

def contents(request, id): # 글 작성 후 확인
    try:
        board = AuthBoard.objects.get(pk=id)
        reply = Reply.objects.filter(authboard_id=id)
        Replyform = ReplyForm()
    except AuthBoard.DoesNotExist:
        raise Http404("Does not exist!")
    return render(request, 'AuthManagedPage\contents.html',
                    {
                        'board':board,
                        'replys':reply,
                        'replyform':Replyform
                    })

def contents_delete(request,id): #삭제
    del_post = AuthBoard.objects.get(pk=id)
    del_post.delete()
    return HttpResponseRedirect(reverse('board')) #수정

def new_reply(request,id):
    form = ReplyForm(request.POST)
    ab = AuthBoard.objects.get(pk = id)

    if form.is_valid():
        user_id = request.session['user_id']
        content = form.data['reply_content']
        AuthBoard.objects.update()
        Reply.objects.create(
                                reply_content = content,
                                reply_date = datetime.now(),
                                user_id = user_id,
                                authboard_id = id
                            )
        ab.ab_reply_yn = 1
        ab.save()
    return redirect('/post/'+str(id)) #수정