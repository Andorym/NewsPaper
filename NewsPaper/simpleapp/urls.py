from django.urls import path
from .views import PostDelete, PostList, PostDetail, PostCreate, PostUpdate
from django.views.decorators.cache import cache_page

urlpatterns = [
     path('', PostList.as_view(), name='News'),
     path('<int:pk>', cache_page(60 * 10) (PostDetail.as_view()), name='post_detail'),
     path('/news/create/', PostCreate.as_view(), name='post_create'),
     path('/news/<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
     path('/news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
     path('/articles/create/', PostCreate.as_view(), name='post_create'),
     path('/articles/<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
     path('/articles/<int:pk>/delete/', PostDelete.as_view(), name='post_delete')
]
  