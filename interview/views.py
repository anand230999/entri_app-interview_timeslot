import json

from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import TimeSlotSerializer
from .models import TimeSlot
from .utils import get_candidate_time_slots


class TimeslotCreateView(CreateAPIView):
    """
        Saving the available timeslot of Interviewer/Candidate.
    """
    serializer_class = TimeSlotSerializer


class GetTimeSlotSerializer(object):
    pass


class TimeSlotGetView(GenericAPIView):
    """
    Get matching time slots.
    """
    http_method_names = ['get']

    def get(self, *args, **kwargs):
        response = {
            "status": False,
            "message": "Not matching slots found."
        }
        interviewer_id = kwargs.get("interviewer_id")
        candidate_id = kwargs.get("candidate_id")
        interviewer_obj = TimeSlot.objects.filter(user_id=interviewer_id, user_type="I").first()
        candidate_obj = TimeSlot.objects.filter(user_id=candidate_id, user_type="C").first()
        if candidate_obj:
            candidate_timeslots = get_candidate_time_slots(candidate_obj.available_from_time,
                                                           candidate_obj.available_to_time)
        else:
            candidate_timeslots = []

        matching = []
        for timeslot in candidate_timeslots:
            if timeslot[0] >= interviewer_obj.available_from_time and timeslot[1] <= interviewer_obj.available_to_time:
                matching.append((timeslot[0].strftime("%I:%M %p"),str(timeslot[1].strftime("%I:%M %p"))))
        if matching:
            response["status"] = "success"
            response["message"] = "Matching slots found"
            response["data"] = matching
            return Response(json.dumps(response), status=status.HTTP_200_OK)
        else:
            return Response(json.dumps(response), status=status.HTTP_404_NOT_FOUND)
