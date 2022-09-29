from django.urls import path, include
from . import views
app_name='job'

urlpatterns = [
   path('', views.job_list, name='job_list'),
   path('<int:pk>', views.job_detail, name='job_detail')
    ]