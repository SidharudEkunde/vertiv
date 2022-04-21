# Create your views here.
from django.db.models import Count
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from sensors.models import TemperatureHumidity, IAQ, DailyTemperatureHumidity, WeeklyTemperatureHumidity, \
    MonthlyTemperatureHumidity
from sensors.serialzers import TemperatureHumiditySerializer, SensorSerializer, TemperatureHealthSerializer
import datetime
from system.models import System


class TemperatureHumidityAPI(APIView):
    """API for TemperatureHumidity"""
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        """GET method to retrieve all details of registered temp-humidity tags"""
        try:
            syst = System.objects.all()
            payload = []
            if syst:
                for i in syst:
                    data = TemperatureHumidity.objects.filter(systemid=i)
                    print(data)
                    serializer = TemperatureHumiditySerializer(data, many=True)
                    payload.append(
                        {"systemname": i.name, "sysid": i.sysid, "image": str(i.image), "sensors": serializer.data})
                return Response(payload, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as err:
            print(err)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def post(request):
        """POST method for new registration"""
        try:
            print(request.data)
            rk = System.objects.filter(sysid=request.data.get('systemid')).first()
            if rk:
                usage = TemperatureHumidity.objects.filter(systemid=rk).aggregate(Count('systemid'))
                print(usage)
                if usage['systemid__count'] < 3:
                    var = TemperatureHumidity()
                    var.macid = request.data.get("macid")
                    var.max = request.data.get("max")
                    var.min = request.data.get("min")
                    var.temperature = 0.0
                    var.humidity = 0.0
                    var.battery = 0.0
                    var.systemid = rk
                    var.save()
                    return Response({"message": "Successfully Registered New Sensor Under System/Bus-bar " + str(rk)}, status=status.HTTP_201_CREATED)
                return Response({"Capacity is full, you can't register under this system or Bus-bar"},
                                status=status.HTTP_406_NOT_ACCEPTABLE)
            return Response({"message": "systemid not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as err:
            print(err)
            return Response({"error": str(err)}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request):
        """DELETE method to delete particular temperature-humidity tag"""

        try:
            data = TemperatureHumidity.objects.filter(macid=request.data.get("macid")).first()
            if data:
                data.delete()
                return Response({"message": "TagID " + str(data) + " Successfully Deleted"}, status=status.HTTP_200_OK)
            return Response({"message": "TagID not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as err:
            print(err)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class DailyTemperatureHumidityAPI(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        """ GET method to retrieve daily temperature-humidity data """
        try:
            currentDate = datetime.date.today().strftime("%Y-%m-%d")
            macid = request.GET.get("macaddress")
            # print(macid)
            asset = TemperatureHumidity.objects.filter(macid=macid).first()
            if asset:
                # print(asset, "asset ")
                sensor = DailyTemperatureHumidity.objects.filter(
                    asset=asset, timestamp__startswith=currentDate)
                if sensor.exists():
                    thSerializer = SensorSerializer(sensor, many=True)
                    return Response(thSerializer.data, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "macid " + str(macid) + " daily tracking data not found"}, status=status.HTTP_204_NO_CONTENT)
            return Response({"message": "macid " + str(macid) + " not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as err:
            print(err)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class WeeklyTemperatureHumidityAPI(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        """ GET method to retrieve weekly temperature-humidity data """
        try:
            currentDate = datetime.date.today()
            lastweekdate = currentDate - datetime.timedelta(days=7)
            tmwdate = currentDate + datetime.timedelta(days=1)

            macid = request.GET.get("macaddress")
            asset = TemperatureHumidity.objects.get(macid=macid)
            if asset:
                print(asset)
                sensor = WeeklyTemperatureHumidity.objects.filter(
                    asset=asset, timestamp__gte=lastweekdate, timestamp__lte=tmwdate).order_by('timestamp')
                if sensor.exists():
                    thSerializer = SensorSerializer(sensor, many=True)
                    return Response(thSerializer.data, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "macid " + str(macid) + " Weekly tracking data not found"}, status=status.HTTP_204_NO_CONTENT)
            return Response({""}, status=status.HTTP_404_NOT_FOUND)
        except Exception as err:
            print(err)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class MonthlyTemperatureHumidityAPI(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        """ GET method to retrieve monthly based temperature-humidity data """
        try:
            currentDate = datetime.date.today()
            month = currentDate.month
            year = currentDate.year
            if month < 10:
                month = "0" + str(month)
            dt = str(year) + "-" + str(month)

            macid = request.GET.get("macaddress")
            asset = TemperatureHumidity.objects.get(macid=macid)
            if asset:
                sensor = MonthlyTemperatureHumidity.objects.filter(
                    asset=asset, timestamp__startswith=dt).order_by('timestamp')
                if sensor.exists():
                    thSerializer = SensorSerializer(sensor, many=True)
                    return Response(thSerializer.data, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "macid not found"}, status=status.HTTP_204_NO_CONTENT)
            return Response({"message": "data not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as err:
            print(err)
            return Response({"error": str(err)}, status=status.HTTP_400_BAD_REQUEST)


# class TempHumiHealthAPI(APIView):
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticated]

#     @staticmethod
#     def get(request):
#         try:
#             sensors = TemperatureHumidity.objects.all()
#             serializer = TemperatureHumiditySerializer(sensors, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Exception as err:
#             return Response({"error":str(err)}, status=status.HTTP_400_BAD_REQUEST)


class IAQAPI(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    """POST method for new registration"""

    @staticmethod
    def post(request):
        try:
            iaq = IAQ()
            iaq.macid = request.data.get("macid")
            iaq.battery = 0.0
            iaq.co2 = 0.0
            iaq.tvoc = 0.0
            iaq.rackid = request.data.get("room")
            # iaq.floor = FloorMap.objects.get(id=request.data.get("floorid"))
            iaq.x = request.data.get("x")
            iaq.y = request.data.get("y")
            iaq.save()
            return Response(status=status.HTTP_201_CREATED)

        except Exception as err:
            print(err)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    """GET method to retrieve all details of registered IAQ tags"""

    # @staticmethod
    # def get(request):
    #     try:
    #         if request.GET.get("floorid"):
    #             data = IAQ.objects.filter(floor=request.GET.get("floorid"))
    #         else:
    #             data = IAQ.objects.all()
    #         if data:
    #             ser = IAQSerializer(data, many=True)
    #             return Response(ser.data, status=status.HTTP_200_OK)
    #         else:
    #             return Response(status=status.HTTP_404_NOT_FOUND)
    #
    #     except Exception as err:
    #         print(err)
    #         return Response(status=status.HTTP_400_BAD_REQUEST)

    """ DELETE method to delete/remove particular IAQ tag details"""

    @staticmethod
    def delete(request):
        try:
            data = IAQ.objects.filter(macid=request.data.get("macid")).first()
            if data:
                data.delete()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)

        except Exception as err:
            print(err)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    """PATCH method to update particular IAQ tag"""

    @staticmethod
    def patch(request):
        try:
            iaq = IAQ.objects.get(macid=request.data.get("macid"))
            iaq.co2 = 0.0
            iaq.tvoc = 0.0
            iaq.room = request.data.get("room")
            iaq.x = request.data.get("x")
            iaq.y = request.data.get("y")
            # iaq.floor = FloorMap.objects.get(id=request.data.get("floorid"))
            iaq.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        except Exception as err:
            print(err)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class HealthAPI(APIView):
    """API for sensors health"""

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    """Get method to retrieve health status of registered sensor tags(Temperature/Humidity sensors) """

    @staticmethod
    def get(request):
        try:
            temp = TemperatureHumidity.objects.all()
            serializer = TemperatureHealthSerializer(temp, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as err:
            print(err)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class RealTimeTrackingAPI(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        try:
            # data = TemperatureHumidity.objects.all().ordr_by("systemid")
            data = TemperatureHumidity.objects.all().values('systemid')
            serializer = TemperatureHumiditySerializer(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as err:
            print(err)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class SystemRealtimeTrackingAPI(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        """ GET method to retrieve details of registered sensors under requested system/bus-bar """
        try:
            payload = []
            sysid = request.GET.get("sysid")
            print(sysid)
            system = System.objects.filter(sysid=sysid).first()
            print(system)
            if system:
                temp = TemperatureHumidity.objects.filter(systemid=system)
                if temp:
                    print(temp)
                    for i in temp:
                        daily = DailyTemperatureHumidity.objects.filter(asset=i)
                        print(daily)
                        serializer = SensorSerializer(daily, many=True)
                        payload.append({"sensorid": i.macid, "sensors": serializer.data})
                    return Response(payload, status=status.HTTP_200_OK)
                return Response({"message": "sensors not found under System ID " + str(sysid)}, status=status.HTTP_204_NO_CONTENT)
            return Response({"message": "SystemID " + str(sysid) + "not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as err:
            print(err)
            return Response({"error": str(err)}, status=status.HTTP_400_BAD_REQUEST)


class WeeklyRealtimeTrackingAPI(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        """ GET method to retrieve weekly based sensor data """
        try:
            payload = []
            sysid = request.GET.get("sysid")
            print(sysid)
            system = System.objects.filter(sysid=sysid).first()
            if system:
                temp = TemperatureHumidity.objects.filter(systemid=system)
                if temp:
                    print(temp)
                    for i in temp:
                        print(i)
                        daily = WeeklyTemperatureHumidity.objects.filter(asset=i)
                        serializer = SensorSerializer(daily, many=True)
                        payload.append({"sensorid": i.macid, "sensors": serializer.data})
                        print(payload)
                    return Response(payload, status=status.HTTP_200_OK)
                return Response({"message": "sensors not found under System ID " + str(sysid)}, status=status.HTTP_204_NO_CONTENT)
            return Response({"message": " System ID " + str(sysid) + " not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as err:
            print(err)
            return Response({"error": str(err)}, status=status.HTTP_400_BAD_REQUEST)


class MonthlyRealtimeTrackingAPI(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        """ GET method to retrieve monthly based sensor data """
        try:
            payload = []
            sysid = request.GET.get("sysid")
            system = System.objects.filter(sysid=sysid).first()
            if system:
                temp = TemperatureHumidity.objects.filter(systemid=system)
                if temp:
                    for i in temp:
                        daily = MonthlyTemperatureHumidity.objects.filter(asset=i)
                        serializer = SensorSerializer(daily, many=True)
                        payload.append({"sensorid": i.macid, "sensors": serializer.data})
                    return Response(payload, status=status.HTTP_200_OK)
                return Response({"message": "sensors not found under System ID " + str(sysid)}, status=status.HTTP_204_NO_CONTENT)
            return Response({"message": "System ID " + str(sysid) + "not found"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as err:
            print(err)
            return Response({"error": str(err)}, status=status.HTTP_400_BAD_REQUEST)

# "select asset_id,round(avg(p.temperature)) as temperature, round(avg(p.humidity)) as humidity, p.time from" \
# " (select asset_id,temperature,humidity,date_format(timestamp-interval minute(timestamp)%30 minute, '%Y-%m-%d %H:%i') as time " \
# "from sensor_dailytemperaturehumidity where timestamp like '" + str(currentDate) + "%'" \
# "group by date_format(timestamp-interval minute(timestamp)%30 minute, '%Y-%m-%d %H:%i'), temperature, humidity,asset_id) as p  group by p.time, asset_id;"
