class TimeSlot:
    """Class for meeting date and time."""

    def __init__(self, date, start_time, end_time):
        self.date = date
        self.start_time = start_time
        self.end_time = end_time

    def get_time_tuple(self):
        return self.start_time, self.end_time

    def time_to_minutes(self, time_text):
        hours, minutes = time_text.split(":")
        return int(hours) * 60 + int(minutes)

    def is_valid_range(self):
        start = self.time_to_minutes(self.start_time)
        end = self.time_to_minutes(self.end_time)
        return start < end

    def overlaps(self, other):
        if self.date != other.date:
            return False

        start_1 = self.time_to_minutes(self.start_time)
        end_1 = self.time_to_minutes(self.end_time)
        start_2 = self.time_to_minutes(other.start_time)
        end_2 = self.time_to_minutes(other.end_time)

        return start_1 < end_2 and end_1 > start_2

    def to_dict(self):
        return {
            "date": self.date,
            "start_time": self.start_time,
            "end_time": self.end_time
        }

    @staticmethod
    def from_dict(data):
        return TimeSlot(
            data["date"],
            data["start_time"],
            data["end_time"]
        )

    def __str__(self):
        return f"{self.date} {self.start_time}-{self.end_time}"
