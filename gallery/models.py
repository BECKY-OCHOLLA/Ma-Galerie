from django.db import models

# Create your models here.
class location(models.Model):
    name=models.CharField(max_length=50)

    

    def __str__(self):
      return self.name

class category(models.Model):
    name=models.CharField(max_length=50)



    def __str__(self):
      return self.name

class Image(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='Images/',null=True ,blank=True)
    description=models.TextField()
    category=models.ForeignKey(category,on_delete=models.CASCADE,)
    location=models.ForeignKey(location,on_delete=models.CASCADE,)
    author=models.CharField(max_length=40, default='admin')
    date=models.DateTimeField(auto_now_add=True)
