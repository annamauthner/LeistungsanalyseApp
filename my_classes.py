import json
from datetime import datetime
import requests

class Person:
    def __init__(self, first_name, last_name=None):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


    def post(self):
        url = "http://127.0.0.1:5000/person/"
        data = {
          "name": self.first_name
        }
        # Convert the data to JSON format
        data_json = json.dumps(data)
        # Send a POST request to the API
        response = requests.post(url, data=data_json)
        # Print the response from the server
        print(response.text)

class Subject(Person):
    def __init__(self, first_name, last_name=None, sex=None, birth_date=None, email=None):
        super().__init__(first_name, last_name)
        self.sex = sex
        self.email= email

    def estimate_max_hr(self):
        if self.sex == "male":
            return 223 - 0.9 * self._age
        elif self.sex == "female":
            return 226 - 1.0 * self._age
        else:
            return None
        

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "sex": self.sex,
            "age": self._age,
            "max_hr": self.estimate_max_hr()
        }
    
    def update_email(self):
        url = f"http://127.0.0.1:5000/person/{self.first_name}"
        # Convert the data to JSON format
        data = {
            "name": self.first_name,
            "email": self.email
        }
        data_json = json.dumps(data)            
        # Send a POST request to the API
        response = requests.put(url, data=data_json)
        # Print the response from the server
        print(response.text)

# Speichern der Daten
        data = {
             "name": self.first_name,
             "email": self.email
            }
        file_path = "data.json"
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)


if __name__ == "__main__":
    main()