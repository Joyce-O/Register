from rest_framework import serializers
from .models import Users

class UsersSerializers(serializers.Serializer):
    class Meta:
        model = Users
        field = '__all__'
    
    def create(self, validate_data):
        print('----', validate_data)
        return Users.objects.create(**validate_data)
