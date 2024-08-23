from utils import is_within_range, is_approaching_limit, calculate_tolerance

class BatteryMonitor:
    def __init__(self):
        self.warning_config = {'temperature': True, 'soc': True, 'charge_rate': True}

    def should_warn(self, limit_type, value, min_val, max_val, tolerance):
        return self.warning_config[limit_type] and is_approaching_limit(value, min_val, max_val, tolerance)

    def check_limits(self, value, min_val, max_val, tolerance, limit_type):
        warning_needed = self.should_warn(limit_type, value, min_val, max_val, tolerance)
        value_ok = is_within_range(value, min_val, max_val)
        return value_ok, warning_needed

    def handle_warnings(self, is_parameter_within_limits, is_approaching_limit_alert, parameter_name):
        if is_approaching_limit_alert:
            print(f'Warning: Approaching {parameter_name} limit')
        elif not is_parameter_within_limits:
            print(f'{parameter_name} is out of range!')

    def battery_is_ok(self, temperature, soc, charge_rate):
        temp_ok, temp_warning = self.check_limits(temperature, 0, 45, calculate_tolerance(45), 'temperature')
        soc_ok, soc_warning = self.check_limits(soc, 20, 80, calculate_tolerance(80), 'soc')
        charge_rate_ok, charge_rate_warning = self.check_limits(charge_rate, None, 0.8, calculate_tolerance(0.8), 'charge_rate')

        self.handle_warnings(temp_ok, temp_warning, 'Temperature')
        self.handle_warnings(soc_ok, soc_warning, 'State of Charge (SOC)')
        self.handle_warnings(charge_rate_ok, charge_rate_warning, 'Charge rate')

        return temp_ok and soc_ok and charge_rate_ok

    def configure_warnings(self, temperature=True, soc=True, charge_rate=True):
        self.warning_config['temperature'] = temperature
        self.warning_config['soc'] = soc
        self.warning_config['charge_rate'] = charge_rate

if __name__ == '__main__':
    monitor = BatteryMonitor()
    monitor.configure_warnings(temperature=False)
