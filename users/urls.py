from django.urls import path, include
from .views import *

app_name="users"

urlpatterns = [
    path('mypage',mypage,name='mypage'),
    
]
