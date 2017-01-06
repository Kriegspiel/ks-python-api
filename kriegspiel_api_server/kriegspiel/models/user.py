# -*- coding: utf-8 -*-

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models, transaction
from django.utils import timezone


class UserManager(BaseUserManager):
    def _create_user(self, email, username, is_superuser, password=None):
        with transaction.atomic():
            user = self.create(email=email)
            user.username = username
            user.is_staff = is_superuser
            user.is_superuser = is_superuser
            user.set_password(password)
            user.save()
            return user

    def create_user(self, email, username, password=None, **other_fields):
        return self._create_user(email, username, False, password)

    def create_superuser(self, email, username, password, **other_fields):
        return self._create_user(email, username, True, password)


class User(AbstractBaseUser):
    email = models.EmailField(db_index=True, unique=True)
    username = models.CharField(db_index=True, unique=True, max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = (u'username',)

    objects = UserManager()
