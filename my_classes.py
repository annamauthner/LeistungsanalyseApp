import json 
from datetime import datetime
import requests 

# ------------Personen-Klasse ------------------------------------------------------------------------------
class Person:
    def __init__(self, first_name, last_name=None):
        self.first_name = first_name
        self.last_name = last_name

    def to_dict(self):
        print(self.__dict__) 
        return {
            "first_name": self.first_name,
            "last_name": self.last_name}  
        
    def put(self):
        url = "http://127.0.0.1:5000/person/"
        data = {"name": self.first_name}
        data_json = json.dumps(data)
        response = requests.post(url, data=data_json)
        print(response.text)
         
          
#----------Subject-Klasse-----------------------------------------------------------------------------------            
class Subject(Person):
    def __init__(self, first_name, last_name=None, sex=None, birthdate=None, email=None):
        super().__init__(first_name, last_name)
        self.sex = sex 
        self._birthdate = birthdate
        self._age = self.calculate_age()
        self.max_hr_bpm = self.calculate_max_hr()
        self.email = email
        
    def calculate_max_hr(self):
        age = self.calculate_age()
        if self.sex == "male":
            max_hr_bpm = 223 - 0.9 * age
        elif self.sex == "female":
            max_hr_bpm = 226 - 1.0 * age
       
        return int(max_hr_bpm)

    def calculate_age(self):
        today = datetime.today()
        birthdate = datetime.strptime(self._birthdate, "%Y-%m-%d")
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age

    def update_email(self):
        url = f"http://127.0.0.1:5000/person/{self.first_name}"
        data = {"name": self.first_name, "email": self.email}
        data_json = json.dumps(data)
        response = requests.put(url, data=data_json)
        print(response.text)
    
        
    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "sex": self.sex,
            "age": self._age,
            "max_hr_bpm": self.max_hr_bpm,
            "Email-Adresse": self.email}
        
#-----------Supervisor-Klasse------------------------------------------------------------------------------
class Supervisor(Person):

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name}


#------------Experiment-Klasse-----------------------------------------------------------------------------
class Experiment:
    def __init__(self, experiment_name=None, date=None, supervisor=None, subject=None):
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
            
