from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('work/', views.WorkView.as_view(), name='work'),
    path('work/<int:work_id>/', views.detail_my_work, name='detail_my_work'),
    path('projects/', views.MyProjectDetailView.as_view(), name='project'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)