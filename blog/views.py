# _*_ coding: utf-8 _*_
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import markdown

from comments.forms import CommentForm
from .models import Post, Category
# Create your views here.


def index(request):
    #  all方法返回的是一个QuerySet（可以理解为一个类似于列表的数据结构），
    # 由于同常来说博客文章列表是按文章发表时间倒序排列的，即最新的文章排在最前面，
    # 所以我们紧接着调用了order_by方法对返回的queryset进行排序。
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # 记得在顶部引入 markdown模块
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    # 记得在顶部导入CommentForm
    form = CommentForm()
    # 获得这篇post下的全部评论
    comment_list = post.comment_set.all()
    return render(request, 'blog/detail.html', context={'post': post,
                                                        'form': form,
                                                        'comment_list': comment_list})


def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list':post_list})
