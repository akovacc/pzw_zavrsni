from django.urls import path
from main.views import *
from . import views

app_name = 'portal'

urlpatterns = [
    path('', views.HomePageView.as_view(), name = 'home'),
    path('news/', views.NewsList.as_view(), name = 'news'),
    path('authors/', views.AuthorsList.as_view(), name = 'authors'),
    path('update/<int:pk>', views.AuthorsUpdateView.as_view(), name='update')
]