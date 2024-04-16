from my_classes import Person, Experiment

def main(experiment_name=None, date=None, supervisor_info=None, subject_info=None):
    if experiment_name is None:
        experiment_name = input("Enter experiment name: ")
    if date is None:
        date = input("Enter date of experiment (YYYY-MM-DD): ")
    if supervisor_info is None:
        supervisor_info = {
            "first_name": input("Enter supervisor's first name: "),
            "last_name": input("Enter supervisor's last name: "),
            "age": int(input("Enter supervisor's age: ")),
            "sex": input("Enter supervisor's sex (male/female): ")
        }

    if subject_info is None:
        subject_info = {
            "first_name": input("Enter subject's first name: "),
            "last_name": input("Enter subject's last name: "),
            "age": int(input("Enter subject's age: ")),
            "sex": input("Enter subject's sex (male/female): ")
        }

    supervisor = Person(**supervisor_info)
    subject = Person(**subject_info)

    experiment = Experiment(experiment_name, date, supervisor, subject)

    print("Experiment details:")
    print(experiment.__dict__)

    experiment.save("experiment.json")

if __name__ == "__main__":
    main()