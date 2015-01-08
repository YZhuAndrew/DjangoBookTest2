# -*- coding: utf-8 -*-
__author__ = 'Yun'
__project__ = 'DjangoBookTest2'

# from django.template import Template, Context
# from django.template.loader import get_template
# from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime


def current_datetime(request):
    # now = datetime.datetime.now()
    # t = Template("<html><body>It is now {{ current_date }}.</body></html>")
    # t = get_template('current_datetime.html')
    # html = t.render(Context({'current_date': now}))
    # return HttpResponse(html)
    # return render_to_response('current_datetime.html', {'current_date': now})
    current_date = datetime.datetime.now()
    locals_prams = {'locals': locals(), }
    # locals_prams = {'current_date': now, 'name': 'YZhu', 'list': {'name': 'Qiqi', 'age': '29', 'gender': 'man'}}
    return render_to_response('current_datetime.html', locals_prams)


def display_meta(request):
    context_dict = {'meta_dict': request.META, }
    return render_to_response('display_meta.html', context_dict)