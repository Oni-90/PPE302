from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from django.utils.translation import gettext_lazy as _
from .models import Organisation, Agent


#create our custom permission class here


#organisation permission class
class IsOrganisation(BasePermission):
    def has_permission(self, request, view):
        #verifying if the user is authenticated
        if not request.user or not request.user.is_authenticated:
            return False
        
        # verifying if the user is an instance of Organisation
        if not hasattr(request.user, 'organisation') or not isinstance(request.user.organisation, Organisation):
            return False
        
        # verifying if the token is valid for the Organisation
        token = self.get_token_from_request(request)
        if token:
            return self.verify_token(token, AccessToken)
        
        return False

    def get_token_from_request(self, request):
        # Extract the token from the Authorization header
        auth_header = request.headers.get('Authorization', None)
        if auth_header and auth_header.startswith('Bearer '):
            return auth_header.replace('Bearer ', '')
        return None

    def verify_token(self, token, token_class):
        try:
            # Validate the token
            token_class(token)
            return True
        except InvalidToken:
            return False

#agent permission class
class IsAgent(BasePermission):
    def has_permission(self, request, view):
        # verifying if the user is authenticated
        if not request.user or not request.user.is_authenticated:
            return False
        
        # verifying if the user is an instance of Agent
        if not isinstance(request.user, Agent):
            return False
        
        # Verifying if the token is valid for the Agent
        token = self.get_token_from_request(request)
        if token:
            return self.verify_token(token, AccessToken)
        
        return False

    def get_token_from_request(self, request):
        # Extract the token from the Authorization header
        auth_header = request.headers.get('Authorization', None)
        if auth_header and auth_header.startswith('Bearer '):
            return auth_header.replace('Bearer ', '')
        return None

    def verify_token(self, token, token_class):
        try:
            # Validate the token
            token_class(token)
            return True
        except InvalidToken:
            return False