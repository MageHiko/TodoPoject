from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class WorkModel(models.Model):
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    image = models.ImageField(upload_to = "work_images/", blank=True, null=True)

    class Meta:
        verbose_name = "Work"
        verbose_name_plural = "Works"
        ordering = ("-id",)
    
    def __str__(self) -> str:
        return self.name
