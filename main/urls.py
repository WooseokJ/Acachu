from django.urls import path
from main import views
import AuthManagedPage


urlpatterns = [
    path('mypage/', views.mypage, name="mypage"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),
]
