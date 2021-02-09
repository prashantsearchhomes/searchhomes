from django.db import models
from datetime import datetime



# Model For Amenities Details 
class Amenities(models.Model):
  title = models.CharField(max_length=550, default=" ") 
  icon = models.FileField(blank=True)
  timestamp = models.DateTimeField(default=datetime.now)
 
  def __str__(self):
   return self.title

  class Meta:
        verbose_name_plural = "Amenities"  

# Model For Builder Details 
class Builder(models.Model):
  name = models.CharField(max_length=200, default= None, blank=True )
  logo = models.FileField( blank=True, default= None )
  slug = models.CharField(max_length=550, default=" ", null=True)
  summary = models.TextField(blank=True )
  sole_partner = models.CharField(max_length=200, default=" ", null=True)  

  def __str__(self):
   return self.name  

  class Meta:
    verbose_name_plural = "Builders"


# Model For Property Details Refering Builder as Foreign Key and Amenities with ManyToManyField
class Property(models.Model):
  builder =models.ForeignKey(Builder, on_delete=models.SET_NULL, null=True)
  name = models.CharField(max_length=1100, default= None) 
  slug = models.CharField(max_length=1100, default=" ", null=True)
  res_com = models.CharField(max_length=1100, default="Residential", null=True)
  location = models.CharField(max_length=1100, default=" ")  
  region = models.CharField(max_length=1100, default=" ")  
  summary = models.CharField(max_length=1100, default=" ", null=True)
  project_area = models.CharField(max_length=1100, default=" ") 
  no_of_units = models.CharField(max_length=550, default=" ") 
  no_of_floors = models.CharField(max_length=550, default=" ") 
  open_area = models.CharField(max_length=550, default=" ") 
  no_of_tower = models.CharField(max_length=550, default=" ") 
  no_of_block = models.CharField(max_length=550, default=" ") 
  prop_type = models.CharField(max_length=550, default=None)
  banner_image = models.FileField(blank=True, default=" ")
  base_price = models.CharField(max_length=550, null=True, default= None)
  status = models.CharField(max_length=550, null=True, default= " ")
  sq_feet_price = models.CharField(max_length=550, null=True, default= None)
  possession_date = models.CharField(max_length=550, null=True, default= None)
  overview = models. TextField(max_length=10000, default=None)
  video = models.CharField(max_length=10000, default=" ")
  google_map = models.CharField(max_length=10000, default=" ")
  rera = models.TextField(max_length=1000, default=None)
  master_plan = models.FileField(blank=True,  default=" ")
  construction_video = models.FileField(blank=True,  default=" ")
  amenities = models.ManyToManyField(Amenities)
  home_banner_display = models.CharField(max_length=550, null=True, default= "No")
  timestamp = models.DateTimeField(default=datetime.now)
  is_featured = models.BooleanField(default=False)

  def __str__(self):
   return self.name  

  class Meta:
        verbose_name_plural = "Property"

# Model for PropertyImages Refering Property as Foreign Key
class PropertyImages(models.Model):
    property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=550, default="")
    image = models.FileField(blank=True)
    timestamp = models.DateTimeField(default=datetime.now)

    def __str__(self):
      return self.title

    class Meta:
      verbose_name_plural = "Property Images"


# Model for Downloads Refering Property as Foreign Key
class Downloads(models.Model):
    property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=550, default=" ") 
    attached_file = models.FileField(blank=True)
    timestamp = models.DateTimeField(default=datetime.now) 

    def __str__(self):
      return self.title
  
    class Meta:
      verbose_name_plural = "Downloads"

# Model for Property  Site Details Refering Property as ForeignKey
class PropSiteDetails(models.Model):
    property =models.ForeignKey(Property, on_delete=models.SET_NULL, null=True)
    bhk_type = models.CharField(max_length=550, default=" ") 
    block = models.CharField(max_length=550, null=True) 
    phase = models.CharField(max_length=550, default=" ") 
    inclusion = models.TextField(max_length=1000, default=" ") 
    builtup_area_sqft = models.FloatField(null=True, default= None)
    carpet_area_sqft = models.FloatField(null=True, default= None)
    balcony_area = models.FloatField(null=True, default= None)
    rate_sqft = models.FloatField(null=True, default= None)
    agreement_value = models.FloatField(null=True, default= " ")
    floor_plan = models.FileField(blank=True)
    timestamp = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name_plural = "Property Site Details"