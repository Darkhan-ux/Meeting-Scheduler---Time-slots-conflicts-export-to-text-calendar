import sys

from meeting import Meeting
from online_meeting import OnlineMeeting
from participant import Participant
from time_slot import TimeSlot
from scheduler import Scheduler
from validators import (
    validate_date,
    validate_email,
    validate_name,
    validate_time
)


def input_participant():
    name = input("Enter participant name: ").strip()
    email = input("Enter participant email: ").strip()

    if not validate_name(name):
        print("Invalid name. Name must contain at least 2 characters.")
        return None

    if not validate_email(email):
        print("Invalid email.")
        return None

    return Participant(name, email)


def input_time_slot():
    date = input("Enter date (YYYY-MM-DD): ").strip()
    start_time = input("Enter start time (HH:MM): ").strip()
    end_time = input("Enter end time (HH:MM): ").strip()

    if not validate_date(date):
        print("Invalid date. Use a real date in YYYY-MM-DD format.")
        return None

    if not validate_time(start_time) or not validate_time(end_time):
        print("Invalid time. Use HH:MM format, for example 09:30 or 18:45.")
        return None

    time_slot = TimeSlot(date, start_time, end_time)

    if not time_slot.is_valid_range():
        print("Start time must be earlier than end time.")
        return None

    return time_slot


def input_meeting(scheduler):
    if len(scheduler.participants) == 0:
        print("Please add at least one participant before creating a meeting.")
        return None

    title = input("Enter meeting title: ").strip()

    if len(title) < 2:
        print("Meeting title must contain at least 2 characters.")
        return None

    time_slot = input_time_slot()

    if time_slot is None:
        return None

    print("Available participants:")
    scheduler.show_all_participants()

    emails_text = input("Enter participant emails separated by comma: ")
    emails = []

    for email in emails_text.split(","):
        clean_email = email.strip()

        if clean_email != "":
            emails.append(clean_email)

    if len(emails) == 0:
        print("Meeting must have at least one participant.")
        return None

    for email in emails:
        if not validate_email(email):
            print(f"Invalid participant email: {email}")
            return None

        if scheduler.find_participant_by_email(email) is None:
            print(f"Participant not found: {email}")
            return None

    meeting_type = input("Online meeting? yes/no: ").strip().lower()

    if meeting_type == "yes":
        link = input("Enter meeting link: ").strip()

        if len(link) == 0:
            print("Online meeting link cannot be empty.")
            return None

        return OnlineMeeting(title, time_slot, emails, link)

    return Meeting(title, time_slot, emails)


def show_menu():
    print()
    print("===== Meeting Scheduler =====")
    print("1. Add participant")
    print("2. Create meeting")
    print("3. Show all participants")
    print("4. Show all meetings")
    print("5. Show meetings by date")
    print("6. Show meetings by participant")
    print("7. Export calendar to text file")
    print("8. Export calendar to CSV file")
    print("9. Save data")
    print("10. Load data")
    print("11. Show meeting titles")
    print("0. Exit")


def main():
    scheduler = Scheduler()
    scheduler.load_data()

    while True:
        show_menu()
        choice = input("Choose option: ").strip()

        if choice == "1":
            participant = input_participant()

            if participant is not None:
                added = scheduler.add_participant(participant)

                if added:
                    scheduler.save_data()
                    print("Participant added and saved.")
                else:
                    print("Participant with this email already exists.")

        elif choice == "2":
            meeting = input_meeting(scheduler)

            if meeting is not None:
                added = scheduler.add_meeting(meeting)

                if added:
                    scheduler.save_data()
                    print("Meeting created and saved.")
                else:
                    print("Time conflict found. Meeting was not created.")

        elif choice == "3":
            scheduler.show_all_participants()

        elif choice == "4":
            scheduler.show_all_meetings()

        elif choice == "5":
            date = input("Enter date (YYYY-MM-DD): ").strip()

            if not validate_date(date):
                print("Invalid date. Use a real date in YYYY-MM-DD format.")
                continue

            meetings = list(scheduler.meetings_by_date(date))

            if len(meetings) == 0:
                print("No meetings found for this date.")
            else:
                for meeting in meetings:
                    print(meeting.get_details())
                    print("-" * 30)

        elif choice == "6":
            email = input("Enter participant email: ").strip()
            meetings = scheduler.get_meetings_by_participant(email)

            if len(meetings) == 0:
                print("No meetings found.")
            else:
                for meeting in meetings:
                    print(meeting.get_details())
                    print("-" * 30)

        elif choice == "7":
            scheduler.export_to_text()
            print("Calendar exported to exports/calendar.txt")

        elif choice == "8":
            scheduler.export_to_csv()
            print("Calendar exported to exports/calendar.csv")

        elif choice == "9":
            scheduler.save_data()
            print("Data saved.")

        elif choice == "10":
            scheduler.load_data()
            print("Data loaded.")

        elif choice == "11":
            titles = scheduler.get_meeting_titles()
            print(titles)

        elif choice == "0":
            scheduler.save_data()
            print("Data saved. Goodbye!")
            sys.exit()

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
