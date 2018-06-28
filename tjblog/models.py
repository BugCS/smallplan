from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime
# Create your models here.
# coding: utf-8


class Article(models.Model):
    # 文章标题可以重名，不同的用户id就可以分别
    title = models.CharField(max_length=255)
    # 简介可以为空
    brief = models.CharField(null=True, blank=True, max_length=255)
    # 所属版块 Category类位于Article下面时，调用需要加上引号
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    content = models.TextField(u"文章内容")
    author = models.ForeignKey("UserProfile", on_delete=models.CASCADE)
    # auto_now 和 auto_now_add 区别？
    # 每次对象修改了，保存都会更新auto_now的最新时间
    # 每次对象创建的时候，会生成auto_now_add 时间
    pub_date = models.DateTimeField(blank=True, null=True)
    last_modify = models.DateTimeField(auto_now=True)
    # 文章置顶功能
    priority = models.IntegerField(u"优先级", default=1000)
    head_img = models.ImageField(u"文章标题图片", upload_to="uploads")

    status_choices = (('draft', u"草稿"),
                      ('published', u"已发布"),
                      ('hidden', u"隐藏"),
                      )
    status = models.CharField(choices=status_choices, default='published', max_length=32)

    def __str__(self):
        return self.title

    # 自定义model验证（除django提供的外required max_length 。。。），验证model字段的值是否合法
    def clean(self):
        # Don't allow draft entries to have a pub_date.
        if self.status == 'draft' and self.pub_date is not None:
            raise ValidationError(('Draft entries may not have a publication date.'))
        # Set the pub_date for published items if it hasn't been set already.
        if self.status == 'published' and self.pub_date is None:
            self.pub_date = datetime.date.today()


class Comment(models.Model):
    article = models.ForeignKey(Article, verbose_name=u"所属文章", on_delete=models.CASCADE)
    # 关联到同一张表的时候需要关联自己用self，当关联自己以后 想反向查找需要通过related_name来查，
    # 顶级评论不用包含父评论
    parent_comment = models.ForeignKey('self',  related_name='my_children', blank=True, null=True, on_delete=models.CASCADE,)
    comment_choices = ((1, u'评论'),
                       (2, u"点赞"))
    comment_type = models.IntegerField(choices=comment_choices, default=1)
    user = models.ForeignKey("UserProfile", on_delete=models.CASCADE,)
    comment = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    # django clean方法可以实现表字段验证
    # Model.clean()[source]
    # This method should be used to provide custom model validation, and to modify attributes on your model if desired.
    # For instance, you could use it to automatically provide a value for a field,
    # or to do validation that requires access to more than a single field:

    def clean(self):
        if self.comment_type == 1 and len(self.comment) == 0:
            raise ValidationError(u'评论内容不能为空，sb')

    @property
    def __str__(self):
        return "C:%s" %(self.comment)


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    brief = models.CharField(null=True, blank=True, max_length=255)
    # 一般页面的版块是固定死的，但是我们想动态生成版块的时候，我们需要定义一个位置字段和是否显示字段
    # 一般常规的网站首页都是固定的
    set_as_top_menu = models.BooleanField(default=False)
    position_index = models.SmallIntegerField()
    # 可以有多个管理员
    admins = models.ManyToManyField("UserProfile", blank=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    """
    在用户表中定义一个friends 字段，关联自己
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    name = models.CharField(max_length=32)
    signature = models.CharField(max_length=255, blank=True, null=True)
    head_img = models.ImageField(height_field=150, width_field=150, blank=True, null=True)
    # for web qq
    friends = models.ManyToManyField('self', related_name="my_friends", blank=True)

    def __str__(self):
        return self.name
