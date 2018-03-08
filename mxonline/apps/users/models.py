# coding = utf - 8
from django.db import models
from datetime import datetime

from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, default='', verbose_name=u'昵称')
    birday = models.DateField(verbose_name=u'生日', null=True)
    gender = models.CharField(max_length=10, choices=(('male', u'男'), ('female', u'女')), default='female', verbose_name=u'性别')
    address = models.CharField(max_length=100, default=u'地址', verbose_name=u'地址')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u'手机号')
    image = models.ImageField(upload_to='image/%Y/%m', default=u'image/default.png', max_length=100, verbose_name=u'头像')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    # 继承dj生成的数据表
    def __unicode__(self):
        return self.username

    # 获取用户未读消息
    def unread_nums(self):
        from operation.models import UserMessage
        return UserMessage.objects.filter(user=self.id, has_read=False).count()


# 邮箱验证码
class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u'验证码')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱')
    send_type = models.CharField(choices=(('register', u'注册'), ('forget', u'找回密码'), ('update_email', u'修改邮箱')), max_length=20, verbose_name=u'验证码类型')
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u'发送时间')

    class Meta:
        verbose_name = u'邮箱验证码'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.email)

    # def __str__(self):
    #     return self.code


# 轮播图
class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'标题')
    image = models.ImageField(upload_to='banner/%Y/%m', verbose_name=u'轮播图', max_length=100)
    url = models.URLField(max_length=200, verbose_name=u'访问地址')
    index = models.IntegerField(default=100, verbose_name=u'顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title