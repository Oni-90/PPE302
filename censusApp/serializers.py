from rest_framework import serializers
from datetime import datetime
from .models import AgentToken, CensusType, Organisation, Agent, Census, CensusForm,  OrganisationToken, CensusReport, Field, CensusData


#creating our serializers here


#Agent serializer
class AgentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agent
        fields = '__all__'
        

#organisation serializer
class OrganisationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organisation
        fields = '__all__'
  

#Census Type serializer
class CensusTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CensusType
        fields = '__all__'

#Census serializer
class CensusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Census
        fields = '__all__'


#census report serializer
class CensusReportSerializer(serializers.ModelSerializer):

    class Meta:
        Model = CensusReport
        fields = '__all__'
        read_only_field = ['author'] #Recuperation automatique du champ auteur


#field serializer
class FieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = Field
        fields = '__all__'
        extra_kwargs = {
            'form': {'write_only': True} #form field is write only it will not be displayed
        }


#Census form serializer
class CensusFormSerializer(serializers.ModelSerializer):

    field = FieldSerializer(many=True, read_only=True)

    class Meta:
        model = CensusForm
        fields = '__all__'


#census data serializer
class CensusDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = CensusData
        fields = '__all__'
    
    def validate(self, data):
        field = data.get('field')
        data = data.get('data')

         #validate data by field type
        if field.field_type == 'char' and not isinstance(data, str):
            raise serializers.ValidationError('Invalid value')
        
        elif field.field_type == 'int':
            try:
                float(data)
            except ValueError:
                raise serializers.ValidationError('Invalid value')  
            
        elif field.field_type == 'date':
            try:
                datetime.strptime(data, '%Y-%m-%d')
            except ValueError:
                raise serializers.ValidationError('Invalid value')
            
        elif field.field_type == 'bool' and not isinstance(data, bool):
            raise serializers.ValidationError('Invalid value')
        
        return data
    

#Agent login serializer
class AgentLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agent
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    #login data validation
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            raise serializers.ValidationError("Both username and password are required.") #return error if data is incorrect
        
        return data
    

#Organisation login serializer
class OrganisationLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organisation
        fields = ['name', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    #login date validation
    def validate(self, data):
        name = data.get('name')
        password = data.get('password')

        if not name or not password:
            raise serializers.ValidationError("Both name and password are required.") #return error if data is not valid or aren't provide
        
        return data
    

#Agent token generation serializer
class AgentTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentToken
        fields = ['key', 'agent', 'created']

#Organoisation token generation serializer
class OrganisationTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganisationToken
        fields = ['key', 'organisation', 'created']


