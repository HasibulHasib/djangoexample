from django.db import models

'''class testf(models.Model):
    f1 = models.CharField(max_length=122)
    def __str__(self):
        return self.f1'''
# Create your models here
class my_order(models.Model):
    name= models.CharField(max_length=120, null=True)
    email= models.EmailField(blank=False, null=True)
    phone= models.CharField(max_length=20, null=True)
    flat= models.CharField(max_length=6, null=True)
    house= models.CharField(max_length=6, null=True)
    avenue= models.CharField(max_length=6,null=True)
    road= models.CharField(max_length=6, null=True)
    def __str__(self):
        return self.name
