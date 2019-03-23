import json

from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


from ubereatsapp.models import Restaurant, Meal, Order, OrderDetails, Driver
from ubereatsapp.serializers import RestaurantSerializer



############
# CUSTOMER
############

def customer_get_restaurants(request):
    restaurants = RestaurantSerializer(
        Restaurant.objects.all().order_by("-id"),
        many = True,
        context = {"request": request}
        
    ).data

    return JsonResponse({"restaurants": restaurants})