from django.urls import path
from AuthManagedPage import views

urlpatterns = [
    path('authmanaged/', views.Aut),
    path('post', views.post),
    path('contents', views.contents)
]
