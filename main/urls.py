from django.urls import path
from main import views


urlpatterns = [
    path('mypage/', views.mypage, name="mypage"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('mypage/userprofile/', views.edit_userprofile, name="userprofile"),
    path('bookmark/', views.bookmark, name="bookmark"),
    path('review/', views.review, name="review"),
    path('email_confirm/', views.email_confirm, name="email_confirm"),
]
