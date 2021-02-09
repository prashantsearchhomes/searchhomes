from django.contrib import admin
from shi_app.models import (Amenities, Builder, Property, PropertyImages, Downloads, PropSiteDetails)


# admin.site.register(NewProject, NewProjectAdmin)
admin.site.register(Property)
admin.site.register(Builder)
admin.site.register(Amenities)
admin.site.register(PropertyImages)
admin.site.register(Downloads)
admin.site.register(PropSiteDetails)
