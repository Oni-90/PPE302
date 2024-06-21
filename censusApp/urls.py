from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthViewSet, OrganisationViewSet, AgentViewSet, OrganisationViewSet, CensusTypeViewSet, CensusViewSet, CensusFormViewSet, HousingCensusViewSet,PopulationCensusViewSet,AgriculturalCensusViewSet
router = DefaultRouter()
router.register(r'auth', AuthViewSet, basename='auth')
router.register('organisations', OrganisationViewSet)
router.register('agents', AgentViewSet)
router.register('censusTypes', CensusTypeViewSet)
router.register('census', CensusViewSet)
router.register('censusForms', CensusFormViewSet)
router.register('housingCensus', HousingCensusViewSet)
router.register('populationCensus', PopulationCensusViewSet)
router.register('agriculturalCensus', AgriculturalCensusViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
