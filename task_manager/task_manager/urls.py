from django.contrib import admin
from django.urls import path, include, re_path


from task_manager.task_manager.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    re_path(r'^i18n/', include('django.conf.urls.i18n')),
]
