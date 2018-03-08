"""mxonline5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
# coding = utf-8
from django.conf.urls import url, include
from django.contrib import admin
# templateview引用
from django.views.generic import TemplateView
import xadmin
# 处理静态文件
from django.views.static import serve

from users.views import LoginView, RegisterView, ActiveUserView,IndexView
from users.views import ForgetPwdView, ResetView, ModifyPwdView, LogOutView
from organization.views import OrgView, AddFavView
from users.models import UserProfile
from mxonline5.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^index/$', IndexView.as_view(), name='index'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    # 退出登录
    url(r'^logout/$', LogOutView.as_view(), name='logout'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='user_active'),
    url(r'^forget/$', ForgetPwdView.as_view(), name='forget_pwd'),
    url(r'^reset/(?P<reset_code>.*)/$', ResetView.as_view(), name='reset_pwd'),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name='modify_pwd'),
    # 机构url配置
    url(r'^org/', include('organization.urls', namespace='org')),
    # 课程相关url配置
    url(r'^course/', include('courses.urls', namespace='courses')),
    # 讲师相关url配置
    url(r'^teacher/', include('courses.urls', namespace='teacher')),
    # 配置上传文件的访问函数处理
    url(r'media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    # 自己配置静态文件
    # url(r'static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),

    # 机构收藏
    url(r'^add_fav/$', AddFavView.as_view(), name='add_fav'),
    # 用户个人中心
    url(r'^users/', include('users.urls', namespace='users')),
    # 富文本url相关
    # url(r'^ueditor/',include('DjangoUeditor.urls' )),

]
# 全局404页面配置
handler404 ='users.views.page_not_found'
handler500 ='users.views.page_error'
handler403 ='users.views.page_errors'