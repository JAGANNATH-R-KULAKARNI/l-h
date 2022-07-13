from django.db import models

class featurefunc(models.Model):
    name = models.CharField(max_length=100)
    tags = models.CharField(max_length=100)
    lastupdateby = models.CharField(max_length=100)
    updateat = models.DateTimeField()
    flagid = models.IntegerField()
    enable = models.BooleanField()

    def __str__(self):
        return self.name