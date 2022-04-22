from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# from django.contrib.auth.models import User # User 모델을 import한다.
# from .forms import UserCreateForm # UserCreateForm를 import한다.

from django.contrib.auth.hashers import make_password # 
from .models import User

# Create your views here.
def main(request):
    if request.method=='POST': # 요청이 POST형식이면 if문안의 내용실행
        # try: # objects.create_user 메소드에서 이미 "User"가 존재 할 경우의 예외 처리를 위한 try문
        #     #파라미터를 받아 변수담기
        # id=request.POST['User_id']
        # email=request.POSt['User_email']
        # password=request.POST['User_password']
        # re_password=request.POST['User_re_password']
        account=request.POST.get('user_account',None)
        email=request.POST.get('User_email',None)
        password=request.POST.get('User_password',None)
        re_password=request.POST.get('User_re_password',None)          
        
        res_data={} # 프론트에 던져줄 응답데이터
        if password !=re_password:
            res_data['error']="비밀번호 다름"
            return render(request,'main/mypage.html')
        else:
            
            user=User.objects.create(user_account=account,
                                user_email=email,
                                user_password=password,
                                auth_id=1)
            user.save()
            return render(request,'main/index.html')
    else:
        return render(request,'main/index.html')

            
    #         # User를 생성한다. 이때 기존에 User가 존재하는 등의 예외처리 상황이 나올 수 있음
    #         new_user = User.objects.create_user(user_id, user_email, user_password)
    #         # 생성된 유저를 DB에 저장한다.
    #         new_user.save()
    #         # 회원가입이 완료되었다면 메시지와 함께 결과 화면 페이지로 이동시킨다
    #         return render(request, 'main/index.html', {'message':'회원가입완료'})
    #     except:
    #         # 예외처리 발생 상황시 메시지와 함께 결과 화면 페이지로 이동시킨다
    #         return render(request,'main/index.html',{'message':'회원가입이미있음'})
    # else:# 요청이 POST 방식이 아닐 경우 회원가입 페이지로 이동한다.
    #     # UserCreateForm을 form 변수에 담는다
    #     form = UserCreateForm()
    # # 회원가입 페이지로 폼의 데이터와 함께 이동한다.

def mypage(request):
    return render(request,'main/mypage.html',{})



