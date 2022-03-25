from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    price =  models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=500, blank=True, null=True)
    image  = models.ImageField(upload_to='pics')
    discount = models.BooleanField()
    discount_percentage = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    video_url = models.CharField(max_length=200,blank=True,null=True)
