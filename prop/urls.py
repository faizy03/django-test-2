from django.urls import path
from . import views


urlpatterns = [
    path('property/', views.PropertyAPIView.as_view(), name='property'),
    path('propdetails/<int:id>', views.PropertyDetails.as_view(), name="propdetails"),

    path('buyaproperty/', views.PropertyAPIView.as_view(), name='buyaproperty'),
    path('buypropdetails/<int:id>', views.PropertyDetails.as_view(), name="buypropdetails")
]