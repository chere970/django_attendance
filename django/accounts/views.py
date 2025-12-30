from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.
from rest_framework.decorators import permission_classes
from .serializers import LoginSerializer
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def RegisterView(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()

    refresh = RefreshToken .for_user(user)
    # return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
    return Response({
        "user": UserSerializer(user).data,
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def LoginView(request):

    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    refresh = RefreshToken.for_user(user)
    return Response({
        "user": UserSerializer(user).data,
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Dashboard(request):
    if not request.user.is_authenticated:
        return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)
    return Response({
        "message": f"Hello {request.user.username}"
    })


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def dashboard(request):
#     return Response({
#         "message": f"Hello {request.user.username}"
#     })
