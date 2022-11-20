from django.shortcuts import render,HttpResponse,redirect

from django.http import HttpResponseBadRequest
from django import forms
from django.template import RequestContext
from django.db.models import Q
import django_excel as excel
from home.models import Excel
import csv
# Create your views here.
def index(request):
    data=Excel.objects.all()
    if 'q' in request.GET:
        q=request.GET['q']
        Excel.objects.filter(Q(Title_icontains=q)|Q(authors_icontains=q)|Q(dbid_icontains=q))
    
    return render(request,'index.html',{'data':data})


def search(request):
    query=request.GET['query']
    # allPosts=Excel.objects.all()
    allPosts=Excel.objects.filter(Q(Title__icontains=query)|Q(authors__icontains=query)|Q(dbid__icontains=query))

    params={'allPosts':allPosts}

    return render(request,'search.html',params)

# def venue(request):
#     response=HttpResponse(content_type='text/csv')
#     response['content']