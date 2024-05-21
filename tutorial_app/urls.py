from django.urls import path
from . import views

urlpatterns = [
    path('test', views.test, name='test'), #/test 주소 들어가면, views에 있는 test 실행
    path('upload/', views.upload_file, name='upload_file'),
]