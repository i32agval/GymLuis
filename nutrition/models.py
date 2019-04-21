from django.db import models
from django.urls import reverse

# Create your models here.


class FoodCategory(models.Model):
    """
    Model representing a type of food of our own database
    """
    name = models.CharField(
        max_length=20,
        default='',
        help_text='Tipo de alimento')

    def __str__(self):
        return '%s' % self.name


class Food(models.Model):
    """
    Model representing a food of our own database
    """
    name = models.CharField(max_length=100, default='', unique=True)

    food_category = models.ForeignKey(
        'FoodCategory',
        on_delete=models.CASCADE,
        default='',
        max_length=50,
        verbose_name='Categoria',
        related_name='food_category_name')

    protein = models.IntegerField(default=0)
    carbohidrate = models.IntegerField(default=0)
    fat = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('nutrition')

    def __str__(self):
        return '%s' % self.name
