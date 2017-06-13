# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__date__ = '2017/6/5 15:06'


from django.conf.urls import url
from . import views


app_name = 'blog'
urlpatterns = [
    # 第一个参数是网址，第二个参数是处理函数
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
]
