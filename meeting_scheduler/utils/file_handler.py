import csv
import json
import os


def save_json(file_path, data):
    folder = os.path.dirname(file_path)

    if folder:
        os.makedirs(folder, exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_json(file_path):
    if not os.path.exists(file_path):
        return []

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def export_text_calendar(file_path, meetings):
    folder = os.path.dirname(file_path)

    if folder:
        os.makedirs(folder, exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write("MEETING CALENDAR\n")
        file.write("================\n\n")

        for meeting in meetings:
            file.write(meeting.get_details())
            file.write("\n\n")


def export_csv_calendar(file_path, meetings):
    folder = os.path.dirname(file_path)

    if folder:
        os.makedirs(folder, exist_ok=True)

    with open(file_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Date", "Start", "End", "Participants"])

        for meeting in meetings:
            writer.writerow([
                meeting.title,
                meeting.time_slot.date,
                meeting.time_slot.start_time,
                meeting.time_slot.end_time,
                ", ".join(meeting.participants)
            ])
