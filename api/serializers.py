from rest_framework import serializers
from fixed.models import Fixed

class FixedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fixed
        fields = ('country', 'area', 'service', 'provider_name', 'provider_id', 'period', 'p25_download_mbps', 'p75_download_mbps')

    def to_representation(self, instance):
        representation = super(FixedSerializer, self).to_representation(instance)
        representation['period'] = (instance.period.strftime("%B") + ' ' + instance.period.strftime("%Y"))
        return representation
    
class FixedCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Fixed
        fields = ('country',)

class FixedCountryAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fixed
        fields = ('country', 'area')

class FixedCountryAreaProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fixed
        fields = ('country', 'area', 'provider_name')

class FixedCountryAreaPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fixed
        fields = ('country', 'area', 'period')