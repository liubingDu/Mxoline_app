# -*- coding: utf-8 -*-
from pure_pagination import Paginator, PageNotAnInteger
from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.
from courses.models import Course
from .models import Course, Lesson



class CourseListView(View):
    def get(self, request):
        all_courses = Course.objects.all().order_by("-add_time")

        hot_courses = Course.objects.all().order_by("-click_nums")[0:4]

        """
        课程排序
        """
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "students":
                all_courses = all_courses.order_by("-students")
            elif sort == "hot":
                all_courses == all_courses.order_by("-click_nums")

        """
        公开课翻页功能
        """
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_courses, 12, request=request)
        courses = p.page(page)

        """
        """

        return render(request, 'course-list.html', {
            'all_courses': courses,
            'sort': sort,
            'hot_courses': hot_courses,
        })


class CourseVisw(View):
    """
    课程详情页
    """
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))

        """
        增加课程点击数
        """
        course.click_nums+=1
        course.save()

        return render(request, 'course-detail.html', {
            'course_org': course,
        })


class CourseVideoView(View):
    def get(self, request, course_id):
        all_lesson = Course.objects.get(id=int(course_id))
        return render(request, 'course-video.html', {
            'all_lesson': all_lesson,
        })



