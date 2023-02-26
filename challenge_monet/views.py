from rest_framework import generics
from challenge_monet.serializers import UserSerializer
from django.contrib.auth.models import User


class UserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = []
