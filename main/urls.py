from django.urls import path
from main import views

urlpatterns = [
    path('mypage/', views.mypage)
]
