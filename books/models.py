from django.db import models

# Create your models here.
class Book(models.Model):
	name	= models.CharField(max_length=120)
	author	= models.CharField(max_length=120)
	category= models.CharField(max_length=120, null=True, blank=True)
	b_file	= models.TextField()


	def __str__(self):
		return self.name