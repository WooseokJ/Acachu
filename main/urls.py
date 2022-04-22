from django.urls import path
from main import views
import AuthManagedPage


urlpatterns = [
    path('mypage/', views.mypage, name="mypage"),
]
