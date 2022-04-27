from django.urls import path
from AuthManagedPage import views

urlpatterns = [
    path('authmanaged/', views.Aut,name='board'),
    path('post', views.post,name='post'),
    path('post/<int:id>', views.contents,name='contents'),
    path('post/<int:id>/delete', views.contents_delete,name='contents_delete')
]
