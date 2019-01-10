from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display=('user','user_info','phone','website')

    def user_info(self,obj):
        return obj.description

    user_info.short_description="description"

    def get_queryset(self,request):
        queryset=super().get_queryset(request)
        query_set=queryset.order_by('-phone','user')
        return query_set
admin.site.register(UserProfile,UserProfileAdmin)
