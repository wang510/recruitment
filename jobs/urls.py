from django.conf.urls import url
from django.urls import path
from django.conf import settings

from jobs import views




urlpatterns = [
    # 职位列表
    path("joblist/", views.joblist, name="joblist"),
	# 职位详情
	path('job/<int:job_id>/', views.detail, name='detail'),
]
