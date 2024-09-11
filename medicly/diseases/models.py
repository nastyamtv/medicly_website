from django.db import models
from django_resized import ResizedImageField
class Disease(models.Model):
    name = models.CharField(max_length=60)
    title = models.CharField(max_length=60, default="")
    #image = models.ImageField(upload_to='uploads/cinema/')
    description = models.CharField(max_length=60, default="")
    #status = models.CharField(max_length=60, default="")
    #image = models.ImageField(upload_to='uploads/medicine/', default="" , blank=True)
    image = ResizedImageField(
        size=[400, 200],
        crop=["middle", "center"],
        default="default_image.jpg",
        upload_to="uploads/medicine/",
    )