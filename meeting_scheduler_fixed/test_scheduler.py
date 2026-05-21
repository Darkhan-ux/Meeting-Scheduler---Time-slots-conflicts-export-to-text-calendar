import os
import unittest

from meeting import Meeting
from participant import Participant
from time_slot import TimeSlot
from scheduler import Scheduler
from validators import validate_date, validate_email, validate_time


class TestScheduler(unittest.TestCase):

    def test_create_participant(self):
        participant = Participant("Ali", "ali@mail.com")
        self.assertEqual(participant.get_name(), "Ali")
        self.assertEqual(participant.get_email(), "ali@mail.com")

    def test_validate_email(self):
        self.assertTrue(validate_email("test@mail.com"))
        self.assertFalse(validate_email("wrong-email"))

    def test_validate_date(self):
        self.assertTrue(validate_date("2026-05-20"))
        self.assertFalse(validate_date("2026-99-99"))
        self.assertFalse(validate_date("20-05-2026"))

    def test_validate_time(self):
        self.assertTrue(validate_time("14:30"))
        self.assertFalse(validate_time("25:00"))

    def test_add_meeting_without_conflict(self):
        scheduler = Scheduler()

        time_slot = TimeSlot("2026-05-20", "14:00", "15:00")
        meeting = Meeting("Team Meeting", time_slot, ["ali@mail.com"])

        result = scheduler.add_meeting(meeting)

        self.assertTrue(result)
        self.assertEqual(len(scheduler.meetings), 1)

    def test_meeting_conflict(self):
        scheduler = Scheduler()

        time_slot_1 = TimeSlot("2026-05-20", "14:00", "15:00")
        meeting_1 = Meeting("Meeting 1", time_slot_1, ["ali@mail.com"])

        time_slot_2 = TimeSlot("2026-05-20", "14:30", "16:00")
        meeting_2 = Meeting("Meeting 2", time_slot_2, ["ali@mail.com"])

        scheduler.add_meeting(meeting_1)
        result = scheduler.add_meeting(meeting_2)

        self.assertFalse(result)
        self.assertEqual(len(scheduler.meetings), 1)

    def test_no_conflict_for_different_participant(self):
        scheduler = Scheduler()

        time_slot_1 = TimeSlot("2026-05-20", "14:00", "15:00")
        meeting_1 = Meeting("Meeting 1", time_slot_1, ["ali@mail.com"])

        time_slot_2 = TimeSlot("2026-05-20", "14:30", "16:00")
        meeting_2 = Meeting("Meeting 2", time_slot_2, ["dana@mail.com"])

        scheduler.add_meeting(meeting_1)
        result = scheduler.add_meeting(meeting_2)

        self.assertTrue(result)
        self.assertEqual(len(scheduler.meetings), 2)

    def test_save_and_load_data(self):
        scheduler = Scheduler()
        scheduler.add_participant(Participant("Ali", "ali@mail.com"))
        scheduler.add_meeting(Meeting(
            "Team Meeting",
            TimeSlot("2026-05-20", "14:00", "15:00"),
            ["ali@mail.com"]
        ))
        scheduler.save_data()

        loaded_scheduler = Scheduler()
        loaded_scheduler.load_data()

        self.assertEqual(len(loaded_scheduler.participants), 1)
        self.assertEqual(len(loaded_scheduler.meetings), 1)

    def test_export_text_file(self):
        scheduler = Scheduler()

        time_slot = TimeSlot("2026-05-20", "14:00", "15:00")
        meeting = Meeting("Team Meeting", time_slot, ["ali@mail.com"])

        scheduler.add_meeting(meeting)
        scheduler.export_to_text()

        self.assertTrue(os.path.exists("exports/calendar.txt"))


if __name__ == "__main__":
    unittest.main()
