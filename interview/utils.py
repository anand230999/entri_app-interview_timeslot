from datetime import time


def get_candidate_time_slots(start_time, end_time):
    """
    split time range in to 1hr slots
    """
    result = []
    prev_time_slot = ""
    end_time = time(hour=end_time.hour + 1, minute=end_time.minute)
    start_time = time(hour=start_time.hour - 1, minute=start_time.minute)
    while True:
        if not prev_time_slot:
            prev_time_slot = start_time
        timeslot = time(hour=prev_time_slot.hour+1, minute=prev_time_slot.minute)
        if end_time >= timeslot:
            result.append((prev_time_slot, timeslot))
            prev_time_slot = timeslot
        else:
            break
    return result
