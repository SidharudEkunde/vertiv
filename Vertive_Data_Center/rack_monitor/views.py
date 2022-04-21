from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from common.models import FloorMap
from rack_monitor.models import Rack
from rack_monitor.serializers import RackSerializer


class RackAPI(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    """GET method for retrieve details of registered rack_monitor tag """
    @staticmethod
    def get(request):
        try:
            floor = request.GET.get("floorid")
            rck = Rack.objects.filter(floor=floor)
            serializer = RackSerializer(rck, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        except Exception as err:
            print(err)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    """POST method to register new rack_monitor tag"""
    @staticmethod
    def post(request):
        try:
            rck = Rack()
            rck.floor = FloorMap.objects.filter(id=request.data.get("floorid")).first()
            rck.macid = request.data.get("macid")
            rck.pdu = request.data.get("pdu")
            rck.capacity = request.data.get("capacity")            
            rck.x = request.data.get("x1")
            rck.y = request.data.get("y1")
            rck.x1 = request.data.get("x2")
            rck.y1 = request.data.get("y2")
            rck.save()
            return Response(status=status.HTTP_201_CREATED)
            
        except Exception as err:
            return Response({"error :": str(err)}, status=status.HTTP_400_BAD_REQUEST)

    """PATCH method to update particular rack_monitor tag"""
    @staticmethod
    def patch(request):
        try:
            rck = Rack.objects.get(macid=request.data.get("macid"))
            rck.floor = FloorMap.objects.get(id=request.data.get("floorid"))
            rck.x = request.data.get("x")
            rck.y = request.data.get("y")
            rck.save()
            return Response(status=status.HTTP_202_ACCEPTED)
            
        except Exception as err:
            print(err)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    """DELETE method for delete particular rack_monitor tag"""
    @staticmethod
    def delete(request):
        try:
            rck = Rack.objects.filter(macid=request.data.get("macid"))
            if rck:
                rck.delete()
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as err:
            print(err)
            return Response(status=status.HTTP_400_BAD_REQUEST)

