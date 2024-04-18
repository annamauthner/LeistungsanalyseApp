from my_functions import estimate_max_hr, build_person, build_experiment
import json
from my_classes import Person, Experiment

def main():
    experiment_name = input("Enter experiment name: ")
    date = input("Enter date of experiment (YYYY-MM-DD): ")
    supervisor_first_name = input("Enter supervisor's first name: ")
    supervisor_last_name = input("Enter supervisor's last name: ")
    supervisor_sex = input("Enter supervisor's sex (male/female): ")
    supervisor_age = int(input("Enter supervisor's age: "))
    subject_first_name = input("Enter subject's first name: ")
    subject_last_name = input("Enter subject's last name: ")
    subject_sex = input("Enter subject's sex (male/female): ")
    subject_age = int(input("Enter subject's age: "))

    supervisor = Person(supervisor_first_name, supervisor_last_name, supervisor_sex, supervisor_age)
    subject = Person(subject_first_name, subject_last_name, subject_sex, subject_age)

    experiment = Experiment(experiment_name, date, supervisor.to_dict(), subject.to_dict())

    print("Experiment details:")
    print(experiment.__dict__)

    filename = "experiment_data.json"
    experiment.save(filename)
    
    
if __name__ == "__main__":
    main()