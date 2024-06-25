from rest_framework import serializers
from .models import AgentToken, CensusType, Organisation, Agent, Census, CensusForm, HousingCensus, OrganisationToken, PopulationCensus,AgriculturalCensus

#creating my serializers

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'

class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = '__all__'

class CensusTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CensusType
        fields = '__all__'

class CensusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Census
        fields = '__all__'

class CensusFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = CensusForm
        fields = '__all__'

class HousingCensusSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousingCensus
        fields = '__all__'

class PopulationCensusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopulationCensus
        fields = '__all__'

class AgriculturalCensusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgriculturalCensus
        fields = '__all__'


class AgentLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            raise serializers.ValidationError("Both username and password are required.")
        
        return data

class OrganisationLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = ['name', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        name = data.get('name')
        password = data.get('password')

        if not name or not password:
            raise serializers.ValidationError("Both name and password are required.")
        
        return data

class AgentTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentToken
        fields = ['key', 'agent', 'created']

class OrganisationTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganisationToken
        fields = ['key', 'organisation', 'created']
