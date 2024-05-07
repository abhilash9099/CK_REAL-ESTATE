import json
from django.shortcuts import render

from property.forms import AddListingForm
from property.models import ContactUs, PropertyDetails,Neibhorhood,PropertyType
from django.shortcuts import render, redirect,reverse
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    queryset  = PropertyDetails.objects.all()
    #queryset.
    ##print(queryset.all())
    #,context={'property_details': property_details}
    #context = {"products": queryset}
    #print(context)
    return render(request,'index.html',{"products": queryset})

def propertyDetail(request,id):
    property  = PropertyDetails.objects.filter(id=id).first()
    return render(request,'propery-detail.html',{"property": property})

def addEditPropertyDetail(request,id=''):

    
    propertyTypeList = PropertyType.objects.all().values()
    neighbourhoodList = Neibhorhood.objects.all().values()
    context = {
        "propertyTypeList":propertyTypeList,
        "neighbourhoodList":neighbourhoodList,
    }
    if id is not '':
        property  = PropertyDetails.objects.filter(id=id).first()
        context["property"] =property

    return render(request, "add_property.html",context)

def storeUpdateListing(request):
    if request.method == 'POST':
        data = request.POST

        id = data['id']
        #image1 = request.FILES['property_photo1']
        #image2 = request.FILES['property_photo2']
        #image3 = request.FILES['property_photo3']
        #image4 = request.FILES['property_photo4']
        try:
            image1 = request.POST['property_photo1']
        except:
            image1 = request.FILES['property_photo1']

        try:
            image2 = request.POST['property_photo2']
        except:
            image2 = request.FILES['property_photo2']
        try:
            image3 = request.POST['property_photo3']
        except:
            image3 = request.FILES['property_photo3']

        try:
            image4 = request.POST['property_photo4']
        except:
            image4 = request.FILES['property_photo4']

        if id is not '':
            property =  PropertyDetails.objects.get(id=id)
            property.property_status = int(data['property_status'])
            property.street_address = data['street_address']
            property.city = data['city']
            property.state = data['state']
            property.zip_code = data['zip_code']
            property.price =float(data['price'])
            property.description = data['description']
            property.bedroom = int(data['bedroom'])
            property.bath = int(data['bath'])
            property.year_built = int(data['year_built'])
            property.build_up_size= int(data['total_sqft'])
            property.total_sqft = int(data['total_sqft'])
            property.property_type =data['property_type']
            property.neighbourhood=data['neighbourhood']

            if image1 != '' and  image1 != 'undefined' :
                print("not undefined Image 1")
                property.property_photo1 = image1
            if image2 != '' and image2 != 'undefined':
                print("not undefined Image 2")
                property.property_photo2 = image2
            if image3 != '' and image3 != 'undefined':
                print("not undefined Image 3")
                property.property_photo3 = image3
            if image4 != '' and image4 != 'undefined':
                print("not undefined Image 4")
                property.property_photo4 = image4

            property.save()
            return redirect("/")
            #return HttpResponse("edited")
        else:

            propertyListing = PropertyDetails()
        
            propertyListing.property_status = int(data['property_status'])
            propertyListing.street_address = data['street_address']
            propertyListing.city = data['city']
            propertyListing.state = data['state']
            propertyListing.zip_code = data['zip_code']
            propertyListing.price =float(data['price'])
            propertyListing.description = data['description']
            propertyListing.bedroom = int(data['bedroom'])
            propertyListing.bath = int(data['bath'])
            propertyListing.year_built = int(data['year_built'])
            propertyListing.build_up_size= int(data['total_sqft'])
            propertyListing.total_sqft = int(data['total_sqft'])
            propertyListing.property_type =data['property_type']
            propertyListing.neighbourhood=data['neighbourhood']
            if image1 != '' and  image1 != 'undefined' :
                print("not undefined Image 1")
                propertyListing.property_photo1 = image1
            if image2 != '' and image2 != 'undefined':
                print("not undefined Image 2")
                propertyListing.property_photo2 = image2
            if image3 != '' and image3 != 'undefined':
                print("not undefined Image 3")
                propertyListing.property_photo3 = image3
            if image4 != '' and image4 != 'undefined':
                print("not undefined Image 4")
                propertyListing.property_photo4 = image4

            propertyListing.save()

            return redirect("/")

@csrf_exempt
def deletelistings(request,id):
    if request.method == "DELETE":
        PropertyDetails.objects.filter(id=id).delete()

    return HttpResponse("success")

@csrf_exempt
def contactUs(request):
    if request.method == "POST":
        data = request.POST
        contact =ContactUs()
        contact.email_id=data["email_id"]
        contact.message = data["message"]
        contact.save()

    return HttpResponse("success")

