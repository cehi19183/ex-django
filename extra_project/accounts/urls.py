from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('regist/', views.RegistUserView.as_view(), name='regist'),
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
    path('profile/<int:pk>/', views.UserDetailView.as_view(), name='profile'),
    path('user_delete/<int:pk>/', views.UserDeleteView.as_view(), name='delete'),
]