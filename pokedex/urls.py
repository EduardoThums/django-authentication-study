from pokedex import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.PokedexViewSet, basename='pokedex')

pokedex_urlpatterns = router.urls
