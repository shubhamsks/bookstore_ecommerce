from django.urls import path
from .views import OrderPageView, charge
urlpatterns = [
	path('charge/', charge, name = 'charge'),
	path('',OrderPageView.as_view(), name='orders'),
]