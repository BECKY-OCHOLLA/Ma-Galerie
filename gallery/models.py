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

class image(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='Images/',null=True ,blank=True)
    description=models.TextField()
    category=models.ForeignKey(category,on_delete=models.CASCADE,)
    location=models.ForeignKey(location,on_delete=models.CASCADE,)
    author=models.CharField(max_length=40, default='admin')
    date=models.DateTimeField(auto_now_add=True)

    @classmethod
    def filter_by_location(cls,location):
      image_location = image.objects.filter(location__name=location).all()
      return image_location

    def save_image(self):
        self.save()

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    @classmethod
    def search_by_category(cls, category):
        images = cls.objects.filter(category__name__icontains=category)
        return images

    def __str__(self):
        return self.name


    def delete_image(self):
        self.delete()

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
    
        return image

    class Meta:
        ordering = ['date']
    
    

