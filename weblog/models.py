from django.db import models
from django.shortcuts import reverse
class Blog(models.Model):
    STATUS_CHOICES = (
        ('pub', "published"),
        ('drf', "Draft"),
    )

    title = models.CharField(max_length=30)
    text = models.TextField()
    create_datetime = models.DateTimeField(auto_now_add=True)
    modified_datetime = models.DateTimeField(auto_now=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])