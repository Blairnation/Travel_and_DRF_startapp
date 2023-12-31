from typing import Any
# from django.db import models
# from django.contrib.auth.models import UserManager, PermissionsMixin
# from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
# from django.utils import timezone

# # Create your models here.
# class UserManager(BaseUserManager):
#   def _create_user(self, username, email, password, is_active, is_staff, is_superuser, **extra_fields):
#       now = timezone.now()
#       if not username:
#          raise ValueError('Username is not valid')
#       email = self.normalize_email(email)
#       user = self.model(username=username, email=email, is_active=True, is_staff=is_staff, 
#                         is_superuser=is_superuser, date_joined=now, **extra_fields)
#       user.set_password(password)
#       user.save(using = self._db)

#       return user
  
#   def create_user(self, username, email, password, **extrafields):
#      return self._create_user(username, email, password, is_active=True, is_staff=False,
#                               is_superuser=False, **extra_fields)

#   def create_superUser(self, username, email, password, **extrafields):
#      user = self._create_user(username, email, password, is_active=True, is_staff=True,
#                               is_superuser=True, **extra_fields)
#      user.save(using = self._db)
#      return user

      
# class User(AbstractBaseUser, PermissionsMixin):
#    username = models.CharField(max_length=30, unique=True)
#    email = models.EmailField(max_length=250, unique=True)
#    first_name = models.CharField(max_length=30, blank=True, null=True)
#    last_name = models.CharField(max_length=30, blank=True, null=True)
#    is_active = models.BooleanField(default=True)
#    is_staff= models.BooleanField(default=False)
#    is_superuser = models.BooleanField(default=False)
#    date_joined = models.DateTimeField(default=timezone.now())
#    recieved_newsletter = models.BooleanField(default=False)
#    birth_date = models.DateTimeField(blank=True, null=True)
#    address = models.CharField(max_length=300, blank=True, null=True)
#    city = models.CharField(max_length=30, blank=True, null=True)

#    objects = UserManager()

#    USERNAME_FIELD = 'username'
#    REQUIRED_FIELDS = ['email']
   
