from rest_framework import serializers
from .models import User
from contacts.serializers import ContactSerializer

class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    contacts = ContactSerializer(many=True, required=False)

    def get_name(self,obj)->str:
        return f'{obj.first_name} {obj.last_name}'

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value) if not key== 'password' else instance.set_password(value)

        instance.save()

        return instance

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name', 'first_name', 'last_name', 'phone', 'registered_at', 'password', 'contacts']
        read_only_fields = ['contacts']
        extra_kwargs = {"password": {"write_only": True}, "first_name": {"write_only": True}, "last_name": {"write_only": True}}