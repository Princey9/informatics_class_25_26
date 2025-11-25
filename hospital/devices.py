class MedicalDevice:
    """class for medical devices in the hospital system"""   
    def __init__(self, device_name, device_id):
        self.device_name = device_name
        self.__device_id = device_id
        self.__status = "Off"
        
        #Instatiate the Inner Class: the calibration unit belongs to the device
        self.calibration_unit = self.CalibrationUnit()
        
    def get_device_info(self):
        return f"Device ID: {self.device_id}, Device Name: {self.device_name}"
    
    # Encapsulation: Getter (read-only property) for device id
    @property
    def device_id(self):
        return self.__device_id 
    
    # Encapsulation: change status
    def switch_on(self):
        if self.__status == "Off":
            self.__status = "On"
            self.calibration_unit.check_calibration
            return f"{self.device_name} is now On."
        else:
            return f"{self.device_name} is already On."
        
    # Polymorphic mehtod (must be overridden in subclasses))
    def perform_measurement(self):
        raise NotImplementedError("Subclasses must implement this method")
        
    # --- inner class ---
    class CalibrationUnit:
        """inner class for device calibration unit"""   
        def __init__(self):
            self.last_check = "2025-11-25"
            
        def check_calibration(self):
            return f"Last calibration check was on {self.last_check}."


class ECGDevice(MedicalDevice):
    """class for ECG medical device"""   
    def __init__(self, device_name, device_id, electrode_count):
        super().__init__(device_name, device_id)
        self.electrode_count = electrode_count
        
    def perform_measurement(self):
        if self._MedicalDevice__status == "On":
            result = f"Heart Ragte: 72 bpm, Rhythm: Normal Sinus Rhythm"
            return f"ECG Device {self.device_id} measures with {self.electrode_count} electrodes. Result: {result}"
        else:
            return f"Cannot perform measurement. {self.device_name} is Off."
        
class BloodPressureMonitor(MedicalDevice):
    """class for Blood Pressure Monitor device"""   
    def __init__(self, device_name, device_id, cuff_type):
        super().__init__(device_name, device_id)
        self.cuff_type = cuff_type
        
    def perform_measurement(self):
        if self._MedicalDevice__status == "On":
            result = f"Systolic: 120 mmHg, Diastolic: 80 mmHg"
            return f"Blood Pressure Monitor {self.device_id} measures. Result: {result}"
        else:
            return f"Cannot perform measurement. {self.device_name} is Off."