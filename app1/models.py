from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class SchoolData(models.Model):
    name = models.CharField(max_length=100)
    payable_amount = models.IntegerField()
    paid_amount = models.IntegerField()
    remaining_amount = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return self.name