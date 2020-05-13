from django.db import models


# Create your models here.
from django.contrib.auth.models import(
    BaseUserManager, AbstractBaseUser
)


class myUser(AbstractBaseUser):
    username = models.CharField(max_length=300)
