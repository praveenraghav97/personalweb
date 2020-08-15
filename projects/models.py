from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200, null=False)
    description = models.TextField()
    img = models.ImageField(upload_to='pics/projects')

    def __str__(self):
        return self.title
