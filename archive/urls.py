from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'archive'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('article/create/', views.article_create, name='article_create'),
]
