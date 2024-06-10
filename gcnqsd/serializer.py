from rest_framework import serializers

from gcnqsd.models import *


class FolderFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FolderFileModel
        fields = '__all__'


class CaNhan_HoGiaDinhSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaNhan_HoGiaDinh
        fields = '__all__'


class ToChuc_CongDongDanCuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tochuc_CongDongDanCu
        fields = '__all__'


class ThuaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thua
        fields = '__all__'


class Nha_CanHoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nha_CanHo
        fields = '__all__'


class CongTringXayDungSerializer(serializers.ModelSerializer):
    class Meta:
        model = CongTrinhXayDung
        fields = '__all__'


class RungSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rung
        fields = '__all__'


class TaiSanKhacSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaiSanKhac
        fields = '__all__'
