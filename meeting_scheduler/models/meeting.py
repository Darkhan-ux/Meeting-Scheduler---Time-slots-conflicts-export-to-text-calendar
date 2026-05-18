from models.time_slot import TimeSlot


class Meeting:
    """Base meeting class."""

    def __init__(self, title, time_slot, participants):
        self.title = title
        self.time_slot = time_slot
        self.participants = participants

    def get_details(self):
        names = ", ".join(self.participants)

        return (
            f"Title: {self.title}\n"
            f"Date: {self.time_slot.date}\n"
            f"Time: {self.time_slot.start_time} - {self.time_slot.end_time}\n"
            f"Participants: {names}\n"
            f"Type: Offline meeting"
        )

    def to_dict(self):
        return {
            "type": "offline",
            "title": self.title,
            "time_slot": self.time_slot.to_dict(),
            "participants": self.participants
        }

    @staticmethod
    def from_dict(data):
        time_slot = TimeSlot.from_dict(data["time_slot"])

        return Meeting(
            data["title"],
            time_slot,
            data["participants"]
        )
