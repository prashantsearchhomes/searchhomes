from django.http import HttpResponse
from django.shortcuts import render

from shi_app.models import (Builder, Property)


# Initialization for the index file 
def index(request):
    builder = Builder.objects.all().order_by('-id')

    property_details = Property.objects.all()
    
    property_region = Property.objects.values_list('region', flat=True)
    
    # property_location = Property.objects.filter(location).all()
    # property_region = Property.objects.filter(region).all()

    print(property_details)
    print(property_region)

    
    # builders = {}
    # for i in builder:
    #     name = i.name
    #     logo = i.logo
    #     builders[name] = logo
    return render(request, 'index.html', { 'property_details':property_details, 'property_region':property_region})
    



# Filteration of the Property by name, location, region and sending to home.html    
def properties(request,**kwargs):
    
    location = request.POST.get("location", '')
    region = request.POST.get("region", '')
    name = request.POST.get("name", '')
    
    print(location)
    print(region)
    print(name)
    
    filters = {}

    prop = Property.objects.filter(name=name, location=location, region=region)   
    # if location:
    #     filters['location'] = location
    #     prop = Property.objects.filter(location__icontains=location)
    #     print(prop)
    # if region:
    #     filters['region'] = region
    #     prop = Property.objects.filter(region__icontains=region)
    #     print("1")
    # if name:
    #     filters['name'] = name
    #     prop = Property.objects.filter(name__icontains=name) 

    print(prop)  
    properties = {}
    i=0
    for obj in prop:
        property = {
            "name":obj.name,
            "location":obj.location,
            "slug":obj.slug,
            "res_com":obj.res_com,
            "region":obj.region,
            "status":obj.status,
            "rera":obj.rera,
            "overview":obj.overview,
            "summary":obj.summary,
            "project_area":obj.project_area,
            "no_of_units":obj.no_of_units,
            "no_of_floors":obj.no_of_floors,
            "open_area":obj.open_area,
            "no_of_block":obj.no_of_block,
            "builder":obj.builder,
            "prop_type":obj.prop_type,
            "banner_image":obj.banner_image,
            "base_price":obj.base_price,
            "possession_date":obj.possession_date,
            "sq_feet_price":obj.sq_feet_price,
            "master_plan":obj.master_plan
        }
        properties[i] = property
        i = i+1  
    return render(request,'home.html', {'properties':properties})
