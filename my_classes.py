import json
from datetime import datetime

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

class Subject(Person):
    def __init__(self, first_name, last_name, sex, birth_date):
        super().__init__(first_name, last_name)
        self.sex = sex
        self._birth_date = birth_date
        self._age = self.calculate_age()

    def estimate_max_hr(self):
        if self.sex == "male":
            return 223 - 0.9 * self._age
        elif self.sex == "female":
            return 226 - 1.0 * self._age
        else:
            return None

    def calculate_age(self):
        today = datetime.today()
        birth_date = datetime.strptime(self._birth_date, "%Y-%m-%d")
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "sex": self.sex,
            "age": self._age,
            "max_hr": self.estimate_max_hr()
        }

class Supervisor(Person):
    def to_dict(self):
        return {"full_name": self.get_full_name()}

class Experiment:
    def __init__(self, experiment_name, date, supervisor, subject):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject

    def to_dict(self):
        return {
            "experiment_name": self.experiment_name,
            "date": self.date,
            "supervisor": self.supervisor.to_dict(),
            "subject": self.subject.to_dict()
        }

    def save(self, filename):
        with open(filename, "w") as f:
            json.dump(self.to_dict(), f, indent=4)