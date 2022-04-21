from django.urls import path
from ChoicePage import views

urlpatterns = [
    path('choice/', views.Cho, name="choice"),
    path('choice/category/', views.Cat),
    path('choice/imagesearch/', views.Img)
]
