from django.db import models

# Create your models here.

class videolink(models.Model):
    link = models.CharField(max_length=200)
    quality = models.IntegerField(null=True,blank=True)



    def __str__(self):
        return self.link

