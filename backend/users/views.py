from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
import json
from .serializer import *
import requests

# Create your views here.

class UsersView(APIView):

    def get(self,request):
        # data=json.dumps(list(Users.objects.filter().values()))
        queryset=Users.objects.filter().values()
        ser=UserSerialize(queryset, many=True)
        data=ser.data
        resp=requests.get(url='https://jsonplaceholder.typicode.com/users')
        resp_data=json.loads(resp.content)
        return Response([data,resp_data])


# email: paul@workongrid.com