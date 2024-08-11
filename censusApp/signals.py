from django.db.models.signals import post_delete,post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Organisation, Agent

User = get_user_model()

#delete user when an Organisation is deleted
@receiver(post_delete, sender=Organisation)
def delete_user_organisation(sender, instance, **kwargs):
    try:
        user = User.objects.get(email=instance.email)
        user.delete()
       
    except User.DoesNotExist:
        pass

#delete user when an Agent is deleted
@receiver(post_delete, sender=Agent)
def delete_user_agent(sender, instance, **kwargs):
    try:
        user = User.objects.get(email=instance.email)
        user.delete()
    except User.DoesNotExist:
        pass

#update user when an Organisation is updated
@receiver(post_save, sender=Organisation)
def update_user_organisation(sender, instance, **kwargs):
    try:
        user = User.objects.get(email=instance.email)
        user.email = instance.email
        user.password = instance.password
        user.save()
    except User.DoesNotExist:
        pass