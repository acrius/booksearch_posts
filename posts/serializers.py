from django.contrib.auth.models import User
from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Post, Comment


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'date_joined', 'url')


class PostSerializer(HyperlinkedModelSerializer):
    owner = UserSerializer()

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'publication_date',
                  'owner', 'tags', 'url')
        read_only_fields = ('id', 'publication_date')
        depth = 1


class CommentSerializer(HyperlinkedModelSerializer):
    owner = UserSerializer(required=False)

    class Meta:
        model = Comment
        fields = ('id', 'post', 'owner', 'parent',
                  'content', 'publication_date', 'url')
        read_only_fields = ('id', 'owner')
