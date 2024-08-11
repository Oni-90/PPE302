from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .permission import IsOrganisation, IsAgent
from rest_framework_simplejwt.tokens import RefreshToken
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from .models import AgentToken, CensusType, Organisation, Agent, Census, CensusForm, OrganisationToken, CensusReport, CensusData, Field
from .serializers import AgentTokenSerializer, CensusTypeSerializer, OrganisationSerializer, AgentSerializer, CensusSerializer, CensusFormSerializer, OrganisationTokenSerializer,AgentLoginSerializer,OrganisationLoginSerializer,CensusReportSerializer,CensusDataSerializer,FieldSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


# Creating ours views here.


#viewset for Agent
class AgentViewSet(viewsets.ModelViewSet):

    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # extract the username and email from the request data
        data = request.data
        username = data.get('username')
        email = data.get('email')

        # verify if the agent already exists
        if Agent.objects.filter(username=username, email=email).exists():
            return Response({'detail': 'Agent already exists.'}, status=status.HTTP_400_BAD_REQUEST)
       
         # else create a new user mapped with the agent username as the username
        User.objects.create_user(
            username=request.data['username'],  
            password=request.data['password'],  
            email= request.data['email'],  
            first_name=request.data['firstname'],
            last_name=request.data['lastname'],
            is_active = request.data['state'],
            is_staff=False,
        )
        # and create the agent
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        # extract the username and email from the request data
        data = request.data
        username = data.get('username')
        email = data.get('email')

        # verify if the agent exists before updating
        if Agent.objects.filter(id=kwargs.get('pk')).exists():
            return Response({'detail': 'Agent does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # else update the agent
        return super().update(request, *args, **kwargs)


#viewset for Organisation
class OrganisationViewSet(viewsets.ModelViewSet):

    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer

    def create(self, request, *args, **kwargs):
        # extract the name from the request data
        data = request.data
        name = data.get('name')

        # verify if the organisation already exists
        if Organisation.objects.filter(name=name).exists():
            return Response({'detail': 'Organisation already exists.'}, status=status.HTTP_400_BAD_REQUEST) #trhow an error if the organisation already exists
        
        # else create a new user mapped with the organisation name as the username
        User.objects.create_user(
            username = request.data['name'],  
            password = request.data['password'],  
            email = request.data['email'],  
            is_staff=True,
        )
        # and create the organisation
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        # extract the name from the request data
        data = request.data
        name = data.get('name')

        # verify if the organisation exists before updating
        if Organisation.objects.filter(id=kwargs.get('pk')).exists():
            return Response({'detail': 'Organisation does not exist.'}, status=status.HTTP_400_BAD_REQUEST) #throw an error if the organisation does not exist
        
        # else update the organisation
        return super().update(request, *args, **kwargs)


#viewset for CensusType
class CensusTypeViewSet(viewsets.ModelViewSet):

    queryset = CensusType.objects.all()
    serializer_class = CensusTypeSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # extract the name from the request data
        data = request.data
        name = data.get('name')

        # verify if the census type already exists
        if CensusType.objects.filter(name=name).exists():
            return Response({'detail': 'Census type already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # else create the census type
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        # extract the name from the request data
        data = request.data
        name = data.get('name')

        # verify if the census type exists before updating
        if CensusType.objects.filter(id=kwargs.get('pk')).exists():
            return Response({'detail': 'Census type does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # else update the census type
        return super().update(request, *args, **kwargs)


#viewset for Census
class CensusViewSet(viewsets.ModelViewSet):

    queryset = Census.objects.all()
    serializer_class = CensusSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # extract the name from the request data
        data = request.data
        name = data.get('name')

        # verify if the census already exists
        if Census.objects.filter(name=name).exists():
            return Response({'detail': 'Census already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # else create the census
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        # extract the name from the request data
        data = request.data
        name = data.get('name')

        # verify if the census exists before updating
        if Census.objects.filter(id=kwargs.get('pk')).exists():
            return Response({'detail': 'Census does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # else update the census
        return super().update(request, *args, **kwargs)


#viewset for CensusForm
class CensusFormViewSet(viewsets.ModelViewSet):

    serializer_class = CensusFormSerializer
    queryset = CensusForm.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        recensement_id = self.kwargs.get('recensement_id')
        if recensement_id:
            return CensusForm.objects.filter(census_id=recensement_id)
        return CensusForm.objects.all()
    
    def create(self, request, *args, **kwargs):
        # extract the name from the request data
        data = request.data
        # name = data.get('name')
        recensement_id = data.get('census_id')
        
        #verify if the census form already exists
        if CensusForm.objects.filter(census_id=recensement_id).exists():
            return Response({'detail': 'Census form already exists.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # else create the census form
        return super().create(request, *args, **kwargs)   
    
    def update(self, request, *args, **kwargs):
        # extract the name from the request data
        data = request.data
        name = data.get('name')

        # verify if the census form exists before updating
        if CensusForm.objects.filter(id=kwargs.get('pk')).exists():
            return Response({'detail': 'Census form does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # else update the census form
        return super().update(request, *args, **kwargs)
    

#viewset for censusReport
class CemsusReportViewSet(viewsets.ModelViewSet):

    queryset = CensusReport.objects.all()
    serializer_class = CensusReportSerializer
    permission_classes = [IsAuthenticated] 


#function to filter data
class CensusDataFilter(filters.FilterSet):

    field = filters.ModelChoiceFilter(queryset=Field.objects.all())
    data = filters.CharFilter(lookup_expr='icontains')  #seach data sensitive

    class Meta:
        model = CensusData
        fields = ['field', 'data']


#viewset for census data
class CensusDataViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = CensusData.objects.all()
    serializer_class = CensusDataSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = CensusDataFilter

    def perform_create(self, request,*args,**kwargs):
        serializers = self.get_serializer(data=request.data)
        try:
            serializers.is_valid(raise_exception=True)
            self.perform_create(serializers)
            headers = self.get_success_headers(serializers.data)
            return Response(serializers.data, status=status.HTTP_201_CREATED, headers=headers)
        
        except serializers.ValidationError as e:
            return Response({'message': e.detail}, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):

        return super().get_queryset()
    

#View set for field 
class FieldViewSet(viewsets.ModelViewSet):

    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class AuthViewSet(viewsets.GenericViewSet):

    def get_serializer_class(self):
        if self.action == 'agent_login':
            return AgentLoginSerializer
        elif self.action == 'organisation_login':
            return OrganisationLoginSerializer
        return super().get_serializer_class()

    @action(detail=False, methods=['post'])
    def agent_login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        # verify the account matching in db and generate token key for agent
        agent = Agent.objects.filter(username=username).first()
        if agent and agent.check_password(password):
            try:
                #ensure that the user exists and is associated with this agent
                user = User.objects.get(username=agent.username)
            except User.DoesNotExist:
                return Response({'message': 'Invalid credential'}, status=status.HTTP_401_UNAUTHORIZED)
            
            # generate the JWT tokens
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['post'])
    def organisation_login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data['name']
        password = serializer.validated_data['password']

        # veify the account matching in db and generate token key for organisation
        organisation = Organisation.objects.filter(name=name).first()
        if organisation and organisation.check_password(password):
            try:
                # ensure that the user exists and is associated with this organisation
                user = User.objects.get(username=organisation.name)
            except User.DoesNotExist:
                return Response({'message': 'Invalid credential'}, status=status.HTTP_401_UNAUTHORIZED)

            # generate the JWT tokens
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'success',
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            

#view set for agent statistics
class StatAgentViewSet(viewsets.ViewSet):

    def count(self, request):
        total_agent = Agent.objects.count()
        actif_agent = Agent.objects.filter(state=True).count()
        data = {
            'total_agent': total_agent,
            'actif_agent': actif_agent
        }
        return Response(data, status=status.HTTP_200_OK)


#view set for census statistics
class StatCensusViewSet(viewsets.ViewSet):

    def count(self, request):
        totalCensus = Census.objects.count()
        actifCensus = Census.objects.filter(state=True).count()
        data = {
           'total': totalCensus,
            'actif': actifCensus
        }
        return Response(data , status=status.HTTP_200_OK)
     
