from django.db import models

# Create your models here.
class Quake(models.Model):
    Date = models.CharField(max_length=100)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Type = models.CharField(max_length=100)
    Depth = models.FloatField()
    Magnitude = models.FloatField()
    Magnitude_Type = models.CharField(max_length=100)
    ID = models.CharField(max_length=100)

    def __str__(self):
        return self.ID

    class Meta:
        verbose_name_plural = 'Quake'

class datapoint(models.Model):
    ID = models.CharField(max_length=100)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Elevation = models.FloatField()
    Object_Tags = models.CharField(max_length=100)
    Object_Count = models.FloatField()
    Datapoint_Group = models.CharField(max_length=100)
    Image = models.CharField(max_length=100) 
    

    def __str__(self):
        ret = self.ID + " " + self.Object_Tags
        return ret
        

    class Meta:
        verbose_name_plural = 'datapoint'