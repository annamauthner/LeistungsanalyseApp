from my_functions import estimate_max_hr, build_person, build_experiment
import json

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

    supervisor = build_person(supervisor_first_name, supervisor_last_name, supervisor_sex, supervisor_age)
    subject = build_person(subject_first_name, subject_last_name, subject_sex, subject_age)

    experiment = build_experiment(experiment_name, date, supervisor, subject)

    print("Experiment details:")
    print(experiment)

    with open("experiment.json", "w") as outfile:
        json.dump(experiment, outfile, indent=4)

if __name__ == "__main__":
    main()