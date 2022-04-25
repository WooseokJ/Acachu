from django.urls import path
from ChoicePage import views

urlpatterns = [
    path('choice/', views.Cho, name="choice"),
    path('choice/category/', views.Cat, name="category"),
    path('choice/imagesearch/', views.Img, name="imagesearch")
]
