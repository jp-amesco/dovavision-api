from django.db import models

class User(models.Model):
	name = models.CharField(max_length=50)	
	email = models.CharField(max_length=50)	
	password = models.CharField(max_length=100)	
	birth = models.DateField()	

	def __str__(self):
		return self
		
