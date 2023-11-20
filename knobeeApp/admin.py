from django.contrib import admin
from knobeeApp import models
# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ["Job_ID","Job_Title","Job_Description"]
admin.site.register(models.JobListings,ListingAdmin)

class ApplicationAdmin(admin.ModelAdmin):  
    list_display = ["App_ID","Job_ID","Name","Email","Contact"]
admin.site.register(models.JobApplications,ApplicationAdmin)
