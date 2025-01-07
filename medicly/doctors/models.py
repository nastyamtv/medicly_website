from django.db import models
from datetime import date
from django_resized import ResizedImageField


class Doctor(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Name",
        default="Unknown Doctor"
    )
    birthday = models.DateField(
        verbose_name="Birthday",
        default="1980-01-01"
    )
    phone = models.CharField(
        max_length=15,
        verbose_name="Phone",
        default="+380999999999"
    )
    degree = models.CharField(
        max_length=255,
        verbose_name="Degree",
        default="General Practitioner"
    )
    email = models.EmailField(
        verbose_name="Email",
        default="unknown@doctor.com"
    )
    image = ResizedImageField(
        size=[1600, 800],
        crop=["middle", "center"],
        default="default_image.jpg",
        upload_to="uploads/medicine/",
    )


    patients = models.IntegerField(
        verbose_name="Number of Patients",
        default=0
    )
    projects = models.IntegerField(
        verbose_name="Number of Projects",
        default=0  #
    )
    hours_support = models.IntegerField(
        verbose_name="Hours of Support",
        default=0
    )
    experience_years = models.IntegerField(
        verbose_name="Years of Experience",
        default=0
    )
    skills = models.JSONField(
        verbose_name="Skills",
        default=dict,  # JSON-поле для скіла
        help_text="Example: {'Ophthalmologist': '100%', 'ENT Specialist': '90%'}"
    )

    @property
    def age(self):
        """Обчислює вік на основі дати народження."""
        today = date.today()
        return today.year - self.birthday.year - (
            (today.month, today.day) < (self.birthday.month, self.birthday.day)
        )

    def __str__(self):
        return self.name
