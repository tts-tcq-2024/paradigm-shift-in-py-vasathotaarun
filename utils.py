def is_within_range(value, min_val, max_val):
    return (min_val is None or value >= min_val) and value <= max_val
 
def is_approaching_limit(value, min_val, max_val, tolerance):
    lower_approaching = min_val is not None and min_val <= value < min_val + tolerance
    upper_approaching = max_val - tolerance < value <= max_val
    return lower_approaching or upper_approaching
 
def calculate_tolerance(value):
    return value * 0.05
