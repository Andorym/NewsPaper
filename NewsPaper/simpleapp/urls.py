from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    path('', PostList.as.view()),
    path('<int:pk', PostDetail.as.view()),
]