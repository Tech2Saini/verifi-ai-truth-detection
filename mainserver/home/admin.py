from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile,Feedback,ContactServices
from django.utils.timesince import timesince
from django.utils.timezone import now
from django.utils.html import format_html


class ProfileAdmin(UserAdmin):
    # Display these fields in the admin panel
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('gender', 'city', 'bio',"profile_image")}),
    )

    list_display = ["username","email","Full_Name","gender","city","Active","User_Type","Profile"]

    def Full_Name(self,obj):
        return f"{obj.first_name} {obj.last_name}"

    def Profile(self,obj):
        image = f"<img src='/media/{obj.profile_image}' style='width:70px;height:70px;border-radius:50%;' />"
        return format_html(image)
    
    def Active(self,instance):
        return f"{instance.is_active}"

    def User_Type(self,instance):
        if instance.is_superuser:
            return "Super"
        elif instance.is_staff:
            return "Staff"
        else:
            return "Normal"
            

# Register the custom user model

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'rating', 'real', 'created_date')
    search_fields = ('user__username', 'content')
    list_filter = ('rating', 'real', 'created_date')



class ContactAdmin(admin.ModelAdmin):
    list_display = ('Name', 'email', 'subject', 'message', 'created_date')

    def Name(self,instance):
        return str(instance.name).title()



admin.site.register(Profile, ProfileAdmin)
admin.site.register(ContactServices,ContactAdmin)