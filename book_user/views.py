from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView

from book_user.serializers import LoginSerializer


class ThreeMinuteThrottling(UserRateThrottle):
    time = '3/min'


# Create your views here.
class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)
    throttle_classes = [ThreeMinuteThrottling]

    def post(self, request):
        serializer = LoginSerializer(data=self.request.data,
                                     context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response('You logged in')
