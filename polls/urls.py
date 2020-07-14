from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),        # name 쓰는 이유 : 그 이름의 주소가 자동으로 완성됨.
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/votes/', views.votes, name='votes'),
]
