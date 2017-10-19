from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly, ReadOnly


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all().order_by('-publication_date')
    serializer_class = PostSerializer
    permission_classes = (ReadOnly, )


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all().order_by('-publication_date')
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = (ReadOnly, )
