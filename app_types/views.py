from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def types(request):
    return HttpResponse ('หมวดหมู่')

def type(request, type_id):
    return HttpResponse('หมวดหมู่ ID = ' + str(type_id))
