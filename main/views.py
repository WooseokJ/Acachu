from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse

from django.contrib.auth.hashers import make_password # 
from .models import *
import random
from django.contrib.auth import authenticate, login

def main(request):
    if request.method=='POST': # 요청이 POST형식이면 if문안의 내용실행

        account=request.POST.get('user_account',None)
        email=request.POST.get('User_email',None)
        password=request.POST.get('User_password',None)
        re_password=request.POST.get('User_re_password',None)          
        
        login_id=request.POST.get('login_id',None)
        login_pw=request.POST.get('login_pw',None)
        if login_id !=None:
            try:
                m = User.objects.get(user_account=login_id, user_password=login_pw)
                request.session['user_account'] = m.user_account
                re_login_id=request.session.get('login_id')
                re_login_pw=request.session.get('login_pw')
                if (login_id==re_login_id) and (login_pw==re_login_pw):
                    return render(request, 'main/mypage.html')
            except User.DoesNotExist as e:
                return render(request,  'main/index.html')
        if account !=None:
            if password !=re_password:
                return render(request, 'main/index.html')

            if password == re_password:
                adj = random.choice(Adj.objects.all())
                noun = random.choice(Noun.objects.all())
                nick = adj.first + ' ' + noun.second
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
    return render(request,'main/mypage.html',{})
