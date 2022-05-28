from django.db import models

# Create your models here.
class location(models.Model):
    name=models.CharField(max_length=50)

    @classmethod
    def get_locations(cls):
      locations = Location.objects.all()
      return locations

    def __str__(self):
      return self.name
