from django.shortcuts import render

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TransactionSerializer
# Create your views here.

class TransactionView(GenericAPIView):

    serializer_class = TransactionSerializer

    def post(self, request):
        # print(request.data)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        transaction = serializer.create(validated_data=serializer.validated_data)
        serializer = self.serializer_class(transaction)

        # print(serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)