from my_functions import estimate_max_hr
class Subject():
    def __init__(self, first_name, last, sex):
      self.first_name = first_name
      self.last_name = last
      self.sex = sex

    def estimate_max_hr(self, age, sex):
      """A function that estimates the maximum heart rate of a subject"""
      return estimate_max_hr(age, sex)

class Supervisor():
    def __init__(self, first_name, last_name):
      self.first_name = first_name
      self.last_name = last_name

class Experiment():
    def __init__(self, name, date):
      self.name = name
      self.data = data

    def add_subject(self, subject):
      self.subject = subject

    def add_supervisor(self, supervisor):
      self.supervisor=supervisor