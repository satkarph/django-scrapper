from django.db import models

# Create your models here.
class File(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True )
    url = models.CharField(max_length=500,  blank=True, null=True)

    def __str__(self):
        return self.url
