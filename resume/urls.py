from django.urls import path
from .views import *

urlpatterns = [
    path('', welcome, name='welcome'),
    path('work/', work, name='work'),
    path('work/<int:work_id>/', detail_my_work, name='detail_my_work'),
    path('projects/', project, name='project'),
]