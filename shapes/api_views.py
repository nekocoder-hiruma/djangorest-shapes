from rest_framework import exceptions
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from shapes.models import Triangle, Rectangle, Square, Diamond
from shapes.serializers import TriangleSerializer, RectangleSerializer, SquareSerializer, DiamondSerializer


class ShapeAPIView(ModelViewSet):
    permission_classes = [AllowAny]
    pagination_class = PageNumberPagination
    shape_name: str
    lookup_url_kwarg = 'shape_name'
    lookup_field = 'name'

    def check_permissions(self, request):
        super().check_permissions(request)
        self.shape_name = self.kwargs.get('shape_name').lower()
        if self.shape_name not in ['triangle', 'rectangle', 'square', 'diamond']:
            raise exceptions.PermissionDenied("Invalid shape, please check again.")

    def get_serializer_class(self):
        if self.shape_name == 'triangle':
            self.serializer_class = TriangleSerializer
        elif self.shape_name == 'rectangle':
            self.serializer_class = RectangleSerializer
        elif self.shape_name == 'square':
            self.serializer_class = SquareSerializer
        else:
            self.serializer_class = DiamondSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        if self.shape_name == 'triangle':
            self.queryset = Triangle.objects.all()
        elif self.shape_name == 'rectangle':
            self.queryset = Rectangle.objects.all()
        elif self.shape_name == 'square':
            self.queryset = Square.objects.all()
        else:
            self.queryset = Diamond.objects.all()
        return super().get_queryset()
