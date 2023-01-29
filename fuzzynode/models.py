from django.db import models


# Create your models here.
class urbansea(models.Model):
    name=models.CharField(unique=True,null=False,blank=False,max_length=100)
    slug=models.CharField(unique=False,null=False,blank=False,max_length=100)
    def __str__(self) -> str:
        return self.name
