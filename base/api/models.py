from django.db import models
class UploadModel(models.Model):
    title = models.CharField(max_length=100, blank=True)
    caption = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='samples')

    def __str__(self):
        if self.title:
            return self.title
        return str(self.image)

