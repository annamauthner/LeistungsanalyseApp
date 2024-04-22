from my_classes import Subject, Supervisor, Experiment

def main():
    experiment_name = input("Enter experiment name: ")
    date = input("Enter date of experiment (YYYY-MM-DD): ")

    supervisor_first_name = input("Enter supervisor's first name: ")
    supervisor_last_name = input("Enter supervisor's last name: ")
    supervisor = Supervisor(supervisor_first_name, supervisor_last_name)

    subject_first_name = input("Enter subject's first name: ")
    subject_last_name = input("Enter subject's last name: ")
    subject_sex = input("Enter subject's sex (male/female): ")
    subject_birth_date = input("Enter subject's birth date (YYYY-MM-DD): ")
    subject = Subject(subject_first_name, subject_last_name, subject_sex, subject_birth_date)

    experiment = Experiment(experiment_name, date, supervisor, subject)

    print("Experiment details:")
    print("Experiment name:", experiment.experiment_name)
    print("Date:", experiment.date)
    print("Supervisor:", supervisor.get_full_name())
    print("Subject:", subject.get_full_name())
    print("Estimated Max Heart Rate:", subject.estimate_max_hr())

    experiment.save("experiment.json")

if __name__ == "__main__":
    main()