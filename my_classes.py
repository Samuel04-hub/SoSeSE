from my_functions import estimate_max_hr

class Subject:
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.max_hr = self.estimate_max_hr(age, sex)
    
    def estimate_max_hr(self, age, sex):
        """
        Calls the estimate_max_hr function to calculate the maximum heart rate.
        """
        return estimate_max_hr(age, sex)

    
class Supervisor:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    
class Experiment:
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def add_subject(self, subject):
      self.subject = subject

    def add_supervisor(self, supervisor):
      self.supervisor = supervisor