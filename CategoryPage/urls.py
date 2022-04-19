from django.urls import path
from CategoryPage import views

urlpatterns = [
    path('choice/category/', views.Cat)
]
