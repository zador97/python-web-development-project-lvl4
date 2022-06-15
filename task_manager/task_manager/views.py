from django.http import HttpRequest, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods

from .forms import LoginUserForm, CreateUserForm


def home(request):
    return render(request, 'task_manager/home.html')


class UserListView(ListView):
    model = User
    context_object_name = 'users_list'


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'task_manager/login.html'


class CreateUser(CreateView):
    form_class = CreateUserForm
    template_name = 'task_manager/register.html'
    success_url = reverse_lazy('login')


class UpdateUser(UpdateView):
    model = User
    form_class = CreateUserForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('users')


class DeleteUser(DeleteView):
    model = User
    success_url = reverse_lazy('users')


@require_http_methods(['GET'])
def logout_user(request):
    logout(request)

    return redirect('login')
