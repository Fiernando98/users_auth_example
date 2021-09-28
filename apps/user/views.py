from drf_query_filter import fields
from knox.views import LoginView
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication

from .models import User
from .serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    model = User
    serializer_class = UserSerializer
    queryset = model.objects.all()

    query_params = [
        fields.Field('username', 'username__icontains')
    ]


# Create your views here.
class LoginCustomView(LoginView):
    """
    This only overrides the original View for using the Basic Authentication instead of the
    default one
    """
    authentication_classes = (BasicAuthentication,)
