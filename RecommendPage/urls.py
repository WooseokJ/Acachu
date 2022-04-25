from django.urls import path
from RecommendPage import views

urlpatterns = [
    path('recommendlist/', views.recommendList),
    path('details/', views.details, name='details'),
    path('new_review/', views.new_review, name='new_review'),
    path('reg_bookmark/', views.reg_bookmark, name='reg_bookmark'),
    path('del_bookmark/', views.del_bookmark, name='del_bookmark'),
]
