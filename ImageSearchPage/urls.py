from django.urls import path
from ImageSearchPage import views

urlpatterns = [
    path('ImageSearch/', views.Img)
]
