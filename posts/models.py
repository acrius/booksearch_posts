from django.db.models import Model, CharField, TextField,\
                             DateTimeField, ForeignKey
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Post(Model):
    class Meta:
        ordering = ('publication_date',)

    title = CharField(max_length=200)
    content = TextField()
    publication_date = DateTimeField('Date of publish.', auto_now_add=True,
                                     blank=True)
    owner = ForeignKey(User)
    tags = TaggableManager()

class Comment(Model):
    class Meta:
        ordering = ('publication_date',)

    post = ForeignKey(Post)
    owner = ForeignKey(User, blank=True)
    parent = ForeignKey('Comment', null=True, blank=True)
    content = TextField()
    publication_date = DateTimeField('Date of publish.', auto_now_add=True,
                                     blank=True)
