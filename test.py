from my_classes import Subject, Supervisor, Experiment

def main():
    
    # Beispiel-Subject erstellen und über die API senden
    subject = Subject("Julian", "Maier", "male", "1994-07-16", "julian@mail.at")
    subject.put()

    # Beispiel-Email aktualisieren und über die API senden
    subject.email = "juls.maier@mail.at"
    subject.update_email()

    # Beispiel-Experiment erstellen und speichern
    supervisor = Supervisor("Holger", "Schwarz")
    experiment = Experiment("Example Experiment", "2024-05-05", supervisor, subject)
    experiment.save("example_experiment.json")

if __name__ == "__main__":
    main()