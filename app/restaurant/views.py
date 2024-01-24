from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import (
    IsAuthenticated, 
    AllowAny
)
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import (
    api_view, 
    permission_classes, 
    authentication_classes
)

from user.models import (
    User,
    OwnerProfile,
    EmployeeProfile
)

from .models import (
    Restaurant,
    Menu,
    Item    
)
from .serializers import (
    RestaurantCreationSerializer,
    RestaurantUpdateSerializer,
    MenuSerializer,
    ItemSerializer,
)
from .permissions import IsOwnerPermission


User = get_user_model()


@authentication_classes([JWTAuthentication])
@permission_classes([IsOwnerPermission])
@api_view(["POST"])
def create_restaurant(request):
    try:
        serializer = RestaurantCreationSerializer(data=request.data)
        if serializer.is_valid():
            owner_obj = OwnerProfile.objects.get(user=request.user)
            print(owner_obj)
            serializer.save(owner=owner_obj)

            return Response({
                "message": "Restaurant created successfully!",
            }, status=status.HTTP_201_CREATED)
        return Response({
            "error": serializer.errors,
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({
            "error": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@api_view(["PATCH"])
def update_restaurant(request, id):
    try:
        restaurant_obj = Restaurant.objects.get(id=id)
        serializer = RestaurantUpdateSerializer(
            instance=restaurant_obj, 
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            
            serializer.save()

            return Response({
                "message": "Restaurant updated successfully!",
            }, status=status.HTTP_200_OK)
        return Response({
            "error": serializer.errors,
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({
            "error": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@authentication_classes([JWTAuthentication])
@permission_classes([IsOwnerPermission])
@api_view(["GET"])
def get_restaurants(request):
    try:
        owner_obj = OwnerProfile.objects.get(user=request.user)
        restaurants = Restaurant.objects.filter(owner=owner_obj)
        serializer = RestaurantUpdateSerializer(restaurants, many=True)

        return Response({
            "restaurants": serializer.data,
        }, status=status.HTTP_200_OK)
    except:
        Response({
            "message": "Restaurants not found!",
        }, status=status.HTTP_404_NOT_FOUND)


@authentication_classes([JWTAuthentication])
@permission_classes([IsOwnerPermission])
@api_view(["POST"])
def create_menu(request):
    try:
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({
                "message": "Menu created successfully!",
            }, status=status.HTTP_201_CREATED)
        return Response({
            "error": serializer.errors,
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({
            "error": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@api_view(["PATCH"])
def update_menu(request, id):
    try:
        menu_obj = Menu.objects.get(id=id)
        serializer = MenuSerializer(
            instance=menu_obj, 
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            
            serializer.save()

            return Response({
                "message": "Menu updated successfully!",
            }, status=status.HTTP_200_OK)
        return Response({
            "error": serializer.errors,
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({
            "error": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@authentication_classes([JWTAuthentication])
@permission_classes([IsOwnerPermission])
@api_view(["GET"])
def get_menus(request):
    try:
        owner_obj = OwnerProfile.objects.get(user=request.user)
        menus = Menu.objects.filter(restaurant__owner_id=owner_obj.id)
        serializer = MenuSerializer(menus, many=True)
        print(serializer.data)

        return Response({
            "restaurants": serializer.data,
        }, status=status.HTTP_200_OK)
    except:
        Response({
            "message": "Restaurants not found!",
        }, status=status.HTTP_404_NOT_FOUND)


@authentication_classes([JWTAuthentication])
@permission_classes([IsOwnerPermission])
@api_view(["POST"])
def create_item(request):
    try:
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({
                "message": "Item created successfully!",
            }, status=status.HTTP_201_CREATED)
        return Response({
            "error": serializer.errors,
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({
            "error": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@api_view(["PATCH"])
def update_item(request, id):
    try:
        item_obj = Item.objects.get(id=id)
        serializer = ItemSerializer(
            instance=item_obj, 
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            
            serializer.save()

            return Response({
                "message": "Item updated successfully!",
            }, status=status.HTTP_200_OK)
        return Response({
            "error": serializer.errors,
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({
            "error": str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)