from rest_framework import serializers
from .models import CensusType, Organisation, Agent, Census, CensusForm, HousingCensus, PopulationCensus,AgriculturalCensus

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
        fields = ['username', 'password']  # Spécifiez les champs que vous voulez utiliser pour le login
        extra_kwargs = {
            'password': {'write_only': True}  # Optionnel : Marque le champ "password" comme "write-only"
        }

class OrganisationLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = ['name', 'password']  # Spécifiez les champs que vous voulez utiliser pour le login
        extra_kwargs = {
            'password': {'write_only': True}  # Optionnel : Marque le champ "password" comme "write-only"
        }

