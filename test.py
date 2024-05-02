from my_classes import Person, Subject, Supervisor, Experiment

def main():
    # Erstelle eine Person und rufe die put-Methode auf
    person = Person("John", "Doe")
    person.put()

    # Erstelle ein Subjekt und aktualisiere die E-Mail-Adresse
    subject = Subject("Jane", "Doe", "female", "1990-01-01", "jane@example.com")
    subject.update_email()

    # Erstelle einen Supervisor
    supervisor = Supervisor("Alice", "Smith")

    # Erstelle ein Experiment mit den erstellten Objekten
    experiment = Experiment("Experiment 1", "2024-04-30", supervisor, subject)

    # Speichere das Experiment in einer JSON-Datei
    experiment.save("experiment_data.json")

if __name__ == "__main__":
    main()