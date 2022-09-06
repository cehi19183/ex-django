from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import RegistBaseForm, UserLoginForm
from . import models


# Create your views here.
# 初期画面
class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'accounts/home.html'

# 新規ユーザー登録
class RegistUserView(generic.CreateView):
    template_name = 'accounts/regist.html'
    form_class = RegistBaseForm

# 登録ユーザーの認証(ログイン)
class LoginUserView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = UserLoginForm

# ログアウト
class LogoutUserView(LogoutView):
    pass

# userprofileモデルの表示
class UserDetailView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'accounts/user_detail.html'
    model = models.UserProfile

class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'accounts/user_update.html'
    model = models.UserProfile
    fields = ['grade', 'department', 'image']

    def get_success_url(self):
        return reverse_lazy('accounts:profile', kwargs={'pk': self.object.pk})

class UserDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'accounts/user_delete.html'
    model = models.User
    success_url = reverse_lazy('accounts:login')