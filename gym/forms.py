from django import forms
from .models import Exercise, UserImages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ExerciseForm(forms.ModelForm):
    """
    Form to a new exercise
    """

    class Meta:
        model = Exercise
        fields = ['user', 'name', 'machine', 'date', 'weight']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.inst = kwargs.pop('instance', None)
        self.machine = kwargs.pop('maquina', None)
        super(ExerciseForm, self).__init__(*args, **kwargs)
        self.fields['user'].disabled = True
        self.initial['user'] = self.inst
        self.initial['machine'] = self.machine


class SignUpForm(UserCreationForm):
    """
    Form to signup in the application
    """
    first_name = forms.TextInput()
    last_name = forms.TextInput()
    birthdate = forms.DateField()
    city = forms.ChoiceField()
    profile_picture = forms.ImageField()

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name',
            'birthdate', 'city', 'profile_picture', 'password1', 'password2', )

    def __init__(self, *args, **kwargs):
        self.cities = kwargs.pop('cities', None)
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['city'].choices = self.cities
        self.fields['profile_picture'].required = False
        self.fields['profile_picture'].initial = '/media/images/logo-gym.png'
        self.fields['birthdate'].input_formats = ['%d/%m/%Y']


class UploadImageForm(forms.ModelForm):
    """
    Form to upload a new image and new measures for an user
    """

    class Meta:
        model = UserImages
        fields = [
            'user', 'image', 'date', 'weight', 'chest',
            'biceps', 'waist', 'quadricep', 'gastrocnemius',
            'muscle_mass', 'muscle_fat']

    def __init__(self, *args, **kwargs):
        self.inst = kwargs.pop('instance', None)
        super(UploadImageForm, self).__init__(*args, **kwargs)
        self.fields['user'].disabled = True
        self.initial['user'] = self.inst
