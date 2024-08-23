import unittest
from battery_monitor import BatteryMonitor
 
class TestBatteryMonitor(unittest.TestCase):
 
    def setUp(self):
        self.monitor = BatteryMonitor()
 
    def test_battery_is_ok(self):
        self.monitor.configure_warnings(temperature=True, soc=True, charge_rate=True)
        self.assertTrue(self.monitor.battery_is_ok(25, 50, 0.5))  # All within range
 
    def test_temperature_out_of_range(self):
        self.monitor.configure_warnings(temperature=True)
        self.assertFalse(self.monitor.battery_is_ok(50, 50, 0.5))  # Temperature out of range
 
    def test_soc_out_of_range(self):
        self.monitor.configure_warnings(soc=True)
        self.assertFalse(self.monitor.battery_is_ok(25, 15, 0.5))  # SOC out of range
 
    def test_charge_rate_out_of_range(self):
        self.monitor.configure_warnings(charge_rate=True)
        self.assertFalse(self.monitor.battery_is_ok(25, 50, 1.0))  # Charge rate out of range
 
    def test_all_parameters_out_of_range(self):
        self.monitor.configure_warnings(temperature=True, soc=True, charge_rate=True)
        self.assertFalse(self.monitor.battery_is_ok(50, 15, 1.0))  # All parameters out of range
 
if __name__ == '__main__':
    unittest.main()
