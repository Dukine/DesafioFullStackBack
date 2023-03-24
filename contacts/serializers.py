from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    def get_name(self,obj)->str:
        return f'{obj.first_name} {obj.last_name}'

    class Meta:
        model = Contact
        fields = ['id', 'email', 'name', 'first_name', 'last_name', 'phone', 'registered_at', ]
        extra_kwargs = {'first_name': {'write_only': True}, 'last_name': {'write_only': True}}