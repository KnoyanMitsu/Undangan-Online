from rest_framework import serializers
from dataKendaraan.models import Kendaraan

class KendaraanSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    no_polisi = serializers.CharField(max_length=10)
    warna = serializers.CharField(max_length=10)
    merk = serializers.CharField(max_length=20)
    type = serializers.CharField(max_length=50)
    jenis = serializers.CharField(max_length=20)
    tahun = serializers.DateField()
    pajak = serializers.IntegerField()
    release_date = serializers.DateTimeField()

    def create(self, validated_data):
        return Kendaraan.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.create = validated_data.get('create', instance.create)
        instance.no_polisi = validated_data.get('no_polisi', instance.no_polisi)
        instance.warna = validated_data.get('warna', instance.warna)
        instance.merk = validated_data.get('merk', instance.merk)
        instance.type = validated_data.get('type', instance.type)
        instance.jenis = validated_data.get('jenis', instance.jenis)
        instance.tahun = validated_data.get('tahun', instance.tahun)
        instance.pajak = validated_data.get('pajak', instance.pajak)
        instance.release_date = validated_data.get('release_date', instance.release_date)

        instance.save()
        return instance