from django.db import models


# Create your models here.
from django.contrib.auth.models import(
    BaseUserManager, AbstractBaseUser
)


class userManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("User must have a emaill address")
        if not password:
            raise ValueError("User must have a password")
        user = self.model(
            email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=self.normalize_email(
            email), password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class myUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email',
                              max_length=300, unique=True)
    date_joined = models.DateTimeField(
        verbose_name='date_joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last_login', auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    # username an password are provided by default
    REQUIRED_FIELD = []

    objects = userManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
