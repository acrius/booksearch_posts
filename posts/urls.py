from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import PostsViewSet, CommentsViewSet, UsersViewSet

router = DefaultRouter()
router.register('posts', PostsViewSet)
router.register('comments', CommentsViewSet)
router.register('users', UsersViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
