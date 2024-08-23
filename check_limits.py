from utils import calculate_tolerance
 
class BatteryMonitor:
    def __init__(self):
        # Define parameter boundaries and statuses using a list of tuples
        self.parameter_ranges = {
            'soc': [
                (0, 20, 'LOW_SOC_BREACH'),
                (21, 24, 'LOW_SOC_WARNING'),
                (25, 75, 'NORMAL'),
                (76, 80, 'HIGH_SOC_WARNING'),
                (81, 100, 'HIGH_SOC_BREACH')
            ],
            'temperature': [
                (0, 5, 'LOW_TEMP_BREACH'),
                (6, 9, 'LOW_TEMP_WARNING'),
                (10, 40, 'NORMAL'),
                (41, 45, 'HIGH_TEMP_WARNING'),
                (46, 100, 'HIGH_TEMP_BREACH')
            ],
            'charge_rate': [
                (0, 0.7, 'NORMAL'),
                (0.71, 0.8, 'HIGH_CR_WARNING'),
                (0.81, 1.0, 'HIGH_CR_BREACH')
            ]
        }
 
        self.warning_messages = {
            'LOW_SOC_BREACH': 'State of Charge is critically low!',
            'LOW_SOC_WARNING': 'State of Charge is approaching low!',
            'HIGH_SOC_WARNING': 'State of Charge is approaching high!',
            'HIGH_SOC_BREACH': 'State of Charge is critically high!',
            'LOW_TEMP_BREACH': 'Temperature is critically low!',
            'LOW_TEMP_WARNING': 'Temperature is approaching low!',
            'HIGH_TEMP_WARNING': 'Temperature is approaching high!',
            'HIGH_TEMP_BREACH': 'Temperature is critically high!',
            'HIGH_CR_WARNING': 'Charge rate is approaching the limit!',
            'HIGH_CR_BREACH': 'Charge rate is too high!',
            'NORMAL': 'All parameters are within normal range.'
        }
 
    def evaluate_parameter(self, value, param_type):
        # Map the value to the appropriate status based on ranges
        for min_val, max_val, status in self.parameter_ranges[param_type]:
            if min_val <= value <= max_val:
                return status
        return 'UNKNOWN'  # If the value doesn't fit any known range
 
    def translate_status_to_message(self, status):
        # Translate the status to a corresponding warning message
        return self.warning_messages.get(status, 'Unknown status')
 
    def check_battery_status(self, temperature, soc, charge_rate):
        temp_status = self.evaluate_parameter(temperature, 'temperature')
        soc_status = self.evaluate_parameter(soc, 'soc')
        charge_rate_status = self.evaluate_parameter(charge_rate, 'charge_rate')
 
        # Chain the transformations
        temp_message = self.translate_status_to_message(temp_status)
        soc_message = self.translate_status_to_message(soc_status)
        charge_rate_message = self.translate_status_to_message(charge_rate_status)
 
        # Output the messages
        self.output_message(temp_message)
        self.output_message(soc_message)
        self.output_message(charge_rate_message)
 
        # Determine overall battery status
        overall_status = all(status == 'NORMAL' for status in [temp_status, soc_status, charge_rate_status])
        return overall_status
 
    def output_message(self, message):
        # Output the message, this can be modified to log, print, or send elsewhere
        print(message)

if __name__ == '__main__':
    monitor = BatteryMonitor()
    # Example values
    overall_status = monitor.check_battery_status(temperature=42, soc=78, charge_rate=0.76)
    print(f'Overall Battery Status: {"OK" if overall_status else "NOT OK"}')
