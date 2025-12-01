from django.shortcuts import render, redirect
from .models import House, Category

def home_view(request):

    houses = House.objects.all().filter(is_active=True)

    data = {
        'houses': houses,
        'title': 'Home Page'
    }

    return render(request, 'main/index.html', data)

def house_detail_view(request, house_id):

    house = House.objects.get(id=house_id)

    return render(request, 'main/property-detail.html', {'house': house, 'title': 'House Page'})

def product_view(request):

    return render(request, 'main/properties.html')

def contact_view(request):

    return render(request, 'main/contact.html')