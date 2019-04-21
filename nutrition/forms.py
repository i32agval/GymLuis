from django import forms
from .models import Food


class FoodForm(forms.ModelForm):
    """
    Form to show information about a food of our own database
    """
    class Meta:
        model = Food
        fields = ('food_category', 'name', 'protein', 'carbohidrate', 'fat')

    def __init__(self, *args, **kwargs):
        super(FoodForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Alimento'
        self.fields['food_category'].label = 'Tipo'


class RecipeForm(forms.Form):
    """
    Form to show information about a recipe of fatsecret API
    """
    recipe_type = forms.ChoiceField(label="Tipo de receta")
    recipe = forms.ChoiceField(label="Receta")

    def __init__(self, *args, **kwargs):
        recipe_type = kwargs.pop('instance', None)
        recipes_list = kwargs.pop('recipes', None)
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['recipe_type'].choices = recipe_type.items()
        self.fields['recipe'].choices = recipes_list.items()
