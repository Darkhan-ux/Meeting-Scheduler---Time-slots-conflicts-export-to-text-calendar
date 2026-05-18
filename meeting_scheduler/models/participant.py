class Participant:
    """Class for meeting participant."""

    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def to_dict(self):
        return {
            "name": self.__name,
            "email": self.__email
        }

    @staticmethod
    def from_dict(data):
        return Participant(data["name"], data["email"])

    def __str__(self):
        return f"{self.__name} ({self.__email})"
