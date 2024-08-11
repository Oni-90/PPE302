from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views
from .views import AuthViewSet, OrganisationViewSet, AgentViewSet, OrganisationViewSet, CensusTypeViewSet, CensusViewSet, CensusFormViewSet, CensusDataViewSet, FieldViewSet, StatAgentViewSet, StatCensusViewSet


#defining our routes here


router = DefaultRouter()
router.register(r'auth', AuthViewSet, basename='auth')
router.register('organisations', OrganisationViewSet)
router.register('agents', AgentViewSet, basename='agent')
router.register('censusTypes', CensusTypeViewSet)
router.register('census', CensusViewSet)
router.register('censusForms', CensusFormViewSet)
router.register(r'censusData', CensusDataViewSet)
router.register('field', FieldViewSet)


#defining our urls here
urlpatterns = [
    path('', include(router.urls)),
    path('api/auth/token/', obtain_auth_token, name='api_token_auth'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('census-forms/<int:recensement_id>/', CensusFormViewSet.as_view({'get': 'list'}), name='census-form-list'),
    path('census-forms/<int:recensement_id>/<int:pk>/', CensusFormViewSet.as_view({'get': 'retrieve'}), name='census-form-detail'),

    path('stat/agent/', StatAgentViewSet.as_view({'get': 'count'}), name='stat-agent'),
    path('stat/census/', StatCensusViewSet.as_view({'get': 'count'}), name='stat-census'),




]
