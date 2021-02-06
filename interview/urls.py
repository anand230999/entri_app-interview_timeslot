from django.urls import path

from .views import TimeslotCreateView, TimeSlotGetView

urlpatterns = [
    path("create_timeslot", TimeslotCreateView.as_view(), name="create-timeslot"),
    path("get_timeslot/<slug:interviewer_id>/<slug:candidate_id>", TimeSlotGetView.as_view(), name="get-timeslot")
]