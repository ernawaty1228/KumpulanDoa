from rest_framework import serializers
from .models import Doa

class DoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doa
        fields = ['id', 'judul', 'arab', 'arti', 'kategori', 'tanggal_dibuat']
        read_only_fields = ['id', 'tanggal_dibuat']
