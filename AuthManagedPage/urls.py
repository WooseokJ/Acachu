from django.urls import path
from AuthManagedPage import views

urlpatterns = [
    path('authmanaged/', views.Aut, name='board'),
    path('managerboard/', views.managerboard, name='managerboard'),
    path('post', views.post, name='post'),
    path('post/<int:id>', views.contents, name='contents'),
    path('post/<int:id>/update',
         views.contents_update,
         name="contents_update"),
    path('post/<int:id>/delete1',
         views.contents_delete1,
         name='contents_delete1'),
    path('post/<int:id>/delete2',
         views.contents_delete2,
         name='contents_delete2'),
    path('post/new_reply/<int:id>',
         views.new_reply,
         name='new_reply'),
    path('authmanaged/storeprofile/',
         views.edit_storeprofile,
         name="storeprofile"),
]
