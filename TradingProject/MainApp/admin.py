from django.contrib import admin
from .models import Candle

#admin configuration for the candle model
@admin.register(Candle)
class CandleAdmin(admin.ModelAdmin):
    list_display = ('id', 'open', 'high', 'low', 'close', 'date')
    list_filter = ('date',)
    search_fields = ('id', 'date')
    date_hierarchy = 'date'

