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


#comment model
class comment(models.Model):
    content = models.CharField(max_length=2000)
    author = models.CharField(max_length=150)
    date = models.DateTimeField()
    origin_post = models.ForeignKey(post, on_delete=models.CASCADE, related_name="comment_set")

    def __str__(self):
        return self.content[:5]+"..."