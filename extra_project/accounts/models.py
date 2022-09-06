from asyncio.windows_events import NULL
from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.urls import reverse_lazy

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email: raise ValueError('Users must have as email address')
        user = self.model(
            username=username,
            email=self.normalize_email(email)
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        user = self.create_user(email, password=password)
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def get_absolute_url(self):
        return reverse_lazy('accounts:home')

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', primary_key=True, on_delete=models.CASCADE)
    GRADE_CHOICES = [
        (1, '1回生'),
        (2, '2回生'),
        (3, '3回生'),
        (4, '4回生'),
        (5, 'それ以外'),
        (6, '秘密'),
    ]
    grade = models.IntegerField(choices=GRADE_CHOICES)
    DEPARTMENT_CHOICES = [
        ('土木工学科', '土木工学科'),
        ('建築学科', '建築学科'),
        ('電気電子工学科', '電気電子工学科'),
        ('機械工学科', '機械工学科'),
        ('生命応用科学科', '生命応用科学科'),
        ('情報工学科', '情報工学科'),
        ('秘密', '秘密'),
    ]
    department = models.CharField(max_length=30, choices=DEPARTMENT_CHOICES)
    image = models.ImageField(null=True, blank=True, upload_to='media', default=NULL)
    message = models.TextField(max_length=100, blank=True, null=True, default='自己紹介を記入してください')