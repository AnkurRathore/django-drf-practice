from django.db import models


# Create your models here.
class Consumers(models.Model):
    street = models.CharField(max_length=300)
    status = models.CharField(max_length=200)
    previous_jobs_count = models.IntegerField(default=0)
    amount_due = models.IntegerField()
    lat = models.FloatField()
    lng = models.FloatField()
