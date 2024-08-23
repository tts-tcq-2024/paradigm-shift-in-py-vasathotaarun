import unittest
from battery_monitor import BatteryMonitor
from utils import is_within_range, is_approaching_limit, calculate_tolerance
 
class TestUtils(unittest.TestCase):
    def test_is_within_range(self):
        self.assertTrue(is_within_range(25, 20, 30))
        self.assertFalse(is_within_range(15, 20, 30))
        self.assertTrue(is_within_range(20, 20, 30))  # Edge case: exactly on the lower boundary
        self.assertTrue(is_within_range(30, 20, 30))  # Edge case: exactly on the upper boundary
        self.assertTrue(is_within_range(10, None, 20))  # No lower boundary
        self.assertTrue(is_within_range(30, 20, None))  # No upper boundary
 
    def test_is_approaching_limit(self):
        self.assertTrue(is_approaching_limit(22, 20, 30, 3))  # Approaching lower limit
        self.assertTrue(is_approaching_limit(28, 20, 30, 3))  # Approaching upper limit
        self.assertFalse(is_approaching_limit(25, 20, 30, 3))  # Well within the range
 
    def test_calculate_tolerance(self):
        self.assertEqual(calculate_tolerance(100), 5)  # Default 5% tolerance
        self.assertEqual(calculate_tolerance(100, 10), 10)  # 10% tolerance
        self.assertEqual(calculate_tolerance(50, 20), 10)  # 20% tolerance
 
class TestBatteryMonitor(unittest.TestCase):
    def setUp(self):
        self.monitor = BatteryMonitor()
 
    def test_evaluate_parameter(self):
        # Test SOC evaluations
        self.assertEqual(self.monitor.evaluate_parameter(10, 'soc'), 'LOW_SOC_BREACH')
        self.assertEqual(self.monitor.evaluate_parameter(22, 'soc'), 'LOW_SOC_WARNING')
        self.assertEqual(self.monitor.evaluate_parameter(50, 'soc'), 'NORMAL')
        self.assertEqual(self.monitor.evaluate_parameter(78, 'soc'), 'HIGH_SOC_WARNING')
        self.assertEqual(self.monitor.evaluate_parameter(90, 'soc'), 'HIGH_SOC_BREACH')
        # Test temperature evaluations
        self.assertEqual(self.monitor.evaluate_parameter(3, 'temperature'), 'LOW_TEMP_BREACH')
        self.assertEqual(self.monitor.evaluate_parameter(8, 'temperature'), 'LOW_TEMP_WARNING')
        self.assertEqual(self.monitor.evaluate_parameter(25, 'temperature'), 'NORMAL')
        self.assertEqual(self.monitor.evaluate_parameter(43, 'temperature'), 'HIGH_TEMP_WARNING')
        self.assertEqual(self.monitor.evaluate_parameter(50, 'temperature'), 'HIGH_TEMP_BREACH')
 
        # Test charge rate evaluations
        self.assertEqual(self.monitor.evaluate_parameter(0.5, 'charge_rate'), 'NORMAL')
        self.assertEqual(self.monitor.evaluate_parameter(0.75, 'HIGH_CR_WARNING'))
        self.assertEqual(self.monitor.evaluate_parameter(0.85, 'charge_rate'), 'HIGH_CR_BREACH')
 
    def test_translate_status_to_message(self):
        self.assertEqual(self.monitor.translate_status_to_message('LOW_SOC_BREACH'), 'State of Charge is critically low!')
        self.assertEqual(self.monitor.translate_status_to_message('HIGH_TEMP_WARNING'), 'Temperature is approaching high!')
        self.assertEqual(self.monitor.translate_status_to_message('NORMAL'), 'All parameters are within normal range.')
        self.assertEqual(self.monitor.translate_status_to_message('UNKNOWN'), 'Unknown status')
 
    def test_battery_is_ok(self):
        # Normal conditions
        self.assertTrue(self.monitor.check_battery_status(25, 50, 0.5))
        # Warning conditions
        self.assertFalse(self.monitor.check_battery_status(43, 78, 0.75))
        # Breach conditions
        self.assertFalse(self.monitor.check_battery_status(50, 10, 0.9))
 
if __name__ == '__main__':
    unittest.main()
