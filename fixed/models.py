from django.db import models

class Fixed(models.Model):

    country = models.CharField(max_length=50)
    area = models.CharField(max_length=100)
    service = models.CharField(max_length=6)
    provider_name = models.CharField(max_length=50)
    provider_id = models.IntegerField()
    period = models.DateTimeField()
    p25_download_mbps = models.DecimalField(max_digits=7, decimal_places=2)
    p75_download_mbps = models.DecimalField(max_digits=7, decimal_places=2)
