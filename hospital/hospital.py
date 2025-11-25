from personal import Patient, Doctor
from response import PatientEmergency, DoctorEmergency

pat_anna = Patient("Anna Schmidt", 30, "P12345")
doc_meyer = Doctor("Dr. Meyer", 45, "Cardiology")

response_anna = PatientEmergency("Medical Team A", pat_anna)
response_meyer = DoctorEmergency("Consultation Team B", doc_meyer)
print(pat_anna.get_patient_info())
print(doc_meyer.get_doctor_info())

emergency_participants = [response_anna, response_meyer]
print("\nEmergency Responses:")
for participant in emergency_participants:
    print(participant.dispatch_team("Critical"))
    print(participant.react())  