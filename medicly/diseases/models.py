from django.db import models
from datetime import date
from django_resized import ResizedImageField
class Disease(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Disease Name",
        default="Unknown Disease"
    )
    description = models.TextField(
        verbose_name="Description",
        default="Detailed description about the disease."
    )
    image = ResizedImageField(
        size=[1600, 800],
        crop=["middle", "center"],
        default="default_image.jpg",
        upload_to="uploads/medicine/",
    )


    symptoms = models.JSONField(
        verbose_name="Symptoms",
        default=dict,
        help_text="Example: {'Fever': 'Common', 'Cough': 'Rare'}"
    )
    treatments = models.TextField(
        verbose_name="Treatments",
        default="Treatment methods or suggestions."
    )

    def __str__(self):
        return self.name
