from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status
from .serializer import UsersSerializers
from .models import Users

# Create your views here.

class UsersView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        firstname = request.data.get('firstname', '')
        lastname = request.data.get('lastname', '')
        age = request.data.get('age', '')
        job_position = request.data.get('job_position', '')
        data = {
            'firstname': firstname,
            'lastname': lastname,
            'age': age,
            'job_position': job_position}
        # print(firstname)
        Users.objects.create(**data)
        # serializers = UsersSerializers(data={
        #     'firstname': firstname,
        #     'lastname': lastname,
        #     'age': age,
        #     'job_position': job_position,
        # })
        # serializers.is_valid(raise_exception=True)
        # user = serializers.save()
        return Response(
            status = status.HTTP_201_CREATED,
            data = {'message': 'Registeration is successful'}
        )

