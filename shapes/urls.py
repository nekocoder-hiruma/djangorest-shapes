from django.urls import path, include

from shapes.api_views import ShapeAPIView

app_name = 'Shapes'

urlpatterns = [
    path('<str:shape_name>/', include([
        path('',
             ShapeAPIView.as_view({'post': 'create',
                                   'get': 'list'}),
             name='shape_api-create_list'),
        path('get/<str:shape_name>/',
             ShapeAPIView.as_view({'get': 'retrieve',
                                   'put': 'update',
                                   'delete': 'destroy'}),
             name='shape_api-detail'),
    ]))
]
