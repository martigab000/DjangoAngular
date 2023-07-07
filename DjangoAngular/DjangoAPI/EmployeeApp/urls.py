from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path

from EmployeeApp import views

urlpatterns=[
   
    re_path(r'^question/$',views.questionApi),
    re_path(r'^question/([0-9]+)$',views.questionApi),

    # re_path(r'^SaveFile$', views.SaveFile)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )