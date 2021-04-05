from rest_framework.serializers import ModelSerializer

from user.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['uuid', 'username', 'first_name', 'last_name', 'created', 'modified']


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']

        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
