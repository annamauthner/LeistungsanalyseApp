from my_classes import Person, Subject, Supervisor, Experiment

def main():
    # Beispiel-Person erstellen und über die API senden
    person = Person("Anna", "Mauthner")
    person.put()

    # Beispiel-Subject erstellen und über die API senden
    subject = Subject("Anna", "Mauthner", "female", "1990-01-01", "anna@mauthner.com")
    subject.put()

    # Beispiel-Email aktualisieren und über die API senden
    subject.email = "jule.trotzki@example.com"
    subject.update_email()

    # Beispiel-Experiment erstellen und speichern
    supervisor = Supervisor("John", "Doe")
    experiment = Experiment("Example Experiment", "2024-04-30", supervisor, subject)
    experiment.save("example_experiment.json")

if __name__ == "__main__":
    main()