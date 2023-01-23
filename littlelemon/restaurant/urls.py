from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('menu/', views.MenuItemView.as_view()),
    path('menu/, <int:pk>', views.SingleMenuItemSerializer.as_view()),
    path('api-token-auth/', obtain_auth_token),
]
