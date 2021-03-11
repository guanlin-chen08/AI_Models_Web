from django.contrib import admin

# Register your models here.
from historyapp.models import History
from historyapp.models import HistoryImage

class HistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'bs1', 'last_modify_date', 'created')
    ordering = ('id',)
    search_fields = ('bs1',)
class HistoryImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'EmpName', 'image', 'last_modify_date', 'created')
    ordering = ('id',)
    search_fields = ('id',)
admin.site.register(History, HistoryAdmin)
admin.site.register(HistoryImage, HistoryImageAdmin)