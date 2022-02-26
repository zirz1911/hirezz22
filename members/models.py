import datetime
import os
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, user_id, user_name, user_email, password=None):
        if not user_id:
            raise ValueError("User Id required...")
        if not user_name:
            raise ValueError("Name required...")
        if not user_email:
            raise ValueError("Email required...")

        user = self.model(
            user_id=user_id,
            user_name=user_name,
            user_email=user_email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, user_name, user_email, password=None):
        user = self.create_user(
            user_id=user_id,
            user_name=user_name,
            user_email=user_email,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class myUser(AbstractBaseUser):
    user_id = models.CharField(verbose_name="user_id", max_length=50, unique=True)
    user_name = models.CharField(verbose_name="user name", max_length=100)
    user_lastname = models.CharField(verbose_name="user lastname", max_length=100)
    user_email = models.EmailField(verbose_name="user email", max_length=100)
    user_job = models.CharField(verbose_name="user job", max_length=50)
    user_date_join = models.DateTimeField(verbose_name="user time join", auto_now_add=True)
    user_last_login = models.DateTimeField(verbose_name="user last login", auto_now=True)
    user_profile = models.ImageField(upload_to="uploads/", null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "user_id"

    REQUIRED_FIELDS = ['user_name', 'user_email']

    objects = MyUserManager()

    def __str__(self):
        return self.user_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Item(models.Model):
    p_id = models.AutoField(primary_key=True)
    topic = models.TextField(max_length=200)
    price = models.FloatField(default=0.00)
    description = RichTextField(blank=True, null=True)
    contactFb = models.TextField(max_length=100, null=True)
    contactTw = models.TextField(max_length=100, null=True)
    contactEmail = models.TextField(max_length=100, null=True)
    contactOther = models.TextField(max_length=100, null=True)
    image = models.ImageField(upload_to="uploads/", null=True, blank=True)
    image2 = models.ImageField(upload_to="uploads/", null=True, blank=True)
    image3 = models.ImageField(upload_to="uploads/", null=True, blank=True)

