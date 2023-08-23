from django.contrib import admin
from banner_app.models import BannerAppModel

# Register your models here.

class BannerAdmin(admin.ModelAdmin):
    list_display = ('user', 'moto_heading', 'pro_file_image',)
admin.site.register(BannerAppModel, BannerAdmin)
