from django.db import models


class Location(models.Model):
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city}, {self.address}"


class Worker(models.Model):
    full_name = models.CharField(max_length=100, unique=True)
    speciality = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class Schedule(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedule'

    def __str__(self):
        return f'{self.location}, {self.worker}'


class ScheduleItem(models.Model):
    DAYS_OF_THE_WEEK = (
        ('1', 'Monday'),
        ('2', 'Tuesday'),
        ('3', 'Wednesday'),
        ('4', 'Thursday'),
        ('5', 'Friday'),
        ('6', 'Saturday'),
        ('7', 'Sunday')
    )
    day = models.CharField(max_length=1, choices=DAYS_OF_THE_WEEK)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f'Day:{self.day}, Time:{self.start_time}-{self.end_time}'

    class Meta:
        ordering = ('start_time',)


class Appointment(models.Model):
    schedule = models.ForeignKey(Schedule, models.CASCADE)
    # DAYS_OF_THE_WEEK = (
    #     ('1', 'Monday'),
    #     ('2', 'Tuesday'),
    #     ('3', 'Wednesday'),
    #     ('4', 'Thursday'),
    #     ('5', 'Friday'),
    #     ('6', 'Saturday'),
    #     ('7', 'Sunday')
    # )
    # day = models.CharField(max_length=1, choices=DAYS_OF_THE_WEEK)
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"Location: {self.schedule.location},\
         worker: {self.schedule.worker}, day: {self.day},\
          time: {self.start_time}-{self.end_time}"
