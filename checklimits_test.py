import unittest
from check_limits import BatteryMonitor

class TestBatteryMonitor(unittest.TestCase):

    def setUp(self):
        self.monitor = BatteryMonitor()

    def test_battery_is_ok(self):
        # Test for a battery that is OK for all parameters
        self.monitor.configure_warnings(temperature=True, soc=True, charge_rate=True)
        self.assertTrue(self.monitor.battery_is_ok(25, 50, 0.5))  # All within acceptable range

        # Test for a battery that is NOT OK due to temperature
        self.assertFalse(self.monitor.battery_is_ok(50, 50, 0.5))  # Temperature is out of range

        # Test for a battery that is NOT OK due to SOC
        self.assertFalse(self.monitor.battery_is_ok(25, 15, 0.5))  # SOC is out of range

        # Test for a battery that is NOT OK due to charge rate
        self.assertFalse(self.monitor.battery_is_ok(25, 50, 1.0))  # Charge rate is out of range
       
        # Test for a battery that is all parameters being out of range
        self.assertFalse(self.monitor.battery_is_ok(50, 15, 1.0))  # All parameters out of range
if __name__ == '__main__':
    unittest.main()
