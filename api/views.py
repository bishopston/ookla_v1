from rest_framework import generics
from fixed.models import Fixed
from .serializers import FixedSerializer, FixedCountrySerializer, FixedCountryAreaSerializer, FixedCountryAreaProviderSerializer, FixedCountryAreaPeriodSerializer

class FixedAPIView(generics.ListAPIView):
    queryset = Fixed.objects.all()[:10]
    serializer_class = FixedSerializer

class CountryView(generics.ListAPIView):
    serializer_class = FixedCountrySerializer

    def get_queryset(self):
        queryset = Fixed.objects.all()
        countries = queryset.values('country').order_by('country').distinct()
        serializer = FixedCountrySerializer(countries, many=True)
        return serializer.data
        
class CountryAreaView(generics.ListAPIView):
    serializer_class = FixedCountryAreaSerializer

    def get_queryset(self):
        queryset = Fixed.objects.all()
        country = self.request.query_params.get('country')
        #area = self.request.query_params.get('area')
        if country is not None:
            queryset = queryset.filter(country=country).order_by('area')
            areas = queryset.values('country', 'area').distinct()
            serializer = FixedCountryAreaSerializer(areas, many=True)
            return serializer.data
        else:
            queryset = Fixed.objects.none()
            return queryset
        
class CountryAreaProviderView(generics.ListAPIView):
    serializer_class = FixedCountryAreaProviderSerializer

    def get_queryset(self):
        queryset = Fixed.objects.all()
        country = self.request.query_params.get('country')
        area = self.request.query_params.get('area')
        if country is not None and area is not None:
            queryset = queryset.filter(country=country, area=area).order_by('provider_name')
            provider_names = queryset.values('country', 'area', 'provider_name').distinct()
            serializer = FixedCountryAreaProviderSerializer(provider_names, many=True)
            return serializer.data
        else:
            queryset = Fixed.objects.none()
            return queryset
        
class CountryAreaPeriodView(generics.ListAPIView):
    serializer_class = FixedCountryAreaPeriodSerializer

    def get_queryset(self):
        queryset = Fixed.objects.all()
        country = self.request.query_params.get('country')
        area = self.request.query_params.get('area')
        if country is not None and area is not None:
            queryset = queryset.filter(country=country, area=area).order_by('period')
            periods = queryset.values('country', 'area', 'period').distinct()
            for i in range(len(periods)):
                periods[i]['period'] = periods[i]['period'].strftime("%B %Y")
            serializer = FixedCountryAreaPeriodSerializer(periods, many=True)
            return serializer.data
        else:
            queryset = Fixed.objects.none()
            return queryset