from django.urls import path
from . import views


urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('work/', views.work, name='work'),
    path('work/<int:work_id>/', views.detail_my_work, name='detail_my_work'),
    path('projects/', views.project, name='project'),
]