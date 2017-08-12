# -*- coding: utf-8 -*-



from django.conf.urls import url, include

from organization.views import OrgView,AddUseraskView,OrgHomeView,OrgCourseView,OrgDescView,OrgTeacherView,AddFavView

# 课程机构首页
urlpatterns =[
    url(r'^list/$',OrgView.as_view(), name="org_list"),

    url(r'^add_ask/$', AddUseraskView.as_view(), name="add_ask"),

    url(r'^home/(?P<org_id>\d+)/$',OrgHomeView.as_view(),name='org_home'),

    url(r'^course/(?P<org_id>\d+)/$',OrgCourseView.as_view(),name='org_course'),

    url(r'^desc/(?P<org_id>\d+)/$',OrgDescView.as_view(), name='org_desc'),

    url(r'^teacher/(?P<org_id>\d+)/$',OrgTeacherView.as_view(), name='org_teacher'),

    url(r'^add_fav/$', AddFavView.as_view(), name="add_fav"),

]