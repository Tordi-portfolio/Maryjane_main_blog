from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('base', views.base, name='base'),
    path('bio', views.bio, name='bio' )
]
