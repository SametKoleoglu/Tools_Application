from django.contrib import admin

from .models import Ping

# Register your models here.
# admin.site.register(Ping)

@admin.register(Ping)
class PingAdmin(admin.ModelAdmin):
    list_display = ('protocol', 'url', 'status', 'response_time', 'response_code')
    list_filter = ('protocol', 'url', 'status')
    search_fields = ('protocol',)
    
    def __str__(self):
        return self.url
