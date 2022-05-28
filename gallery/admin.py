from django.contrib import admin
from .models import location,category,image



# Register your models here.
admin.site.register(image)
admin.site.register(location)
admin.site.register(category)
