# coding = utf-8
__author__ = 'mm'


from .models import Course, Lesson, Video, CourseResource
from organization.models import CourseOrg
import xadmin


class LessonInline(object):
    model = Lesson
    extra = 0


class CourseResourceInline(object):
    model = CourseResource
    extra = 0


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'click_nums', 'students', 'get_zj_nums', 'go_to']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'click_nums', 'students']
    ordering = ['-click_nums']
    readonly_fields = ['click_nums']
    list_editable = ['degree', 'desc']
    exclude = ['students']
    inlines = [LessonInline, CourseResourceInline]
    refresh_times = [3, 5]
    import_excel = True
    # style_fields = {'detail': 'ueditor'}


    # def save_models(self):
    #     # 在保存课程的时候统计课程机构的课程数
    #     obj = self.new_obj
    #     obj.save()
    #     if obj.course_org is not None:
    #         course_org = obj.course_org
    #         course_org.course_nums = Course.objects.filter(course_org=course_org).count()
    #         course_org.save()
    # def queryset(self):
    #     qs = super(CourseAdmin, self).queryset()
    #     qs.filter(is_banner=True)
    #     return qs


# class BannerCourseAdmin(object):
#     list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'click_nums', 'students']
#     search_fields = ['name', 'desc', 'detail', 'degree', 'students']
#     list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'click_nums', 'students']
#     ordering = ['-click_nums']
#     readonly_fields = ['click_nums']
#     exclude = ['students']
#     inlines = [LessonInline, CourseResourceInline]

    # 过滤轮播图信息
    # def queryset(self):
    #     qs = super(BannerCourseAdmin, self).queryset()
    #     qs.filter(is_banner=True)
    #     return qs


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
# xadmin.site.register(BannerCourse, BannerCourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
