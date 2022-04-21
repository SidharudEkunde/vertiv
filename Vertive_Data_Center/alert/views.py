from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from sensors.models import TemperatureHumidity
from .models import Alert
from .serializers import AlertSerializer
from rest_framework import status
from rest_framework.response import Response
import datetime


class AlertAPI(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    """GET method for retrieve all alert details"""

    @staticmethod
    def get(request):
        try:
            currentDate = datetime.date.today().strftime("%Y-%m-%d")
            print(currentDate)
            alt = Alert.objects.filter(lastseen__startswith=currentDate, value__gt=0)
            if alt:
                serializer = AlertSerializer(alt, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"message": "data not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as err:
            print(err)
            return Response({"error": str(err)}, status=status.HTTP_400_BAD_REQUEST)


class AlertTrackingAPI(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        try:
            dt = datetime.datetime.now()
            print(dt)
            payload = []
            # last = dt - datetime.timedelta(minutes=2)
            last = "2022-04-04"
            # print(last)
            sensors = TemperatureHumidity.objects.filter(lastseen__gt=last)
            print("sensors : ", sensors)
            if sensors:
                for sensor in sensors:
                    alert = Alert.objects.filter(lastseen__gte=last, value=24, macid=sensor).order_by('-lastseen').first()

                    alert1 = Alert.objects.filter(lastseen__gte=last, value=25, macid=sensor).order_by('-lastseen').first()

                    if alert:
                        data = {"macid": sensor.macid, "lastseen": alert.lastseen, "panic": alert.value, "freefall": ""}
                        payload.append(data)
                    elif alert1:
                        data = {"macid": sensor.macid, "lastseen": alert1.lastseen, "panic": "", "freefall": alert1.value}
                        payload.append(data)
                    else:
                        data = {"macid": sensor.macid, "lastseen": sensor.lastseen, "panic": "", "freefall": ""}
                        payload.append(data)

                return Response(payload, status=status.HTTP_200_OK)
            return Response({"message :": " Data not found "}, status=status.HTTP_404_NOT_FOUND)
        except Exception as err:
            print(err)
            return Response({"error :": str(err)}, status=status.HTTP_400_BAD_REQUEST)


