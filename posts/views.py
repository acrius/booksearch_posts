from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly, ReadOnly
from .pagination import CommentPagination


class PostsViewSet(ModelViewSet):
    queryset = Post.objects.all().order_by('-publication_date')
    serializer_class = PostSerializer
    permission_classes = (ReadOnly, )


class CommentsViewSet(ModelViewSet):
    queryset = Comment.objects.all().order_by('-publication_date')
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly, )
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ('post', )
    pagination_class = CommentPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = (ReadOnly, )
