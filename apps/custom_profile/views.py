from drf_query_filter import fields
from rest_framework import viewsets

from .models import CustomProfile
from .serializer import CustomProfileSerializer


class CustomProfileViewSet(viewsets.ModelViewSet):
    model = CustomProfile
    serializer_class = CustomProfileSerializer
    queryset = model.objects.all()

    query_params = []
