from django.urls import path

from mainapp.views import WorkerList, Book, AppointmentsList

urlpatterns = [
    path('workerlist/', WorkerList.as_view()),
    path('book/', Book.as_view()),
    path('appointments/', AppointmentsList.as_view())
]
