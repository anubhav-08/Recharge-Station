from django.shortcuts import render

from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import PlanSerializer
from .models import Plan, Company
# Create your views here.

# To get list of plans available for that that particular company
class PlanListView(GenericAPIView):
    serializer_class = PlanSerializer

    def get_queryset(self, company=None):
        return Plan.objects.filter(company = company)
    
    def get(self, request, company):
        # company = request.query_params['company']
        try:
            company = Company.objects.get(name=company)
        except :
            return Response({"message" : "Invalid Company Selected"}, status=status.HTTP_400_BAD_REQUEST)
        
        qs = self.get_queryset(company)
        serializer = self.serializer_class(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# To get the particular selected plan
class PlanAPIView(GenericAPIView):
    serializer_class = PlanSerializer

    def get(self, request, _id):
        # _id = request.query_params['id']
        plan = Plan.objects.get(id = _id)
        serializer = self.serializer_class(plan)
        return Response(serializer.data, status=status.HTTP_200_OK)