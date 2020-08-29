from django.http import JsonResponse
from django.shortcuts import render
from .models import PlaceOfWork, MyInformation, Project
from django.views.generic import ListView


def welcome(request):
    last_id = MyInformation.objects.all().last().id
    my_obj = MyInformation.objects.get(id=last_id)
    return render(request, 'face.html', {'my_obj': my_obj})


class WorkView(ListView):
    model = PlaceOfWork
    context_object_name = 'list_resume'
    template_name = 'mysite/resume.html'

def detail_my_work(request, work_id):
    name_work = PlaceOfWork.objects.get(id=work_id)
    detail_work = list(name_work.detail_set.all().values())
    return JsonResponse({'elem': detail_work })


class MyProjectDetailView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'mysite/myprojects.html'


