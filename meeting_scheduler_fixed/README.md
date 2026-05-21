# Meeting Scheduler System

This is a simple Python console application for managing meetings.

## Main Features

- Add participants
- Create offline meetings
- Create online meetings
- Check meeting time conflicts
- Show all participants
- Show all meetings
- Show meetings by date
- Show meetings by participant
- Automatically save and load data using JSON
- Export calendar to TXT and CSV files
- Run unit tests

## Project Files

```text
main.py            - starts the program and shows the menu
scheduler.py       - main manager class
participant.py     - participant model
meeting.py         - offline meeting class
online_meeting.py  - online meeting class inherited from Meeting
time_slot.py       - meeting date and time model
validators.py      - input validation
file_handler.py    - JSON/TXT/CSV file operations
decorators.py      - log decorator
test_scheduler.py  - unit tests
requirements.txt   - project dependencies
```

## How to Run

```bash
python main.py
```

## How to Run Tests

```bash
python -m unittest test_scheduler.py -v
```

## Notes

This project uses only built-in Python libraries, so `requirements.txt` is empty.
The `data` and `exports` folders are created automatically.

The project demonstrates:

- Object-Oriented Programming
- Encapsulation
- Inheritance
- Decorators
- Validation
- JSON file handling
- CSV/TXT export
- Lambda, map, filter
- Generator function
- Unit testing
