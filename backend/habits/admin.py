from django.contrib import admin
from .models import Habit, HabitRecord

@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'frequency', 'is_active', 'created_at')
    list_filter = ('frequency', 'is_active', 'created_at')
    search_fields = ('name', 'user__username')
    ordering = ('-created_at',)
    
@admin.register(HabitRecord)
class HabitRecordAdmin(admin.ModelAdmin):
    list_display = ('habit', 'date', 'completed')
    list_filter = ('completed', 'date')
    search_fields = ('habit__name',)
    ordering = ('-date',)