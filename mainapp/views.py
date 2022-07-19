from rest_framework import generics, status
from rest_framework.response import Response
from datetime import datetime

from mainapp.models import Worker, Schedule, ScheduleItem, Appointment
from mainapp.serializers import WorkerListSerializer, ScheduleItemListSerializer, AppointmentSerializer


class WorkerList(generics.ListAPIView):
    def get_queryset(self):
        WorkerList.serializer_class = WorkerListSerializer
        queryset = Worker.objects.all()
        speciality = self.request.query_params.get('speciality')
        if speciality:
            return queryset.filter(speciality=speciality)
        full_name = self.request.query_params.get('full_name')
        day = self.request.query_params.get('day')
        if full_name:
            WorkerList.serializer_class = ScheduleItemListSerializer
            worker = queryset.get(full_name=full_name)
            schedule = Schedule.objects.get(worker=worker)
            if day:
                queryset = ScheduleItem.objects.filter(schedule=schedule, day=day)
            else:
                queryset = ScheduleItem.objects.filter(schedule=schedule)
        return queryset


class Book(generics.CreateAPIView):
    model = Appointment
    serializer_class = AppointmentSerializer

    def post(self, request, *args, **kwargs):
        day = request.data.get('day')
        start_time = request.data.get('start_time')
        end_time = request.data.get('end_time')
        schedule = request.data.get('schedule')
        schedule_item = None
        appointments = None
        start_time_obj = datetime.strptime(start_time, '%H:%M').time()
        end_time_obj = datetime.strptime(end_time, '%H:%M').time()
        day_obj = datetime.strptime(day, "%Y-%m-%d")
        try:
            appointments = Appointment.objects.filter(day=day_obj, schedule=schedule)
            schedule_item = ScheduleItem.objects.get(schedule=schedule, day=day_obj.weekday()+1)
            appointments.get(start_time=start_time, end_time=end_time)
        except (self.model.DoesNotExist, ScheduleItem.DoesNotExist):
            if not schedule_item:
                return Response(data={"error": "Specialist doesn't work in this day."},
                                status=status.HTTP_409_CONFLICT)
            if schedule_item.start_time > start_time_obj or schedule_item.end_time < end_time_obj:
                return Response(data={"error": "Specialist doesn't work in these hours."},
                                status=status.HTTP_409_CONFLICT)
            for appointment in appointments:
                if start_time_obj < appointment.start_time < end_time_obj or start_time_obj < appointment.end_time < end_time_obj or \
                        start_time_obj > appointment.start_time and end_time_obj < appointment.end_time:
                    return Response(data={"error": "This time is already booked."},
                                    status=status.HTTP_409_CONFLICT)
            return self.create(request, *args, **kwargs)
        return Response(data={"error": "Booking with these parameters already exist."}, status=status.HTTP_409_CONFLICT)


class AppointmentsList(generics.ListAPIView):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        queryset = Appointment.objects.all()
        day = self.request.query_params.get('day')
        if day:
            queryset = queryset.filter(day=day)
        return queryset
