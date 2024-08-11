from django.db import models
from django.contrib.auth.hashers import check_password, make_password
from simple_history.models import HistoricalRecords




# Model Organisation
class Organisation(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    nif = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    def check_password(self, raw_password):
        """
        check password for login 
        """
        return check_password(raw_password, self.password)

    def set_password(self, raw_password):
        """
        define password whit hash
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
    username = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    organisation = models.ForeignKey(Organisation, on_delete=models.SET_NULL, null=True,related_name='agents')
    state =models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()


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
    state =models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

#model Census
class Census(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='census')
    census_type = models.ForeignKey(CensusType, on_delete=models.CASCADE, related_name='censusForms')
    start_dDate = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=100)
    state =models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


#model CensusForm
class CensusForm(models.Model):
    organisation = models.ForeignKey(Organisation, related_name='censusForms',on_delete = models.CASCADE)
    census = models.ForeignKey(Census, related_name='censusForms',on_delete = models.CASCADE)
    name = models.CharField(max_length=50)
    state =models.BooleanField(default=False)
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


#model census report
class CensusReport(models.Model):
    object = models.CharField(max_length=255)
    content = models.TextField(max_length=5000)
    author = models.ForeignKey (Agent, on_delete=models.CASCADE, related_name='CensusReport')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
#model field
class Field(models.Model):
    Form_FILED_TYPES =[
        ('char','CharFied'),
        ('int','IntegerField'),
        ('date','DateField'),
        ('bool','BooleanField'),
    ]

    form = models.ForeignKey(CensusForm, related_name='fields',on_delete = models.CASCADE)
    label = models.CharField(max_length=50)
    field_type = models.CharField(max_length=10, choices=Form_FILED_TYPES)
    required = models.BooleanField(default=False)

    def __str__(self):
        return self.name


#model censusData
class CensusData(models.Model):
    census = models.ForeignKey(Census, related_name='censusData',on_delete = models.CASCADE)
    field = models.ForeignKey(Field, related_name='censusData',on_delete = models.CASCADE)
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['census','field'] #a field can't be repeated in a census
    
    def __str__(self):
        return f"Census {self.census.id} - {self.field.label}: {self.data}"


