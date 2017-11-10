from collections import Iterable
from django.contrib.auth.models import User
from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.fields import empty
from taggit_serializer.serializers import TaggitSerializer, TagListSerializerField

from .models import Post, Comment


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'date_joined', 'url')


class PostSerializer(HyperlinkedModelSerializer, TaggitSerializer):
    owner = UserSerializer()
    tags = TagListSerializerField()

    class Meta:
        model = Post
        _common_fields = ('id', 'title', 'publication_date',
                         'owner', 'tags', 'url')
        _retrieve_fields = ('content', )
        _list_fields = ('preview', )
        fields = _common_fields + _retrieve_fields + _list_fields
        read_only_fields = ('id', 'publication_date')
        depth = 1

    def __init__(self, instance=None, data=empty, **kwargs):
        """Redefined method for selecting the refined fields for serialization."""
        super().__init__(instance=instance, data=empty, **kwargs)
        self._set_ref_meta_fields(isinstance(instance, Iterable))

    def _set_ref_meta_fields(self, is_iterable_fields):
        """
        Set fields attribute for class Meta of this class.

        Args:
            :param is_iterable_fields: is instance iterable
            :type is_iterable_fields: bool
        """
        meta_class = getattr(self, 'Meta', None)
        if meta_class:
            meta_class.fields = getattr(meta_class, '_common_fields', ())\
                                + self._get_ref_fields(meta_class, is_iterable_fields)

    @staticmethod
    def _get_ref_fields(meta_class, is_iterable_fields):
        return getattr(meta_class, '_list_fields', ()) if is_iterable_fields\
               else getattr(meta_class, '_retrieve_fields', ())


class CommentSerializer(HyperlinkedModelSerializer):
    owner = UserSerializer(required=False)

    class Meta:
        model = Comment
        fields = ('id', 'post', 'owner', 'parent',
                  'content', 'publication_date', 'url')
        read_only_fields = ('id', 'owner')
