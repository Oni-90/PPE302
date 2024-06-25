from django.db import models
from django.contrib.auth.hashers import check_password, make_password


# Model Organisation
class Organisation(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def check_password(self, raw_password):
        """
        Vérifie si le mot de passe donné correspond au mot de passe enregistré dans la base de données.
        """
        return check_password(raw_password, self.password)

    def set_password(self, raw_password):
        """
        Définit le mot de passe pour l'organisation en utilisant un hachage sécurisé.
        """
        self.password = make_password(raw_password)
        self.save()

    def save(self, *args, **kwargs):
        # Hash the password if it's a plain password
        if not self.password.startswith('pbkdf2_'):
            self.set_password(self.password)
        super(Organisation, self).save(*args, **kwargs)


# Model Agent
class Agent(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=255)
   # organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, related_name='agents')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def save(self, *args, **kwargs):
        # Hash the password if it's a plain password
        if not self.password.startswith('pbkdf2_'):
            self.set_password(self.password)
        super(Agent, self).save(*args, **kwargs)

class OrganisationToken(models.Model):
    key = models.CharField(max_length=40, primary_key=True)
    organisation = models.OneToOneField(Organisation, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

class AgentToken(models.Model):
    key = models.CharField(max_length=40, primary_key=True)
    agent = models.OneToOneField(Agent, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)



#model CensusType
class CensusType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


#model Census
class Census(models.Model):
    start_dDate = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


#model CensusForm
class CensusForm(models.Model):
    census = models.ForeignKey(Census, on_delete=models.CASCADE, related_name='censusForms')
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='censusForms')
    collected_date = models.DateField()
    information = models.TextField()
    census_type = models.ForeignKey(CensusType, on_delete=models.CASCADE, related_name='censusForms')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


#model HousingCensus
class HousingCensus(CensusForm):
    housing_size =models.CharField(max_length=10)
    number_of_pieces = models.IntegerField()
    construction_type = models.CharField(max_length=50)
    public_service = models.CharField(max_length=100)
    household_number = models.IntegerField()
    household_relation  = models.CharField(max_length=30)


#model PopulationCensus
class PopulationCensus(CensusForm):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=30)
    sex = models.CharField(max_length=10)
    nationality = models.CharField(max_length=30)
    profession = models.CharField(max_length=30)
    marital_status = models.CharField(max_length=30)
    education_level = models.CharField(max_length=30)
    housing_type = models.CharField(max_length=30)
    are_you_owner = models.BooleanField()
    

#model AgriculturalCensus
class AgriculturalCensus(CensusForm):
    area_exploited = models.FloatField()
    production_method = models.CharField(max_length=30)
    number_of_workers = models.IntegerField()
    number_of_cattle = models.IntegerField()
    equipment_type = models.CharField(max_length=30)
    agricultural_income = models.FloatField()




