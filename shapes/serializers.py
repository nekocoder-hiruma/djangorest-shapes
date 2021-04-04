from rest_framework.serializers import ModelSerializer

from shapes.models import Triangle, Rectangle, Square, Diamond


class TriangleSerializer(ModelSerializer):
    class Meta:
        model = Triangle
        fields = ['base', 'adjacent', 'opposite', 'name']


class RectangleSerializer(ModelSerializer):
    class Meta:
        model = Rectangle
        fields = ['width', 'length', 'name']


class SquareSerializer(ModelSerializer):
    class Meta:
        model = Square
        fields = ['side', 'name']


class DiamondSerializer(ModelSerializer):
    class Meta:
        model = Diamond
        fields = ['length', 'diagonal_one', 'diagonal_two', 'name']
