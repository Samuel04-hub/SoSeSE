from my_functions import set_max_hr

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Subject(Person):
    #Leider muss ich die calculate_age Methode zuerst definieren, damit im Konstuktor kein Fehler auftritt, weil eine Funktion aufgerufen wird, bevor diese definiert wird.
    def calculate_age(self, date_of_birth):
        from datetime import datetime
        today = datetime.today()
        birth_date = datetime.strptime(date_of_birth, "%Y-%m-%d")
        age = today.year - birth_date.year
        # if_schleife kommt null von mir und nur von Chatler
        if today < birth_date.replace(year=today.year):
            age -= 1
        return age
    
    def estimate_max_hr(self, age, sex):
        return set_max_hr(age, sex)
    
    #Der Konstuktor wird leider erst hier auf geführt, damit calculate_age und set_max_hr früher definiert werden können.
    def __init__(self, first_name : str, last_name : str, sex : str, date_of_birth : str):
        super().__init__(first_name, last_name)
        self.sex = sex
        self.__age = self.calculate_age(str(date_of_birth))
        self.__max_hr = self.estimate_max_hr(self.__age, sex)


    def get_age(self):
        return self.__age
    
    def get_max_hr(self):
        return self.__max_hr
        
    
class Supervisor(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

    
class Experiment:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.subject = None
        self.supervisor = None

    def add_subject(self, subject):
      self.subject = subject

    def add_supervisor(self, supervisor):
      self.supervisor = supervisor

    def __str__(self):
        return (
            f"Experiment: {self.name}, Date: {self.date}, "
            f"Subject: {self.subject.first_name} {self.subject.last_name}, "
            f"Supervisor: {self.supervisor.first_name} {self.supervisor.last_name}"
        )