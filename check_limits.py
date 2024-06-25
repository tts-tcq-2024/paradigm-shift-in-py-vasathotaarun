
def battery_is_ok(temperature, soc, charge_rate):
 return(tempcheck(temperature) and soccheck(soc) and charge_ratecheck(charge_rate))
 
def tempcheck(temperature):
  if temperature < 0 or temperature > 45:
    print('Temperature is out of range!')
    return False
  else:
    return True
def soccheck(soc):
  if soc < 20 or soc > 80:
    print('State of Charge is out of range!')
    return False
  else:
    return True
def charge_rate_check(charge_rate):
  if charge_rate > 0.8:
    print('Charge rate is out of range!')
    return False
  else:
    return True


if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
