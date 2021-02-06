from django.db import models

USER_TYPE=(
    ("I", "Interviewer"),
    ("C", "Candidate")
)


class TimeSlot(models.Model):
    """
    To store interviewer/candidate available time data
    """
    user_type = models.CharField(choices=USER_TYPE, max_length=1)
    user_id = models.CharField(max_length=100)
    available_from_time = models.TimeField()
    available_to_time = models.TimeField()

    def __str__(self):
        return f"{self.user_type} {self.user_id} {self.available_time}"
