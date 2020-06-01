from django.http import Http404, HttpResponseRedirect,  JsonResponse
from django.shortcuts import render
from .models import MyContact, PlaceOfWork


def welcome(request):
    contacts = MyContact.objects.get(id=1)
    return render(request, 'face.html', {'contacts': contacts})


def work(request):
    list_resume = PlaceOfWork.objects.all()
    return render(request, 'mysite/resume.html', {'list_resume': list_resume})


def detail_my_work(request, work_id):
    name_work = PlaceOfWork.objects.get(id=work_id)
    detail_work = name_work.detail_set.all()
    return render(request, 'mysite/detail_work.html', {'detail_work': detail_work, 'name_work': name_work})


# def detail_my_work(request, work_id):
#     name_work = PlaceOfWork.objects.get(id=work_id)
#     detail_work = name_work.detail_set.all()
#     ctx = {'elements': list(detail_work)}
#     print(detail_work)
#     print(work_id)
#     return JsonResponse(detail_work)


def project(request):
    return render(request, 'mysite/myprojects.html')