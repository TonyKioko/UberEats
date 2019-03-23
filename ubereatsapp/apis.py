import json

from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


from ubereatsapp.models import Restaurant, Meal, Order, OrderDetails, Driver
from ubereatsapp.serializers import RestaurantSerializer,MealSerializer



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

def customer_get_meals(request, restaurant_id):
    meals = MealSerializer(
        Meal.objects.filter(restaurant_id = restaurant_id).order_by("-id"),
        many = True,
        context = {"request": request}
    ).data

    return JsonResponse({"meals":meals})

def customer_add_order(request):

    return JsonResponse()
def customer_get_latest_order(request):
    # access_token = AccessToken.objects.get(token = request.GET.get("access_token"),
    #     expires__gt = timezone.now())

    # customer = access_token.user.customer
    # order = OrderSerializer(Order.objects.filter(customer = customer).last()).data

    return JsonResponse()