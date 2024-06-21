# from django.shortcuts import render

from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .permission import IsOrganisation, IsAgent, IsAdmin
from .models import CensusType, Organisation, Agent, Census, CensusForm, HousingCensus, PopulationCensus,AgriculturalCensus
from .serializers import CensusTypeSerializer, OrganisationSerializer, AgentSerializer, CensusSerializer, CensusFormSerializer, HousingCensusSerializer, PopulationCensusSerializer, AgriculturalCensusSerializer,AgentLoginSerializer,OrganisationLoginSerializer


# Create your views here.

#viewset for Agent
class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    permission_classes = [IsOrganisation]


#viewset for Organisation
class OrganisationViewSet(viewsets.ModelViewSet):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer
    # permission_classes = [IsAdmin]


#viewset for CensusType
class CensusTypeViewSet(viewsets.ModelViewSet):
    queryset = CensusType.objects.all()
    serializer_class = CensusTypeSerializer
    permission_classes = [IsAgent,IsOrganisation]


#viewset for Census
class CensusViewSet(viewsets.ModelViewSet):
    queryset = Census.objects.all()
    serializer_class = CensusSerializer
    permission_classes = [IsAgent,IsOrganisation]


#viewset for CensusForm
class CensusFormViewSet(viewsets.ModelViewSet):
    queryset = CensusForm.objects.all()
    serializer_class = CensusFormSerializer
    permission_classes = [IsAgent,IsOrganisation]


#viewset for HousingCensus
class HousingCensusViewSet(viewsets.ModelViewSet):
    queryset = HousingCensus.objects.all()
    serializer_class = HousingCensusSerializer
    permission_classes = [IsAgent,IsOrganisation]


#viewset for PopulationCensus
class PopulationCensusViewSet(viewsets.ModelViewSet):
    queryset = PopulationCensus.objects.all()
    serializer_class = PopulationCensusSerializer
    permission_classes = [IsAgent,IsOrganisation]


#viewset for AgriculturalCensus
class AgriculturalCensusViewSet(viewsets.ModelViewSet):
    queryset = AgriculturalCensus.objects.all()
    serializer_class = AgriculturalCensusSerializer
    permission_classes = [IsAgent,IsOrganisation]


class AuthViewSet(viewsets.GenericViewSet):

    def get_serializer_class(self):
        if self.action == 'agent_login':
            return AgentLoginSerializer
        elif self.action == 'organisation_login':
            return OrganisationLoginSerializer
        return super().get_serializer_class()

    @action(detail=False, methods=['post'])
    def agent_login(self, request):
        username = request.data.get('username')  # Corrigé "usename" en "username"
        password = request.data.get('password')

        # Authentification de l'agent
        agent = Agent.objects.filter(username=username).first()
        if agent and agent.check_password(password):
            serializer = self.get_serializer(agent)  # Utiliser self.get_serializer() pour obtenir le sérialiseur
            return Response(serializer.data)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['post'])
    def organisation_login(self, request):
        name = request.data.get('name')
        password = request.data.get('password')

        # Authentification de l'organisation
        organisation = Organisation.objects.filter(name=name).first()
        if organisation and organisation.check_password(password):
            serializer = self.get_serializer(organisation)  # Utiliser self.get_serializer() pour obtenir le sérialiseur
            return Response(serializer.data)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)