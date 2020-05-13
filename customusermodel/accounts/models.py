from django.db import models


# Create your models here.
from django.contrib.auth.models import(
    BaseUserManager, AbstractBaseUser
)


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
