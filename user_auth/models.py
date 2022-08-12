from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class OurUserManager(BaseUserManager):
    def create_user(self, username, email, tos, password=None):
        if not username:
            return ValueError('Username is required')

        if not email:
            return ValueError('Email address is required')

        if not tos:
            return ValueError('Please ACCEPT our Terms of Service and Privacy Policy')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            tos=tos,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, tos, password):
        user = self.create_user(
            username=username,
            email=self.normalize_email(email),
            tos=tos,
            password=password,
        )

        # user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class OurUser(AbstractBaseUser):
    username = models.CharField(
        verbose_name='Username', max_length=60, unique=True)
    email = models.EmailField(
        verbose_name='Email Address', max_length=60, unique=True)

    tos = models.BooleanField(verbose_name='Terms of Services', default=False)

    date_joined = models.DateTimeField(
        verbose_name='Date Joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='Last Login', auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'tos', ]

    class Meta:
        verbose_name = 'User'

    objects = OurUserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
