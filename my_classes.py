import json 
from my_functions import estimate_max_hr
from my_functions import build_person


class Person:
    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.max_hr = self.estimate_max_hr()
        
    def estimate_max_hr(self):
        return estimate_max_hr(self.age, self.sex)
    
    def to_dict(self):
        print(self.__dict__) 
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "sex": self.sex,
            "age": self.age
        }

    def save(self, filename):
        with open(filename, "w") as f:
            json.dump(self.to_dict(), f, indent=4)


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
            "supervisor": self.supervisor,
            "subject": self.subject
        }

    def save(self, filename):
        with open(filename, "w") as f:
            json.dump(self.to_dict(), f, indent=4)
         
            


                   
            