import json
from my_classes import Person, Experiment, Supervisor, Subject

def main():
    experiment_name = input("Enter experiment name: ")
    date = input("Enter date of experiment (YYYY-MM-DD): ")
    supervisor_first_name = input("Enter supervisor's first name: ")
    supervisor_last_name = input("Enter supervisor's last name: ")
    subject_first_name = input("Enter subject's first name: ")
    subject_last_name = input("Enter subject's last name: ")
    subject_sex = input("Enter subject's sex (male/female): ")
    subject_birthdate = input("Enter subject's birthdate (YYYY-MM-DD): ")
    subject_email = input("Enter subject's email: ")

    supervisor = Supervisor(supervisor_first_name, supervisor_last_name)
    subject = Subject(subject_first_name, subject_last_name, subject_sex, subject_birthdate, subject_email)

    experiment = Experiment(experiment_name, date, supervisor, subject)

    print("Experiment details:")
    print(experiment.__dict__)

    filename = "experiment_data.json"
    experiment.save(filename)
    
    
if __name__ == "__main__":
    main()