from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class IndustryList(models.Model):
	i_name = models.CharField(max_length=255)
	def __str__(self):
		return self.i_name


class Company(models.Model):
	name = models.CharField(max_length=255)
	website = models.CharField(max_length=255)
	phoneNumber = models.CharField(max_length=255)
	addr = models.TextField()
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=255)
	country = models.CharField(max_length=255)
	industry_list = models.ForeignKey(IndustryList, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('home')
