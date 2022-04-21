from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class LoginAPI(APIView):
    @staticmethod
    def post(request):
        username = request.data.get("username")
        password = request.data.get("password")
        try:
            user = list(User.objects.filter(username=username))
            if len(user) != 0:
                user = authenticate(request, username=user[0].username, password=password)
                if user is not None:
                    login(request, user)
                    return Response({"success": " Welcome back {}".format(user)}, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "password is wrong "}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({"error": "username is wrong"}, status=status.HTTP_401_UNAUTHORIZED)

        except Exception as err:
            return Response({"error": str(err)}, status=status.HTTP_404_NOT_FOUND)


class LogoutAPI(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        try:
            logout(request)
            return Response(status=status.HTTP_200_OK)
        except Exception as err:
            return Response({"error :": str(err)}, status=status.HTTP_400_BAD_REQUEST)



