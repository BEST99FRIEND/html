from django.shortcuts import render, redirect, get_object_or_404
from .models import House, Category

def home_view(request):

    houses = House.objects.all().filter(is_active=True)

    data = {
        'houses': houses,
        'title': 'Home Page'
    }

    return render(request, 'main/index.html', data)

def house_detail_view(request, house_id):


    house = get_object_or_404(House, id=house_id)

    return render(request, 'main/property-detail.html', {'house': house, 'title': 'House Page'})

def product_list_view(request):

    categories = Category.objects.all()

    houses = House.objects.all().filter(is_active=True)

    category = request.GET.get("category")
    print(category)

    if category:

        houses = houses.filter(category_name=category)

    data = {
        'categories': categories,
        'houses': houses,
        'title': 'Properties Page'
    }

    return render(request, 'main/properties.html', data)

def contact_view(request):

    return render(request, 'main/contact.html')
