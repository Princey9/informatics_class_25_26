from personal import Patient, Doctor

class EmergencyResponse:
    """class for emergency response in the hospital system"""   
    def __init__(self, response_team):
        self.response_team = response_team
        
    def dispatch_team(self, emergency_type):
        return f"Dispatching {self.response_team} for {emergency_type} emergency."
    
    def react(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class PatientEmergency(EmergencyResponse):
    """class for patient emergencies"""   
    def __init__(self, response_team, patient):
        super().__init__(response_team)
        self.patient = patient
        
    def react(self):
        return f"Providing immediate medical attention to the patient {self.patient.patient_id}."
    
class DoctorEmergency(EmergencyResponse):
    """class for doctor emergencies"""   
    def __init__(self, response_team, doctor):
        super().__init__(response_team)
        self.doctor = doctor
        
    def react(self):
        return f"Alerting doctor {self.doctor.name} for emergency consultation."