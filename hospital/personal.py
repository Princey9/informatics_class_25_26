class Person:
    """base class for a person in the hospital system"""   
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def introduce(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."  
    
class Patient(Person):
    """class for a patient in the hospital system"""   
    def __init__(self, name, age, patient_id):
        super().__init__(name, age)
        self.patient_id = patient_id
        
    def get_patient_info(self):
        return f"Patient ID: {self.patient_id}, Name: {self.name}, Age: {self.age}"
    
class Doctor(Person):
    """class for a doctor in the hospital system"""   
    def __init__(self, name, age, specialty):
        super().__init__(name, age)
        self.specialty = specialty
        
    def get_doctor_info(self):
        return f"Doctor Name: {self.name}, Age: {self.age}, Specialty: {self.specialty}"
