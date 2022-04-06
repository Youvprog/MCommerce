from django.db import models

# Create your models here.

from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
