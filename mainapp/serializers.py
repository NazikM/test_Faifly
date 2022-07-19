from rest_framework import serializers

from mainapp.models import Worker, ScheduleItem, Appointment


class WorkerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'


class ScheduleItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleItem
        fields = ["day", "start_time", "end_time"]


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
