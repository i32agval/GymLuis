from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.UserViewSet, base_name='users')
urlpatterns = router.urls
