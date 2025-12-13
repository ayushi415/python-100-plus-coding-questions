# convert celsius into fahrenheit 

def convert_temperature(temperature, unit):
    if unit == 'C':
        return (temperature * 9/5) + 32
    elif unit == 'F':
        return (temperature - 32) * 5/9
    else:
        return None
print(convert_temperature(25, 'C'))  # Output: 77.0
print(convert_temperature(77, 'F'))  # Output: 25.0