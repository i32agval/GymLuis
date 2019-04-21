from django.db import models
from django.utils import timezone

# Create your models here.


class Entry(models.Model):
    """
    Model representing an entry in the diary
    """
    author = models.ForeignKey(
        'gym.UserProfile', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateField(default=timezone.now())

    def __str__(self):
        return '%s' % self.author
