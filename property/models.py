from django.db import models


class PropertyType(models.Model):
    property_type = models.CharField(max_length=50)

    def __str__(self):
        return self.property_type
    
class ContactUs(models.Model):
    email_id = models.CharField(max_length=100)
    message  = models.CharField(max_length=250)


class Neibhorhood(models.Model):
    # property_Name = models.ForeignKey(Property,on_delete=models.CASCADE)
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length=50)
 
    def __str__(self):
        return self.name

class PriceRange(models.Model):
    price_range = models.CharField(max_length=50)

    def __str__(self):
        return self.price_range

class Property(models.Model):
    price_range = models.ForeignKey(PriceRange,on_delete=models.CASCADE)
    property_type = models.ForeignKey(PropertyType,on_delete=models.CASCADE)
    neighbhorhood = models.ForeignKey(Neibhorhood,on_delete=models.CASCADE)
    featured = models.BooleanField(default=True)

class PropertyDetails(models.Model):
    property_status = models.IntegerField()
    street_address = models.CharField(max_length=50)
    city  = models.CharField(max_length=50)
    state  = models.CharField(max_length=50)
    zip_code  = models.CharField(max_length=50)
    price  = models.FloatField(null=True, blank=True, default=None)
    description = models.CharField(max_length=50)
    bedroom = models.IntegerField()
    bath= models.IntegerField()
    fire_place = models.BooleanField(default=True)
    year_built = models.IntegerField()
    build_up_size  = models.IntegerField()
    total_sqft = models.IntegerField()
    property_photo1 = models.ImageField(upload_to ='static/uploads/') # pip install Pillow
    property_photo2 = models.ImageField(upload_to ='static/uploads/') # pip install Pillow
    property_photo3 = models.ImageField(upload_to ='static/uploads/') # pip install Pillow
    property_photo4 = models.ImageField(upload_to ='static/uploads/') # pip install Pillow
    property_type = models.CharField(max_length=50)
    neighbourhood= models.IntegerField()


class Searches(models.Model):
    price_range = models.ForeignKey(PriceRange,on_delete=models.CASCADE)
    property_type = models.ForeignKey(PropertyType,on_delete=models.CASCADE)
    neighbhorhood = models.ForeignKey(Neibhorhood,on_delete=models.CASCADE)
    date_searched = models.DateTimeField(auto_now_add=True, null=True, blank=True)


