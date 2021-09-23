# Code snippets to write a function converting temperature units
#   to convert temperature values from Kelvin to either Celcius or Fahrenheit


# 1 to convert temperature values from Kelvin to Celcius and 
def kelvinsToCelsius(tempKelvins):
    return tempKelvins - 273.15

# 2 to convert temperature values from Celcius to Fahrenheit.
def celsiusToFahr(tempCelsius):
    return 9/5 * tempCelsius + 32

# 3 to convert temperature values from Kelvin to Fahrenheit
def kelvinsToFahrenheit(tempKelvins):
    tempCelsius = kelvinsToCelsius(tempKelvins)
    tempFahr = celsiusToFahr(tempCelsius)
    return tempFahr





# Embed the docstring:
    """
    Function for converting temperature in Kelvins to Celsius or Fahrenheit.

    Parameters
    ----------
    tempK: <numerical>
        Temperature in Kelvins
    convertTo: <str>
        Target temperature that can be either Celsius ('C') or Fahrenheit ('F'). Supported values: 'C' | 'F'

    Returns
    -------
    <float>
        Converted temperature.
    """

    
    
    
# 4 Temperature Calculator
#   to convert temperature values from Kelvin to either Celcius or Fahrenheit
def tempCalculator(tempK, convertTo):

    # Check if user wants the temperature in Celsius
    if convertTo == "C":
        # Convert the value to Celsius 
        # using the dedicated function for the task 
        # that we defined above
        convertedTemp = kelvinsToCelsius(tempK)
    elif convertTo == "F":
        # Convert the value to Fahrenheit 
        # using the dedicated function for the task 
        # that we defined above
        convertedTemp = kelvinsToFahrenheit(tempK)
    # Return the result
    return convertedTemp