from django.contrib import admin
from django.urls import path, include, re_path


# from task_manager.task_manager.views import *
from task_manager.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^i18n/', include('django.conf.urls.i18n')),
    path('', home, name='home'),
    path('users/', UserListView.as_view(), name='users'),
    path('users/create/', CreateUser.as_view(), name='create_user'),
    path('users/<int:pk>/update/', UpdateUser.as_view(), name='update_user'),
    path('users/<int:pk>/delete/', DeleteUser.as_view(), name='create_user'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]
