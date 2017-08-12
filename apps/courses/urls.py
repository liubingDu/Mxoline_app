# -*- coding: utf-8 -*-


from django.conf.urls import url, include

from .views import CourseListView,CourseVisw,CourseVideoView

# 课程机构首页
urlpatterns =[

    url(r'^list/$',CourseListView.as_view(), name="course_list"),

    url(r'^detail/(?P<course_id>\d+)/$', CourseVisw.as_view(), name="course_detail"),

    url(r'^video/(?P<course_id>\d+)/$', CourseVideoView.as_view(), name="course_video"),

]