from django.urls import path
from ImageSearchPage import views

urlpatterns = [
    path('choice/imagesearch/', views.Img)
]
