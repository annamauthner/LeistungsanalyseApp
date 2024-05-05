from my_classes import Subject, Supervisor, Experiment


def main():
    
    # Beispiel-Subject erstellen und über die API senden
    subject = Subject("Matthias", "Hauck", "male", "1994-07-16", "Matze@mail.at")
    subject.put()

    # Beispiel-Email aktualisieren und über die API senden
    subject.email = "mathhias.hauck@mail.at"
    subject.update_email()

    # Beispiel-Experiment erstellen und speichern
    supervisor = Supervisor("Holger", "Schwarz")
    experiment = Experiment("Example Experiment", "2024-05-05", supervisor, subject)
    experiment.save("data.json")
    

if __name__ == "__main__":
    main()
    

