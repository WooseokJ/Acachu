from django.urls import path
from RecommendPage import views

urlpatterns = [
    path('recommendlist/', views.recommendList),
    path('details/', views.details, name='details'),
    path('new_review/', views.new_review, name='new_review'),
]
