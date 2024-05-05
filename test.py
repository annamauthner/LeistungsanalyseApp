from my_classes import Subject, Person
import json

def main():

    # Neues Subject-Objekt mit dem eingegebenen Vornamen erstellen und auf dem Server anlegen
    subject = Subject("Max")
    subject.post()

    # E-Mail-Adresse aktualisieren
    subject.email = "max.mustermann@gmail.com"
    subject.update_email()

# Speichern der Daten im data.json
    data = {
        "name": "Max",
        "email": "max.mustermann@gmail.com"
    }
    # Dateipfad, in dem die JSON-Daten gespeichert werden sollen
    file_path = "data.json"
    # JSON-Daten in die Datei schreiben
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    main()