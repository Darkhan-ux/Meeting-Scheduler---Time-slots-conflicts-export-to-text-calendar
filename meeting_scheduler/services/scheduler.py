from models.meeting import Meeting
from models.online_meeting import OnlineMeeting
from models.participant import Participant
from utils.decorators import log_action
from utils.file_handler import (
    export_csv_calendar,
    export_text_calendar,
    load_json,
    save_json
)


class Scheduler:
    """Main class for managing participants and meetings."""

    def __init__(self):
        self.participants = []
        self.meetings = []

    @log_action
    def add_participant(self, participant):
        if self.find_participant_by_email(participant.get_email()) is not None:
            return False

        self.participants.append(participant)
        return True

    def find_participant_by_email(self, email):
        for participant in self.participants:
            if participant.get_email() == email:
                return participant

        return None

    def get_participant_emails(self):
        emails = set()

        for participant in self.participants:
            emails.add(participant.get_email())

        return emails

    @log_action
    def add_meeting(self, meeting):
        if self.has_conflict(meeting):
            return False

        self.meetings.append(meeting)
        return True

    def has_conflict(self, new_meeting):
        for old_meeting in self.meetings:
            if old_meeting.time_slot.overlaps(new_meeting.time_slot):
                for email in new_meeting.participants:
                    if email in old_meeting.participants:
                        return True

        return False

    def show_all_participants(self):
        if len(self.participants) == 0:
            print("No participants yet.")
            return

        for participant in self.participants:
            print(participant)

    def show_all_meetings(self):
        if len(self.meetings) == 0:
            print("No meetings yet.")
            return

        for meeting in self.meetings:
            print(meeting.get_details())
            print("-" * 30)

    def meetings_by_date(self, date):
        for meeting in self.meetings:
            if meeting.time_slot.date == date:
                yield meeting

    def get_meeting_titles(self):
        return list(map(lambda meeting: meeting.title, self.meetings))

    def get_meetings_by_participant(self, email):
        result = filter(
            lambda meeting: email in meeting.participants,
            self.meetings
        )

        return list(result)

    def save_data(self):
        participant_data = []

        for participant in self.participants:
            participant_data.append(participant.to_dict())

        meeting_data = []

        for meeting in self.meetings:
            meeting_data.append(meeting.to_dict())

        save_json("data/participants.json", participant_data)
        save_json("data/meetings.json", meeting_data)

    def load_data(self):
        participant_data = load_json("data/participants.json")
        meeting_data = load_json("data/meetings.json")

        self.participants = []

        for item in participant_data:
            self.participants.append(Participant.from_dict(item))

        self.meetings = []

        for item in meeting_data:
            if item["type"] == "online":
                self.meetings.append(OnlineMeeting.from_dict(item))
            else:
                self.meetings.append(Meeting.from_dict(item))

    def export_to_text(self):
        export_text_calendar("exports/calendar.txt", self.meetings)

    def export_to_csv(self):
        export_csv_calendar("exports/calendar.csv", self.meetings)
