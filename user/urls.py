from django.urls import path

from user.api_views import UserAPIView

app_name = 'User'

urlpatterns = [
    path('', UserAPIView.as_view({'get': 'list'}),
         name='user-list'),
    path('register/', UserAPIView.as_view({'post': 'create'}),
         name='user-register'),
    path('<user_uuid>/', UserAPIView.as_view({'get': 'retrieve',
                                              'put': 'update'}),
         name='user-detail')
]
