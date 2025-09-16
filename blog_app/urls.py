from django.urls import path
from . import views
urlpatterns=[
	path('',views.index,name='index'),
    path('post_detail/<int:post_id>/',views.post_detail,name='post_detail'),
    path('create/',views.create_post,name='create_post'),
    path('sign_up/',views.register,name='sign_up'),
]
