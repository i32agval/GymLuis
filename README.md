GymLuis
Web application to save and share your progress in the gym

Is proveed a requeriments.txt file that you must use to install the dependences: pip install -r requirements.txt

Features:

API
===
You can:
  Obtain information from the Fatsecret API. You can visualize the recipes in the API, search by category and name of recipe.
  Obtain information from the Weathermap API. You can visualize the weather of today and the weather of the next 5 days.
Creation of an API to obtain all users registered in the platform, accessing api/v1.

*Each information provided by the user can be edited and deleted.
*Use of generic views (ListView, DetailView and DeleteView) in some cases.
*Use of decorators to control that the user is registered in the platform before accesing some views.
*Use of template inheritance. Base_generic.html is the base template, from which the others inherit.
*Use of templatetags for use a function in the templates.
*Message system after performing actions on the platform, using django.contrig.messages.
*CSS and Javascript

Machines
========
Machine display.
Register the weights used in the different machines of the gym.
Display all weights used in each machine.
  
User information
================
You can register in the platform, as well as edit your profile.
You can visualize your user profile.
You can upload a profile picture.

Diary
=====
You can write information of your day to day in the gym.
You can visualize, edit and delete diary entries.

Nutrition
=========
You can obtain information from the Fatsecret API. You can visualize the recipes in the API, search by category and name of recipe.
The platform allows you to create your own food database.
Create, edit and delete a food.
Use of Javascript to show the recipe/food when you select a category in the select field.
Use of Javascript to show automaticaly the recipe or the food information when you select a recipe/food y the select field. 

Weather
=======
You can obtain information from the Weathermap API.
You can visualize the weather of today and the weather of the next 5 days, showing the date, description and an image of the weather.

Progress
========
You can visualize your progress in graphs (weights used in the machines and your own weight)
Use of Matplotlib for generate the graphs.

My photos
=========
Each user can upload photos of their progress and provide information on their weight and measurements.
You can see all your photos uploaded and keep track of your evolution.
You can edit or delete a photo (with it information).

Social network
==============
You can search users registered in the platform and send a friend request. If the other user accepts the request, you can both see your progress (photos and measures).
You can visualize your friends (users that has been accepted your invitation or vice versa) and see their photos (and they yours).
You can add or delete a friend.
When an user sends a request, the user who receives it will see a message on the main screen, indicating that he has new requests. The user can add or delete the friend.




