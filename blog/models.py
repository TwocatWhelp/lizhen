# _*_ coding:utf-8 _*_
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
'''文章(Post)、 分类(Tag)、 标签(Category)'''


class Category(models.Model):
    """
    Djamgo要求模型必须继承models.Model类。
    Category只需要一个简单的分类名name就可以了
    CharField指定分类名name的数据类型，CharField是字符型，
    CharField的max_length参数指定其最大长度，超过这个长度的分类名就不能存入数据库。
    当然Django还为我们提供了多种其他的数据类型，如日期时间类型DateTimeField、整数类型IntegerField等
    """
    name = models.CharField(max_length=100, verbose_name=u'分类')

    class Meta:
        verbose_name = u"分类"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    """
    标签Tag也比较简单，和Category一样
    再次强调一定继承models.model类！！！
    """
    name = models.CharField(max_length=100, verbose_name=u'标签')

    class Meta:
        verbose_name = u"标签"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Post(models.Model):
    """
    文章的数据类型表稍微复杂一点，主要是涉及的字段更多。
    """
    # 标题
    title = models.CharField(max_length=50, verbose_name=u'标题')

    # 文章正文，我们使用了TextField
    # 存储比较短的字符串可以使用CharField，但对于文章的正文来说可能会是一大段文字，因此使用TextField来存储大段文本。
    body = models.TextField()

    # 这两个列分别表示文章的创建时间和最后一次修改时间，存储时间的字段用DateTimeField类型。
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # 文章摘要，可以没有文章摘要，但默认情况下CharField要求我们必须存入数据，否则就会报错
    # 指定 CharField的 blank=True 参数值后就可以允许空值了
    excerpt = models.CharField(max_length=200, verbose_name=u'摘要', blank=True)

    # 这是分类与标签，分类与标签的模型我们已经定义在上面。
    # 我们在这里把文章对应的数据库表和分类、标签对应的数据库表关联了起来，但是关联形式稍微有点不同。
    # 我们规定一篇文章只能对应一个分类，但是一个分类下可以有多篇文章，所以我们使用的是 ForeignKey，即一对多的关联关系。
    # 而对于标签来说，一篇文章可以有多个标签，同一个标签下也可能有多篇文章，所以我们使用 ManyToManyField，表明这是多对多的关联关系。
    # 同时我们规定文章可以没有标签，因此为标签 tags 指定了 blank=True。
    # 如果你对 ForeignKey、ManyToManyField 不了解，请看教程中的解释，亦可参考官方文档：
    # https://docs.djangoproject.com/en/1.10/topics/db/models/#relationships
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
    # 这里我们通过 ForeignKey 把文章和 User 关联了起来。
    # 因为我们规定一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是一对多的关联关系，和 Category 类似。
    author = models.ForeignKey(User, verbose_name=u'作者')

    class Meta:
        verbose_name = u"正文"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title

    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse函数
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})


"""
    author。文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程。
    其中 User 是 Django 为我们已经写好的用户模型，和我们自己编写的 Category 等类是一样的。
    这里我们通过 ForeignKey 把文章和 User关联了起来，因为我们规定一篇文章只能有一个作者，
    而一个作者可能会写多篇文章，因此这是一对多的关联关系，和 Category 类似。
"""
