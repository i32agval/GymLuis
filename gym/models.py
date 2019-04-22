from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.urls import reverse


# Create your models here.


class UserProfile(models.Model):
    """
    Model representing aditional information of the user
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    profile_picture = models.ImageField(
        upload_to='media/images/', default='logo-gym.png',
        blank=True, null=True)
    followers = models.ManyToManyField(
        to='self', through='Relationship', related_name='related_to',
        symmetrical=False, blank=True)

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)


RELATIONSHIP_STATUSES = (
    (settings.RELATIONSHIP_FOLLOWING, 'Following'),
    (settings.RELATIONSHIP_BLOCKED, 'Blocked'),
)


class Relationship(models.Model):
    from_person = models.ForeignKey(
        UserProfile,
        related_name='from_people', on_delete=models.SET_NULL, null=True)
    to_person = models.ForeignKey(
        UserProfile,
        related_name='to_people', on_delete=models.SET_NULL, null=True)
    status = models.IntegerField(
        choices=RELATIONSHIP_STATUSES,
        null=True, default=settings.RELATIONSHIP_BLOCKED)
    accepted = models.BooleanField(default=False, null=True, )


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    if not instance.is_staff:
        instance.userprofile.save()


class WeightData(models.Model):
    """
    Model representing the user's weight on a certain date
    """
    user = models.ForeignKey(
        'UserProfile', on_delete=models.CASCADE, related_name='weight_data')
    date = models.DateField(default=timezone.now)
    weight = models.IntegerField()

    def __str__(self):
        return '%s' % self.user


class UserImages(models.Model):
    user = models.ForeignKey(
        'UserProfile', on_delete=models.CASCADE,
        related_name='user_images', blank=True, null=True)
    image = models.ImageField(upload_to='media/images/')
    date = models.DateField(default=timezone.now)
    weight = models.IntegerField()
    chest = models.IntegerField()
    biceps = models.IntegerField()
    waist = models.IntegerField()
    quadricep = models.IntegerField()
    gastrocnemius = models.IntegerField()
    muscle_mass = models.IntegerField()
    muscle_fat = models.IntegerField()

    def __unicode__(self,):
        return str(self.image)


class Machine(models.Model):
    """
    Model representing a machine
    """
    name = models.CharField(max_length=30)

    MUSCLE = (
        ('p', 'Pecho'),
        ('b', 'Biceps'),
        ('e', 'Espalda'),
        ('t', 'Triceps'),
        ('h', 'Hombros'),
        ('pi', 'Piernas'),
    )

    muscle_group = models.CharField(
        max_length=2, choices=MUSCLE, help_text='Grupo muscular')
    image = models.ImageField(default='gym.jpg')

    def __str__(self):
        return self.name


class Exercise(models.Model):
    """
    Model representing a exercise performed on a machine with a specific weight
    """
    user = models.ForeignKey(
        'UserProfile', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=30)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    weight = models.IntegerField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('machine', 'date')

    def get_absolute_url(self):
        return reverse('weights', kwargs={'pk': self.machine.id})
