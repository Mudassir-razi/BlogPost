from django.db import models

# Create your models here.


#post model
class post(models.Model):
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=2000)
    writer = models.CharField(max_length=150)
    date = models.DateTimeField()

    def __str__(self):
        return self.title
