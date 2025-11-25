from devices import ECGDevice, BloodPressureMonitor

ecg_1 = ECGDevice("ECG Pro", "ECG1001", 12)
bp_monitor_1 = BloodPressureMonitor("BP Monitor X", "BP2001", "Standard Cuff")

# --- Ecapsulation & inner Class Demo ---
print ("--- Ecapsulation & inner Class Demo ---")
ecg_1.switch_on() # call inner class
print(f"Device Info: {ecg_1.get_device_info()}")

device_list = [ecg_1, bp_monitor_1]
for device in device_list:
    print(device.switch_on())
    print(device.perform_measurement())