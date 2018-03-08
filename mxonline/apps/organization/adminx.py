# coding = utf-8
__author__ = 'mm'


from .models import CityDict, CourseOrg, Teacher
import xadmin


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc', ]
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_num', 'fav_nums', 'image', 'address', 'city', 'city', 'add_time']
    search_fields = ['name', 'desc', 'click_num', 'fav_nums', 'image', 'address', 'city', 'city']
    list_filter = ['name', 'desc', 'click_num', 'fav_nums', 'image', 'address', 'city', 'city', 'add_time']
    relfield_style = 'fa-ajax'


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_num', 'fav_nums', 'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_num', 'fav_nums']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_num', 'fav_nums', 'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)

