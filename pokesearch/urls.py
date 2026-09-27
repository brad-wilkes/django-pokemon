from django.urls import include, path
from rest_framework.routers import DefaultRouter

from pokesearch import views

router = DefaultRouter()
router.register('pokemon', views.PokemonViewSet, basename='pokemon')
router.register('types', views.TypeViewSet, basename='type')

urlpatterns = [
    path('', include(router.urls)),
]
