import uuid
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def _create_user(self, username, password, is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username and password.
        """
        user = self.model(username=username,
                          is_staff=is_staff,
                          is_superuser=is_superuser,
                          **extra_fields)
        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        return self._create_user(username,
                                 password,
                                 False,
                                 False,
                                 **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        return self._create_user(username,
                                 password,
                                 True,
                                 True,
                                 **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(db_index=True,
                            primary_key=True,
                            default=uuid.uuid4)

    is_active = models.BooleanField(default=True)

    username = models.CharField(max_length=150,
                                unique=True)
    first_name = models.CharField(max_length=120,
                                  blank=True,
                                  default='')
    last_name = models.CharField(max_length=120,
                                 blank=True,
                                 default='')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def get_full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'
