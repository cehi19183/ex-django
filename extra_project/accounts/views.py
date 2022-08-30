from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import RegistBaseForm, UserLoginForm
from . import models


# Create your views here.
class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'accounts/home.html'

class RegistUserView(generic.CreateView):
    template_name = 'accounts/regist.html'
    form_class = RegistBaseForm

class LoginUserView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = UserLoginForm

class LogoutUserView(LogoutView):
    pass

class UserDetailView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'accounts/user_detail.html'
    model = models.UserProfile

class UserDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'accounts/user_delete.html'
    model = models.User
    success_url = reverse_lazy('accounts:login')