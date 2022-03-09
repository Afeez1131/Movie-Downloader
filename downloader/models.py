from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=120)
    download_link = models.URLField()
    subtitle_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title