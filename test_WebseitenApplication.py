#Test-Datei für die Webseiten-Application Aufgabe 8
from my_classes import Person, Subject

if __name__ == "__main__":
    s1 = Person("Jann", "Soph")
    Person.post(s1)
    #wieso klappt das hier nicht
    # s1.post()

    s2 = Subject("Jann", "Soph", "female", "2000-01-01", "jann@soph.de")
    Subject.update_email(s2)