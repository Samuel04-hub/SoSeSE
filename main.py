from my_functions import build_person, build_experiment

if __name__ == "__main__":
    # Erstelle Supervisor
    supervisor = build_person("Marven", "Otto", "male", 20)
    
    # Erstelle Subject
    subject = build_person("Samuel", "Marxer", "male", 20)
    
    # Erstelle Experiment
    experiment = build_experiment(
        experiment_name="Heart Rate Test 1",
        date="2025-03-24",
        supervisor=supervisor,
        subject=subject
    )
    
    print(experiment)