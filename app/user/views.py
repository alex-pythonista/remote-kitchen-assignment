from django.contrib.auth import authenticate, get_user_model

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .serializers import SigninSerializer


User = get_user_model()

from rest_framework_simplejwt.tokens import RefreshToken

def get_token(user):
    refresh = RefreshToken.for_user(
        user=user
    )
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token) 
    }

@api_view(["POST"])
def signin(request):
    try:
        serializer = SigninSerializer(data=request.data)
        if serializer.is_valid():  
            user = authenticate(
                request=request,
                username=serializer.data.get('username'),
                password=serializer.data.get('password'),
            )
            if user is not None:

                token = get_token(user=user)
                return Response({
                    "message" : "Login successful",
                    "user" : {
                        "id" : user.id,
                        "username" : user.username,
                        "email" : user.email,
                        "user_type": user.user_type
                    },
                    "token" : token,
                }, status=status.HTTP_200_OK)
            return Response({
                "message" : "Invalid credentials",
            }, status=status.HTTP_401_UNAUTHORIZED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

    except Exception as e:
        return Response({
            "message" : str(e),
        }, status=status.HTTP_400_BAD_REQUEST)