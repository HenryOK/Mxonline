from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.db.models import Q

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Course, CourseResource, Video
from operation.models import UserFavorite, CourseComments, UserCourse
from utiles.mixin_utils import LoginRequiredMixin
# Create your views here.


class CourseListView(View):
    def get(self, request):
        all_courses = Course.objects.all().order_by('-add_time')

        hot_courses = Course.objects.all().order_by('-click_nums')[:3]
        # 课程搜索
        search_keyword = request.GET.get('keywords', '')
        if search_keyword:
            all_courses = all_courses.filter(Q(name__icontains=search_keyword) | Q(desc__icontains=search_keyword) | Q(detail__icontains=search_keyword))

        # 课程机构类别筛选
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'student':
                all_courses = all_courses.order_by('-students')
            elif sort == 'course':
                all_courses = all_courses.order_by('-click_nums')[3]
        # 对课程进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_courses, per_page=6, request=request)
        courses = p.page(page)
        return render(request, 'course-list.html', {
            'all_courses': courses,
            'sort': sort,
            'hot_courses': hot_courses
        })


class CourseDetailView(View):
    """
    课程详情页
    """
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        # 增加课程点击数
        course.click_nums += 1
        course.save()

        # 是否收藏课程
        has_fav_course = False
        # 是否收藏机构
        has_fav_org = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_fav_course = True

            if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
                has_fav_org = True

        tag = course.tag
        if tag:
            relate_course = Course.objects.filter(tag=tag)[:1]
        else:
            relate_course = []
        return render(request, 'course-detail.html', {
            'course': course,
            'relate_courses': relate_course,
            'has_fav_course': has_fav_course,
            'has_fav_org': has_fav_org

        })


class CourseInfoView(LoginRequiredMixin, View):
    """
    课程章节信息
    """
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        course.students += 1
        course.save()
        # 查询用户是否已经关联该课程
        user_course = UserCourse.objects.filter(user=request.user, course=course)
        if user_course:
            user_course = UserCourse(user=request.user, course=course)
            user_course.save()

        user_course = UserCourse.objects.filter(course=course)
        user_ids = [user_course.user.id for user_course in user_course]
        all_user_course = UserCourse.objects.filter(user_id__in=user_ids)
        # 取出所有课程id
        course_id = [user_course.course.id for user_course in all_user_course]
        # 获取 学过该课程的用户还学过
        relate_courses = Course.objects.filter(id__in=course_id).order_by('-click_nums')[:3]

        all_resources = CourseResource.objects.filter(course=course)
        return render(request, 'course-video.html', {
            'course': course,
            'course_resources': all_resources,
            'relate_courses': relate_courses

        })


class VideoPlayView(View):
    """
    视频播放页面
    """
    def get(self, request, course_id):
        video = Video.objects.get(id=int(course_id))
        course = video.lesson.course
        course.students += 1
        course.save()
        # 查询用户是否已经关联该课程
        user_course = UserCourse.objects.filter(user=request.user, course=course)
        if user_course:
            user_course = UserCourse(user=request.user, course=course)
            user_course.save()

        user_course = UserCourse.objects.filter(course=course)
        user_ids = [user_course.user.id for user_course in user_course]
        all_user_course = UserCourse.objects.filter(user_id__in=user_ids)
        # 取出所有课程id
        course_id = [user_course.course.id for user_course in all_user_course]
        # 获取 学过该课程的用户还学过
        relate_courses = Course.objects.filter(id__in=course_id).order_by('-click_nums')[:3]

        all_resources = CourseResource.objects.filter(course=course)
        return render(request, 'course-play.html', {
            'course': course,
            'course_resources': all_resources,
            'relate_courses': relate_courses,
            'video': video

        })


class CommentsView(View, LoginRequiredMixin):
    """
    评论
    """
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        all_comments = CourseComments.objects.filter(course=course)
        return render(request, 'course-comment.html', {
            'course': course,
            'course_resources': all_comments,
            'all_comments': all_comments
         })


class AddCommentsView(LoginRequiredMixin,View):
    """
    用户添加评论
    """
    def post(self, request):
        if not request.user.is_authenticated():
        # 判断用户登录状态
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')
        course_id = request.POST.get('course_id', 0)
        course_ids =int(course_id)
        comments = request.POST.get('comments', '')
        commentss = int(course_id)
        if course_ids >0 and commentss:
            course_comments = CourseComments()
            course = Course.objects.get(id=int(course_id))
            course_comments.course = course
            course_comments.comments = comments
            course_comments.user = request.user
            course_comments.save()
            return HttpResponse('{"status":"success", "msg":"添加成功"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"success", "msg":"添加失败"}', content_type='application/json')





