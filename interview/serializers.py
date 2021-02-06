from rest_framework import serializers

from .models import TimeSlot, USER_TYPE


class TimeSlotSerializer(serializers.ModelSerializer):
    """
    serializer class for saving time slots.
    """
    user_type = serializers.ChoiceField(choices=USER_TYPE, help_text="'I' for Interviewer 'C' for candidate")
    user_id = serializers.CharField(help_text="Id of Interviewer/Candidate")
    available_from_time = serializers.CharField(help_text="Available start time of Interviewer/Candidate"                                                      " in 24hr format")
    available_to_time = serializers.CharField(help_text="Available end time of Interviewer/Candidate in 24hr format")

    class Meta:
        model = TimeSlot
        fields = '__all__'
