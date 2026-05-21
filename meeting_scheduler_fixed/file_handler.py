import csv
import json
import os
from json import JSONDecodeError


def ensure_folder_exists(file_path):
    """Create parent folder if the path contains one."""
    folder = os.path.dirname(file_path)

    if folder:
        os.makedirs(folder, exist_ok=True)


def save_json(file_path, data):
    ensure_folder_exists(file_path)

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def load_json(file_path):
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except JSONDecodeError:
        return []


def export_text_calendar(file_path, meetings):
    ensure_folder_exists(file_path)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write("MEETING CALENDAR\n")
        file.write("================\n\n")

        if len(meetings) == 0:
            file.write("No meetings yet.\n")
            return

        for meeting in meetings:
            file.write(meeting.get_details())
            file.write("\n\n")


def export_csv_calendar(file_path, meetings):
    ensure_folder_exists(file_path)

    with open(file_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Date", "Start", "End", "Participants", "Type"])

        for meeting in meetings:
            meeting_type = "Online" if hasattr(meeting, "link") else "Offline"
            writer.writerow([
                meeting.title,
                meeting.time_slot.date,
                meeting.time_slot.start_time,
                meeting.time_slot.end_time,
                ", ".join(meeting.participants),
                meeting_type
            ])
