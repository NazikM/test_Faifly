from django.contrib import admin

from mainapp import models


class ScheduleItemInline(admin.TabularInline):
    model = models.ScheduleItem
    extra = 1


@admin.register(models.Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['location', 'worker']
    inlines = [ScheduleItemInline]


admin.site.register(models.Location)
admin.site.register(models.Worker)
admin.site.register(models.Appointment)
