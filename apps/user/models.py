# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.utils.translation import ugettext_lazy as _
# from .managers import UserManager

# class User(AbstractUser):
#     username=models.CharField(max_length=50)
#     email=models.EmailField(_('email address'), unique=True)
#     name = models.CharField(max_length=150)
#     user_level = models.CharField(max_length=20, blank=True)
    
#     USERNAME_FIELD='username'
#     REQUIRED_FIELDS=['username', 'email', 'name', 'user_level']

#     objects = UserManager()

#     def __str__(self):
#         return self.username
    