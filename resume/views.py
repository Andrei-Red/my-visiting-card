from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import *


def welcome(request):
    contacts = MyContact.objects.get(id=1)
    return render(request, 'face.html', {'contacts': contacts})



def work(request):
    list_resume = PlaceOfWork.objects.all()
    return render(request, 'mysite/resume.html', {'list_resume': list_resume})


def detail_my_work(request, work_id):
    id_work = PlaceOfWork.objects.get(id=work_id)
    detail_work = id_work.detail_set.all()
    return render(request, 'mysite/detail_work.html', {'detail_work': detail_work, 'id_work': id_work})


def project(request):
    return render(request, 'lastprojects.html')