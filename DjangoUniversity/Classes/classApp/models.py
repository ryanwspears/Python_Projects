from django.db import models


# This is the model for the classes.
class djangoClasses(models.Model):
    title = models.CharField(max_length=50, blank=False)
    courseNum = models.IntegerField(blank=False, unique=True)
    instructorName = models.CharField(max_length=50, blank=False)
    duration = models.FloatField(max_length=4, blank=False)
