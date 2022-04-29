from asyncio.windows_events import NULL
from audioop import reverse
from pickle import NONE
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from argon2 import PasswordHasher
from django.urls import reverse_lazy
from .models import *
from .forms import *
import random
import json
import time
def main(request):
    tags = Tag.objects.all()
    result = []
    for tag in tags:
        try:
            tmp = random.choice(StoreTag.objects.filter(tag=tag))
            result.append(tmp)
        except:
            continue
    # print(result, 1)
    
    user_id=request.session.get('user_id','0')
    try:
        user_info = User.objects.get(user_id=user_id)    
        request.session['auth_id'] = user_info.auth.auth_id
        return render(request,'main/index.html',{'storetags':result,'user_info':user_info})
    except:   
        return render(request,'main/index.html',{'storetags':result})

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

                return redirect('/')
        except:
            messages.warning(request,"로그인실패")
            return redirect("/")
    else:
        messages.warning(request,"로그인실패")
        return redirect('/')
            


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
                
                try:
                    user=User.objects.create(user_account=account,
                                user_email=email,
                                user_password=password,
                                auth_id=1,
                                user_nickname=nick)
                    user.save()
                    return render(request,'main/index.html')
                except:
                    messages.warning(request,'회원가입실패')
                    return redirect('/')
            
    else:
        return render(request,'main/index.html')


def mypage(request):
    user_id=request.session.get('user_id','0')
    if request.method=='POST': # 회원탈퇴
        account=request.POST.get('User_account_mod',None)
        password_mod=PasswordHasher().hash(request.POST.get('User_password_mod',"0"))
        nickname=request.POST.get('User_nickname_mod',None)
        email=request.POST.get('User_email_mod',None)
        delete=request.POST.get('delete_confirm',None)
        if delete==None and account!=None: # 회원수정
            user_info=User.objects.get(user_id=user_id) 
            try:             
                user_info.user_account=account
                user_info.user_password=password_mod
                user_info.user_nickname=nickname
                user_info.user_email=email
                user_info.save()
                redirect('/mypage')
            except:
                redirect('/mypage')
            return redirect('/mypage')
        else: #회원삭제  
            password_del=request.POST.get('User_password_del',"0")
            user_info=User.objects.get(user_id=user_id) 
            try:
                if PasswordHasher().verify(user_info.user_password, password_del):
                    if delete == '삭제':
                        user_info.delete()
                        request.session.flush()
                        return render(request,'main/index.html')# render는 template 같이 보내는것.
                    return redirect('/mypage')#redirect는 url만보는것.
            except:
                return redirect('/mypage')
    else:                                           
        user_info=User.objects.get(user_id=user_id)
        auth_id=user_info.auth_id
        if auth_id==1: #일반용
            auth_yn=False 
            bookmark_info=Bookmark.objects.filter(user_id=user_info.user_id).order_by('-bookmark_reg_date')[:5]
            store_info=Store.objects.all()
            review_info=Review.objects.filter(user_id=user_info.user_id).order_by('-review_mod_date')[:5]
            return render(request,'main/mypage.html',{'user_info':user_info,'bookmark_info':bookmark_info,
                                                    'review_info':review_info,'store_info':store_info,'auth_yn':auth_yn})
        else:           # 업주용
            auth_yn=True 
            print(auth_yn)
            bookmark_info=Bookmark.objects.filter(user_id=user_info.user_id).order_by('-bookmark_reg_date')[:1]
            store_info=Store.objects.all()
            review_info=Review.objects.filter(user_id=user_info.user_id).order_by('-review_mod_date')[:1]
            return render(request,'main/mypage.html',{'user_info':user_info,'bookmark_info':bookmark_info,
                                                    'review_info':review_info,'store_info':store_info,'auth_yn':auth_yn})


def edit_userprofile(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        img = request.FILES['upload_file1']
        user = User.objects.get(user_id = user_id)
        user.user_profileurl = img
        user.save()
        return redirect('/mypage')
    
def bookmark(request):
    user_id=request.session.get('user_id','0')
    user_info=User.objects.get(user_id=user_id)
    bookmark_info=Bookmark.objects.filter(user_id=user_info.user_id)
    store_info=Store.objects.all()
    return render(request,'main/bookmark.html',{'user_info':user_info,'bookmark_info':bookmark_info, 'store_info':store_info})
    
def review(request):
    user_id=request.session.get('user_id','0')
    user_info=User.objects.get(user_id=user_id)
    review_info=Review.objects.filter(user_id=user_info.user_id)
    return render(request,'main/review.html',{'user_info':user_info, 'review_info':review_info})