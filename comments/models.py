# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Comment(models.Model):
    name = models.CharField(verbose_name=u'名字', max_length=100)
    email = models.EmailField(verbose_name=u'邮箱', max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey('blog.Post')

    class Meta:
        verbose_name = u"评论"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.text[:20]
