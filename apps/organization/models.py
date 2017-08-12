# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from datetime import datetime


# Create your models here.

# CourseOrg 机构信息

# CityDict 城市信息


class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"城市")
    desc = models.CharField(max_length=200, verbose_name=u"描述")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    class Meta:
        verbose_name = u"城市"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseOrg(models.Model):
    city = models.ForeignKey(CityDict, verbose_name=u"所在城市")
    name = models.CharField(max_length=50, verbose_name=u"机构名称")
    desc = models.TextField(max_length=500, verbose_name=u"机构描述")
    category = models.CharField(default="pxjg", verbose_name=u"机构类别", max_length=20,
                                choices=(("pxjg", "培训机构"), ("gr", "个人"), ("gx", "高校")))
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏数")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name=u"封面图", max_length=100)
    address = models.CharField(max_length=150, verbose_name=u"机构地址")
    sutudents = models.IntegerField(default=0, verbose_name=u"课程数")
    course_nums = models.ImageField(default=0, verbose_name=u"学习人数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    class Meta:
        verbose_name = u"机构"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name="所属机构")
    name = models.CharField(max_length=50, verbose_name=u"教师名称")
    work_years = models.IntegerField(default=0, verbose_name=u"工作年限")
    work_company = models.CharField(max_length=50, verbose_name=u"就职公司")
    work_position = models.CharField(max_length=50, verbose_name=u"公司职位")
    points = models.CharField(max_length=50, verbose_name=u"教学特点")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏数")
    image = models.ImageField(default='',upload_to="teacher/%Y/%m", verbose_name=u"头像", max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"创建时间")

    class Meta:
        verbose_name = u"教师"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name