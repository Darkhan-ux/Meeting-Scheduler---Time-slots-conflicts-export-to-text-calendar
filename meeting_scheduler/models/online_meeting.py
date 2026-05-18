from models.meeting import Meeting
from models.time_slot import TimeSlot


class OnlineMeeting(Meeting):
    """Online meeting class."""

    def __init__(self, title, time_slot, participants, link):
        super().__init__(title, time_slot, participants)
        self.link = link

    def get_details(self):
        names = ", ".join(self.participants)

        return (
            f"Title: {self.title}\n"
            f"Date: {self.time_slot.date}\n"
            f"Time: {self.time_slot.start_time} - {self.time_slot.end_time}\n"
            f"Participants: {names}\n"
            f"Type: Online meeting\n"
            f"Link: {self.link}"
        )

    def to_dict(self):
        return {
            "type": "online",
            "title": self.title,
            "time_slot": self.time_slot.to_dict(),
            "participants": self.participants,
            "link": self.link
        }

    @staticmethod
    def from_dict(data):
        time_slot = TimeSlot.from_dict(data["time_slot"])

        return OnlineMeeting(
            data["title"],
            time_slot,
            data["participants"],
            data["link"]
        )
