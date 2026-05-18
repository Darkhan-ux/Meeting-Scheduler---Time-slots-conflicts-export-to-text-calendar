# Meeting Scheduler System

## Project Description

Meeting Scheduler System is a simple Python console application for creating and managing meetings.

The program can:

- add participants;
- create offline and online meetings;
- check time conflicts;
- show all meetings;
- show meetings by date;
- show meetings by participant;
- save and load data using JSON;
- export calendar to TXT and CSV files.

## Project Structure

```text
meeting_scheduler/
│
├── main.py
├── README.md
├── requirements.txt
│
├── models/
│   ├── participant.py
│   ├── time_slot.py
│   ├── meeting.py
│   └── online_meeting.py
│
├── services/
│   └── scheduler.py
│
├── utils/
│   ├── validators.py
│   ├── decorators.py
│   └── file_handler.py
│
├── tests/
│   └── test_scheduler.py
│
├── data/
└── exports/
```

## Class Hierarchy and OOP

### Participant

Stores participant name and email.

Uses encapsulation:

- `__name`
- `__email`

### TimeSlot

Stores meeting date, start time, and end time.

Also checks time overlap.

### Meeting

Base class for offline meetings.

### OnlineMeeting

Child class of Meeting.

This shows inheritance.

### Scheduler

Main manager class.

It stores participants and meetings.

This shows association, because Scheduler manages other objects.

## Advanced OOP

### Encapsulation

Participant has private fields.

### Inheritance

OnlineMeeting inherits from Meeting.

### Association

Scheduler has lists of participants and meetings.

### Polymorphism

Meeting and OnlineMeeting both have `get_details()`, but they return different information.

## Collections

The project uses:

- list for participants and meetings;
- dict for JSON data;
- tuple in TimeSlot;
- set for unique participant emails.

## Functional Programming

The project uses:

- lambda;
- map;
- filter.

Examples are in `services/scheduler.py`.

## Decorator

The project uses custom decorator `@log_action`.

It is located in:

```text
utils/decorators.py
```

## Generator

The project uses generator method:

```python
meetings_by_date()
```

It is located in:

```text
services/scheduler.py
```

## Regex

The project uses `re` module for validation:

- email validation;
- date validation;
- time validation.

File:

```text
utils/validators.py
```

## File I/O

The project uses:

- JSON for saving and loading data;
- CSV for calendar export;
- TXT for calendar export;
- os module for creating folders.

## How to Run

Open terminal in the project folder and run:

```bash
python main.py
```

## How to Run Tests

```bash
python -m unittest discover tests
```

## Team Roles

Member 1: Participant and TimeSlot classes.

Member 2: Meeting and OnlineMeeting classes.

Member 3: Scheduler and conflict checking.

Member 4: File handling, validation, and decorators.

Member 5: Main menu, tests, and README.

## Notes

This project is a simple first version. It can be improved later with a graphical interface, database, reminders, and calendar API integration.
