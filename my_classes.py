from my_functions import estimate_max_hr

class Person:
    """
    Super class representing a person.
    This class is used as a base for other classes like Subject and Supervisor.
    With the attributes first_name and last_name.
    """
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Subject(Person):
    """
    Class representing a subject in an experiment.
    Inherits from the Person class.
    """
    def __init__(self, first_name, last_name, age, sex):
        super().__init__(first_name, last_name)
        self.__age = age
        self.sex = sex

    def get_age(self):
        return self.__age
    
    def set_max_hr(self):
        """
        Calls the estimate_max_hr function to calculate the maximum heart rate.
        """
        estimate_max_hr2 = estimate_max_hr(self.__age, self.sex)
        return estimate_max_hr2
        
    
class Supervisor(Person):
    """
    Class representing a supervisor in an experiment.
    Inherits from the Person class.
    """
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

    
class Experiment:
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def add_subject(self, subject):
      self.subject = subject

    def add_supervisor(self, supervisor):
      self.supervisor = supervisor

subject1 = Subject("Hauke","Döllefeld", 21, "male")
print(subject1.set_max_hr())