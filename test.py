from my_functions import estimate_max_hr, build_person, build_experiment
import json
from my_classes import Person, Experiment

def main():
    experiment_name = "hr test"
    date = "2024-04-18"
    supervisor_first_name = "Jule"
    supervisor_last_name = "Totzki"
    supervisor_sex = "female"
    supervisor_age = 20
    subject_first_name = "Sunny"
    subject_last_name = "Sonnenschein"
    subject_sex = "female"
    subject_age = 33

    supervisor = Person(supervisor_first_name, supervisor_last_name, supervisor_sex, supervisor_age)
    subject = Person(subject_first_name, subject_last_name, subject_sex, subject_age)

    experiment = Experiment(experiment_name, date, supervisor.to_dict(), subject.to_dict())

    print("Experiment details:")
    print(experiment.__dict__)

    filename = "test_experiment_data.json"
    experiment.save(filename)
    
    
if __name__ == "__main__":
    main()