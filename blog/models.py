from django.db import models

from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Create your models here.
class Estimate_of_day(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateField()
	estimate = models.IntegerField()
