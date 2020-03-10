from django.db import models
from dovavision.models import Company, User

class Index(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    api_name = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self): 
        return self.name

class Stock(models.Model):
    name = models.CharField(max_length=50)
    api_name = models.CharField(max_length=50, null=True)
    is_active = models.BooleanField(default=True)
    index = models.ForeignKey(Index, on_delete=models.PROTECT) 
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=True)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.name
