from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display=['id','name','address','branch_code','bank']
    
    
admin.site.register(Bank)
