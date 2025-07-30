from rest_framework import serializers
from .models import *

class UsersTbSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersTb
        fields = '__all__'

class OrphelinsTbSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrphelinsTb
        fields = '__all__'

class AdoptionsTbSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdoptionsTb
        fields = '__all__'

class AdoptantsTbSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdoptantsTb
        fields = '__all__'

class DocumentsTbSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentsTb
        fields = '__all__'

class DonatorsTbSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonatorsTb
        fields = '__all__'

class GiftsTbSerializer(serializers.ModelSerializer):
    class Meta:
        model = GiftsTb
        fields = '__all__'

class MedicalVisitsTbSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalVisitsTb
        fields = '__all__'

class EducationTbSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationTb
        fields = '__all__'

class CountryTbSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryTb
        fields = '__all__'

class StatusTbSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusTb
        fields = '__all__'

class RolesTbSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolesTb
        fields = '__all__'

class SexTbSerializer(serializers.ModelSerializer):
    class Meta:
        model = SexTb
        fields = '__all__'

class ActionsTbSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionsTb
        fields = '__all__'

class MessagesTbSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessagesTb
        fields = '__all__'

class OrphelinatsTbSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrphelinatsTb
        fields = '__all__'
