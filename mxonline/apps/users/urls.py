# coding = utf-8
__author__ = 'mm'


from django.conf.urls import url, include
from .views import UserInfoView, UploadImageView, UpdatePwdView, SendEmailCodeView
from .views import UpdateEmailView, MyCourseView, MyFavOrgView, MyFavTeacherView
from .views import MyFavCourseView,MymessageView
urlpatterns = [
    # 用户信息
    url(r'^info/$', UserInfoView.as_view(), name='user_info'),
    # 用户头像上传
    url(r'^img/upload$', UploadImageView.as_view(), name='img_upload'),
    # 用户中心修改密码
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name='update_pwd'),
    # 用户中心中发送邮箱验证码
    url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name='sendemail_code'),
    # 用户中心中修改邮箱
    url(r'^update_email/$', UpdateEmailView.as_view(), name='update_email'),
    # 我的课程
    url(r'^my_course/$', MyCourseView.as_view(), name='my_course'),
    # 我收藏的课程机构
    url(r'^myfav/org$', MyFavOrgView.as_view(), name='myfav_org'),
    # 我收藏的授课教师
    url(r'^myfav/teahcer$', MyFavTeacherView.as_view(), name='myfav_teahcer'),
    # 用户收藏的课程
    url(r'^myfav/course$', MyFavCourseView.as_view(), name='myfav_course'),
    # 我的消息
    url(r'^mymessage$', MymessageView.as_view(), name='mymessage'),

]








