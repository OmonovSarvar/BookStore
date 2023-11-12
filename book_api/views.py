from django.core.mail import send_mail
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView
from django.contrib.auth.admin import User
from rest_framework import filters

from book_api.models import BookStoreModel, SubscribersModel
from book_api.serializers import BookStoreSerializer, UserSerializer, SubscribersSerializer
from book_store.settings import EMAIL_HOST_USER


class TenMinuteThrottling(UserRateThrottle):
    time = '10/min'


class ThreeMinuteThrottling(UserRateThrottle):
    time = '3/min'


class ShowAvailable(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BookStoreModel.objects.all()

    def get_queryset(self):
        return BookStoreModel.objects.all().filter(is_available=True)

    serializer_class = BookStoreSerializer
    throttle_classes = [ThreeMinuteThrottling]


class AllBooks(ListAPIView):
    permission_classes = [AllowAny]
    queryset = BookStoreModel.objects.all()
    serializer_class = BookStoreSerializer
    throttle_classes = [ThreeMinuteThrottling]


class SignUp(CreateAPIView):
    queryset = BookStoreModel.objects.all()
    serializer_class = UserSerializer
    throttle_classes = [TenMinuteThrottling]


Email = str


class Subscribe(APIView):
    """
    Subscribe view .
    """
    queryset = SubscribersModel.objects.all()
    serializer_class = SubscribersSerializer
    throttle_classes = [TenMinuteThrottling]

    def post(self, request):
        global Email
        serializer = SubscribersSerializer(data=request.data)
        response = SubscribersSerializer(data=request.data.get('email'))
        Email = response.initial_data
        to_mail = [Email]
        send_mail('Welcome New Subscriber',
                  'Assalomu alaykum xurmatli mijoz, siz bizni blog postlarimizga obuna bo’ldingiz va tez orada biz sizga eng yaxshi postlarimizni yuboramiz',
                  from_email=EMAIL_HOST_USER,
                  recipient_list=to_mail,
                  fail_silently=False
                  )
        print(f'Message sent to {Email}')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewBook(CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
    queryset = BookStoreModel.objects.all()
    serializer_class = BookStoreSerializer
    throttle_classes = [TenMinuteThrottling]


class BookInformation(RetrieveAPIView):
    queryset = BookStoreModel.objects.all()
    permission_classes = [IsAuthenticated]
    throttle_classes = [TenMinuteThrottling]
    serializer_class = BookStoreSerializer
    lookup_field = 'id'


class UpdateBookInformation(UpdateAPIView):
    queryset = BookStoreModel.objects.all()
    serializer_class = BookStoreSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]
    throttle_classes = [ThreeMinuteThrottling]


class DeleteBook(DestroyAPIView):
    queryset = BookStoreModel.objects.all()
    serializer_class = BookStoreSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]
    throttle_classes = [ThreeMinuteThrottling]


class PersonalInformation(ListAPIView):
    queryset = BookStoreModel
    serializer_class = BookStoreSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [TenMinuteThrottling]

    def get_queryset(self):
        user = self.request.user
        return BookStoreModel.objects.filter(user=user)


class BookTitleSearch(ListAPIView):
    queryset = BookStoreModel.objects.all()
    serializer_class = BookStoreSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    permission_classes = [AllowAny]
    throttle_classes = [TenMinuteThrottling]


class BookSort(ListAPIView):
    queryset = BookStoreModel.objects.all()
    serializer_class = BookStoreSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['title', 'category', 'ISO', 'published']
    search_fields = ['title']
    permission_classes = [AllowAny]
    throttle_classes = [TenMinuteThrottling]
