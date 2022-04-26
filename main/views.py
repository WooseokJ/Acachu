from asyncio.windows_events import NULL
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from argon2 import PasswordHasher
from .models import *
from .forms import *
import random
import json

def main(request):
        return render(request,'main/index.html')


def mypage(request):
    return render(request,'main/mypage.html',{})


def login(request):
    if request.method=='POST':
        user_account = request.POST.get('login_id', None)
        user_password = request.POST.get('login_pw', None)
        try:
            user = User.objects.get(user_account=user_account)
            if PasswordHasher().verify(user.user_password, user_password):
                request.session['user_id'] = user.user_id
                return redirect('mypage')
        except:
            messages.warning(request, "아이디나 비밀번호를 확인하세요")
            return redirect('main')
    messages.warning(request, "아이디나 비밀번호를 확인하세요")
    return redirect('main')
            


def logout(request):
    request.session.flush()
    return redirect('/')

def signup(request):
    if request.method=='POST': # 요청이 POST형식이면 if문안의 내용실행
        account=request.POST.get('user_account',None)
        email=request.POST.get('User_email',None)
        password=request.POST.get('User_password',None)
        re_password=request.POST.get('User_re_password',None)          
        if account !=None:
            if password !=re_password:
                return render(request, 'main/index.html')

            if password == re_password:
                adj = random.choice(Adj.objects.all())
                noun = random.choice(Noun.objects.all())
                nick = adj.first + ' ' + noun.second
                password=PasswordHasher().hash(request.POST.get('User_password',None))
                user=User.objects.create(user_account=account,
                                    user_email=email,
                                    user_password=password,
                                    auth_id=1,
                                    user_nickname=nick)
                user.save()
                return render(request,'main/index.html')
    else:
        return render(request,'main/index.html')


def mypage(request):
    user_id=request.session.get('user_id','0')
    if request.method=='POST':
        print('=========================')
        password=request.POST.get('User_password')
        try: 
            user_info=User.objects.get(user_id=user_id)
            if user_info.user_password==password:
                user_info.delete()
                request.session.flush()

        except:
            redirect('/mypage')
        return redirect('/')
    
    else:  
        user_info=User.objects.get(user_id=user_id)
        bookmark_info=Bookmark.objects.filter(user_id=user_info.user_id)
        store_info=Store.objects.all()
        print(store_info)
        review_info=Review.objects.filter(user_id=user_info.user_id).order_by('-review_mod_date')[:5]
        return render(request,'main/mypage.html',{'user_info':user_info,
                                                'bookmark_info':bookmark_info,
                                                'review_info':review_info,
                                                'store_info':store_info})


    
    
