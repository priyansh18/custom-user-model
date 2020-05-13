from django.db import models


# Create your models here.
from django.contrib.auth.models import(
    BaseUserManager, AbstractBaseUser
)


class userManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("User must have a emaill address")
        if not password:
            raise ValueError("User must have a password")
        user_obj = self.model(email=self.normalize_email(email))
        user_obj.set_password(password)
        user_obj.admin = is_admin
        user_obj.staff = is_staff
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(email, password=password, is_staff=True)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password=password, is_admin=True)
        return user


class myUser(AbstractBaseUser):
    email = models.EmailField(max_length=300, unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    # username an password are provided by default
    REQUIRED_FIELD = []

    objects = userManager()

    def __str__(self):
        return

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.staff
