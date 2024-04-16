import json

class Person:
    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.max_hr = self.estimate_max_hr()

    def estimate_max_hr(self):
        if self.sex == "male":
            return 223 - 0.9 * self.age
        elif self.sex == "female":
            return 226 - 1.0 * self.age
        else:
            return None

    def save(self, filename):
        with open(filename, "w") as f:
            json.dump(self.__dict__,f)

class Experiment:
    def __init__(self, experiment_name, date, supervisor, subject):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor.__dict__
        self.subject = subject.__dict__

    def save(self, filename):
        with open(filename, "w") as f:
            json.dump(self.__dict__, f)