from django.forms import ModelForm
from property.models import PropertyDetails



class AddListingForm(ModelForm):
    class Meta:
        model = PropertyDetails
        fields = ["property_status","street_address", "city", "state", "zip_code",
                "price",
                "description",
                "bedroom",
                "bath",
                "fire_place",
                "year_built",
                "build_up_size",
                "total_sqft",
                "property_photo1",
                "property_photo2",
                "property_photo3",
                "property_photo4",
                "property_type"]

   
