from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from nutrition import views

urlpatterns = [
    url(r'^nutrition/$',
        login_required(views.nutrition),
        name='nutrition'),

    url(r'^food-list/$',
        login_required(views.FoodListView.as_view()),
        name='food-list'),

    url(r'^create-food/$',
        login_required(views.FoodCreateView.as_view()),
        name='create-food'),

    url(r'^food-delete/(?P<pk>\d+)/$',
        login_required(views.FoodDeleteView.as_view()),
        name='food-delete'),

    url(r'^food-update/(?P<pk>\d+)/$',
        login_required(views.FoodUpdateView.as_view()),
        name='food-update'),

    url(r'^ajax/load-foods/$',
        login_required(views.load_foods),
        name='ajax-load-foods'),

    url(r'^ajax/load-recipes/$',
        login_required(views.load_recipes),
        name='ajax-load-recipes'),

    url(r'^ajax/load-recipes-table/$',
        login_required(views.load_recipes_table),
        name='ajax-load-recipesTable'),

    url(r'^ajax/load-nutrients/$',
        login_required(views.load_nutrients),
        name='ajax-load-nutrients'),

    url(r'^recipe/$',
        login_required(views.recipe_data),
        name='recipe-data'),
]
