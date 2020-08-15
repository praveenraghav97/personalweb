from django.db import models

# Create your models here.


class Blog(models.Model):
    category = models.CharField(max_length=200, null=False)
    posted_on = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, null=False)
    title = models.CharField(max_length=500, null=False)
    text = models.TextField(null=False)

    def __str__(self):
        return self.title


