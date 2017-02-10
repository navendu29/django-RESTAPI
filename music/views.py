from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from .models import stalks
from .serializers import stalkSerializer
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
import json

class stockList(APIView):
    def get(self,request):
        stocks=stalks.objects.all()
        serializer=stalkSerializer(stocks,many=True)
        return Response(serializer.data)





    def post(self,request):
        data = json.loads(request.body)
        for obj in data :
            stalks.objects.create(ticker=obj['ticker'], open=obj['open'],close=obj['close'],volume=obj['volume'])

        return HttpResponse("success")


