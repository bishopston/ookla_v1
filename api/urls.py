from django.urls import path
from .views import FixedAPIView, CountryView, CountryAreaView, CountryAreaProviderView, CountryAreaPeriodView

urlpatterns = [
    path("", FixedAPIView.as_view()),
    path("countries/", CountryView.as_view()),
    path("areas_per_country/", CountryAreaView.as_view()),
    path("providers_per_area/", CountryAreaProviderView.as_view()),
    path("periods_per_area/", CountryAreaPeriodView.as_view()),
]