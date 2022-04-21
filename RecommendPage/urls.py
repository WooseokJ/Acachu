from django.urls import path
from RecommendPage import views

urlpatterns = [
    path('recommendlist/', views.recommendList),
    path('details/', views.details),
]
