from rest_framework import serializers
from .models import Donor

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Donor
        fields="__all__"

class DelDonorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Donor
        fields=["donor_id"]