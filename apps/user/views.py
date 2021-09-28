from drf_query_filter import fields
from rest_framework import viewsets

from .models import User
from .serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    model = User
    serializer_class = UserSerializer
    queryset = model.objects.all()

    query_params = [
        fields.Field('username', 'username__icontains')
    ]
