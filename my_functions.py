import requests
def set_max_hr(age: int , sex : str) -> int:
  """
  See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4124545/ Titel anhand dieser PMC-ID in Citavi-Projekt übernehmen for different formulas
  """
  if sex == "male":
    max_hr_bpm =  223 - 0.9 * age
  elif sex == "female":
    max_hr_bpm = 226 - 1.0 *  age
  else:
    raise ValueError("Invalid sex provided. Use 'male' or 'female'.")
  return int(max_hr_bpm)

def build_person(first_name, last_name, sex, age) -> dict:
    """Returns a dictionary of information about a supervisor or subject."""
    person_dict = { "first_name" : first_name,
             "last_name" : last_name,
             "age" : age,
             "estimate_max_hr" : set_max_hr(age,sex)}
    return person_dict

def build_experiment(experiment_name, date, supervisor, subject) -> dict:
    """Returns a dictionary of information about an experiment."""
    experiment_dict = {"experiment_name" : experiment_name,
            "date" : date,
            "supervisor" :   supervisor,
            "subject" :   subject
            }
    return experiment_dict

def ask_name() -> str:
    """Asks the user for their name."""
    try :
        name = input("What is your name? ")
        return name
    except Exception as e:
        print("Please enter a valid name")
        ask_name()

def ask_number() -> int:
    """Asks the user for a number."""
    try:
        number = int(input("Enter a number: "))
        return number
    except Exception as e:
        print("Please enter a valid number")
        ask_number()

def ask_sex() -> str:
    """Ask the user for the sex"""
    sex_string = input("Enter sex (w/m): ")
    if sex_string == "w":
        return "female"
    elif sex_string == "m":
        return "male"
    else:
        print("Please enter 'w' or 'm'")
        ask_sex()

def delete_person(id: int):
    ## Update a person
    # Define the URL of the API
    url = "http://127.0.0.1:5000/person/" + str(id)

    # Send a POST request to the API
    response = requests.delete(url)

    # Print the response from the server
    print(response.text)