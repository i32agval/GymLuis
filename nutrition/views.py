from .models import Food
from .forms import FoodForm, RecipeForm

from django.conf import settings
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views import generic
from django.urls import reverse

from fatsecret import Fatsecret

# Create your views here.


def nutrition(request):
    """
    View to the index of nutrition
    """
    return render(request, 'nutrition/index_nutrition.html')


class FoodListView(generic.FormView):
    """
    Generic view to list our own food list
    """
    form_class = FoodForm
    template_name = 'nutrition/food_list.html'


class FoodCreateView(SuccessMessageMixin, generic.CreateView):
    """
    Generic view to create a new food in our own database
    """
    form_class = FoodForm
    template_name = 'nutrition/create_food.html'
    success_message = 'Alimento añadido correctamente'


class FoodUpdateView(SuccessMessageMixin, generic.UpdateView):
    """
    Generic view to delete a image
    """
    model = Food
    fields = '__all__'
    context_object_name = 'food'
    success_message = 'Alimento actualizado correctamente'

    def get_success_url(self):
        return reverse('food-list')


class FoodDeleteView(SuccessMessageMixin, generic.DeleteView):
    """
    Generic view to delete a image
    """
    model = Food
    context_object_name = 'food'
    success_message = 'Alimento eliminado correctamente'

    def delete(self, request, *args, **kwargs):
        messages.error(self.request, self.success_message)
        return super(FoodDeleteView, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('food-list')


def load_foods(request):
    """
    Required for ajax to show dynamically foods when select a category
    """
    food_category_id = request.GET.get('food_category')
    foods = Food.objects.filter(food_category_id=food_category_id)
    return render(
        request, 'nutrition/food_dropdown_list_options.html', {'foods': foods})


def load_recipes(request):
    """
    Required for ajax to show dynamically recipes when select a type
    """
    fs = Fatsecret(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)

    recipe_type = fs.recipe_types_get().get('recipe_type')
    recipe_type2 = int(request.GET.get('recipe_type'))
    recipe_type_number = []

    [recipe_type_number.append(x) for x in range(len(recipe_type))]
    recipe_type = dict(zip(recipe_type_number, recipe_type))
    for x in recipe_type:
        if x == recipe_type2:
            recipe_type = recipe_type[x]

    recipes = fs.recipes_search(
        search_expression='', recipe_type=recipe_type)
    recipes_list = []

    cont = 0
    for x in range(len(recipes)):
        recipes_list.append(recipes[x]['recipe_id'])
        cont = cont + 1

    cont = 0
    for x in recipes:
        recipes[cont] = recipes[cont]['recipe_name']
        cont = cont + 1

    recipes = dict(zip(recipes_list, recipes))

    return render(
        request, 'nutrition/recipe_dropdown_list_options.html', {
            'recipes': recipes})


def load_nutrients(request):
    """
    Required for ajax to show dynamically nutrients when select a food
    """
    food_id = request.GET.get('food')
    food = Food.objects.get(id=food_id)

    return render(
        request,
        'nutrition/food_nutrients.html', {'food': food})


def load_recipes_table(request):
    """
    Required for ajax to show dynamically recipes info when select a recipe
    """
    fs = Fatsecret(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
    recipe = request.GET.get('recipe')
    url_image = ''
    recipe_info = fs.recipe_get(recipe)
    ingredients = recipe_info['ingredients']
    ingredients = ingredients['ingredient']
    ingredients_list = []
    cooking_time_min = recipe_info.get('cooking_time_min')
    for x in ingredients:
        ingredients_list.append(x.get('ingredient_description'))

    image = recipe_info.get('recipe_images', '')
    if image:
        url_image = image.get('recipe_image')
    direction = recipe_info.get('directions')
    direction_list = direction['direction']
    cont = 0
    description = []
    if direction:
        for x in direction_list:
            try:
                description.append(
                    direction['direction']['direction_description'])
                break
            except:
                description.append(direction['direction'][cont].get(
                    'direction_description'))
            cont = cont + 1
    else:
        description = ''

    nutrients = recipe_info['serving_sizes']
    nutrients = nutrients.get('serving')
    return render(
        request, 'nutrition/recipes_table.html', {
            'url_image': url_image, 'description': description,
            'nutrients': nutrients, 'ingredients_list': ingredients_list,
            'cooking_time_min': cooking_time_min})


def recipe_data(request):
    """
    Access to Fatsecret API to obtain info for the recipe
    """
    fs = Fatsecret(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
    recipe_type = fs.recipe_types_get().get('recipe_type')
    recipe = fs.recipes_search(search_expression='', recipe_type='lunch')
    recipes_list = []
    [recipes_list.append(x['recipe_name']) for x in recipe]
    recipes_number = []
    [recipes_number.append(x) for x in range(len(recipes_list))]
    recipes_list = dict(zip(recipes_number, recipes_list))
    recipes_type_number = []
    [recipes_type_number.append(x) for x in range(len(recipe_type))]
    recipe_type = dict(zip(recipes_list, recipe_type))

    form = RecipeForm(instance=recipe_type, recipes=recipes_list)

    messages.info(
        request, 'Lista de recetas de la API Fatsecret')

    return render(
        request, 'nutrition/recipe_data.html', {
            'recipe_type': recipe_type, 'form': form})
