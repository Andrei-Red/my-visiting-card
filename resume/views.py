from django.http import JsonResponse
from django.shortcuts import render
from .models import PlaceOfWork, MyInformation


def welcome(request):
    last_id = MyInformation.objects.all().last().id
    my_obj = MyInformation.objects.get(id=last_id)
    return render(request, 'face.html', {'my_obj': my_obj})


def work(request):
    list_resume = PlaceOfWork.objects.all()
    return render(request, 'mysite/resume.html', {'list_resume': list_resume})


def detail_my_work(request, work_id):
    name_work = PlaceOfWork.objects.get(id=work_id)
    detail_work = list(name_work.detail_set.all().values())
    return JsonResponse({'elem': detail_work })


def project(request):
    return render(request, 'mysite/myprojects.html')