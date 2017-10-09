# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from rango.models import Category, Page
from django.db import models
from django.contrib import admin
from django.utils.html import format_html

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}
admin.site.register(Category, CategoryAdmin)




class PageAdmin(admin.ModelAdmin):
	list_display = ['category','title', 'url']
admin.site.register(Page, PageAdmin)

admin.site.site_header = 'Crickareer Administration'
#admin.site.index_title = 'Grv Site Administration'