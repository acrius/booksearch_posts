from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, UserViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
