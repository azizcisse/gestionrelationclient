from django.urls import include, path
from . import views


urlpatterns = [
    path('/<str:pk>',views.list_client,name='client'),
]