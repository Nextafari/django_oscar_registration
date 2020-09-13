from rest_framework.generics import CreateAPIView
from .serializers import RegisterUserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import 


class UserRegistration(CreateAPIView):
    serializer_class = RegisterUserSerializer

    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if request.method == "POST":

            serializer.is_valid(raise_exception=True)
            user = User.objects.create(
                first_name=serializer.validated_data.get("first_name"),
                last_name=serializer.validated_data.get("last_name"),
                email=serializer.validated_data.get("email")
            )
            user.set_password(serializer.validated_data.get("password"))
            user.save()
            return Response(
                {
                    'data': "User created successfully!"
                },
                status=status.HTTP_201_CREATED
            )


class GetUser(Api):
    def get(self, request):
        transactions = User.objects.all()
        serializer = RegisterUserSerializer(transactions, many=True)
        return Response(serializer.data)

