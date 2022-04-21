from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from system.models import System
from system.serializers import SystemSerializer


class SystemAPI(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    """GET method for retrieve details of registered system/bus-bar """

    @staticmethod
    def get(request):
        try:
            rck = System.objects.all()
            serializer = SystemSerializer(rck, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as err:
            print(err)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def post(request):
        try:
            print(request.data)
            mapSerializer = SystemSerializer(data=request.data)
            if mapSerializer.is_valid():
                mapSerializer.save()
                return Response(mapSerializer.data, status=status.HTTP_201_CREATED)
            return Response({"message": "check data format"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as err:
            print(err)
            return Response({"error": str(err)}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request):
        try:
            sysid = request.data.get("sysid")
            data = System.objects.filter(sysid=sysid)
            print(data)
            if data:
                data.delete()
                return Response({"message": "systemid/busbar id " + str(sysid) + " removed successfully"}, status=status.HTTP_200_OK)
            return Response({"message": "systemid/busbar id " + str(sysid) + " not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as err:
            print(err)
            return Response(status=status.HTTP_400_BAD_REQUEST)

