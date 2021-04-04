from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from user.models import User
from user.serializers import UserSerializer, UserCreateSerializer


class UserAPIView(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = User.objects.filter(is_active=True)
    lookup_field = 'uuid'
    lookup_url_kwarg = 'user_uuid'
    pagination_class = PageNumberPagination
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'update':
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return UserCreateSerializer
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user, token = self.perform_create(serializer)
        public_serializer = UserSerializer(user, many=False)
        headers = self.get_success_headers(public_serializer.data)
        response_data = {
            'user': public_serializer.data,
            'token': token
        }
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return user, token.key

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()

    def perform_update(self, serializer):
        user = serializer.save()
        return user

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        user = self.perform_update(serializer)

        public_serializer = UserSerializer(user, many=False)
        return Response(public_serializer.data, status=status.HTTP_200_OK)
