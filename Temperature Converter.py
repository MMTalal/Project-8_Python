# Display the title of the script
print("Temperature Conversion Tool")

# Ask the user to input their temperature
temperature = float(input("Input your temperature please: "))

# Ask the user to input the type of their temperature (Celsius, Kelvin, or Fahrenheit)
temperatureType = input("Input the type of your temperature (C, K, or F): ")

# Convert the temperature based on the user's input and display the results in all three temperature scales
if temperatureType == "C" or temperatureType == "c":
    # User input is in Celsius
    print(f"Your temperature is {temperature} Celsius")
    # Convert Celsius to Kelvin
    CelsiusToKelvin = temperature + 273.15
    print(f"Your temperature is {CelsiusToKelvin} Kelvin")
    # Convert Celsius to Fahrenheit
    CelsiusToFahrenheit = (temperature * 1.8) + 32
    print(f"Your temperature is {CelsiusToFahrenheit} Fahrenheit")

elif temperatureType == "K" or temperatureType == "k":
    # User input is in Kelvin
    print(f"Your temperature is {temperature} Kelvin")
    # Convert Kelvin to Celsius
    KelvinToCelsius = temperature - 273.15
    print(f"Your temperature is {KelvinToCelsius} Celsius")
    # Convert Kelvin to Fahrenheit
    KelvinToFahrenheit = ((temperature - 273.15) * 1.8) + 32
    print(f"Your temperature is {KelvinToFahrenheit} Fahrenheit")

elif temperatureType == "F" or temperatureType == "f":
    # User input is in Fahrenheit
    print(f"Your temperature is {temperature} Fahrenheit")
    # Convert Fahrenheit to Celsius
    FahrenheitToCelsius = (temperature - 32) / 1.8
    print(f"Your temperature is {FahrenheitToCelsius:.2f} Celsius")
    # Convert Fahrenheit to Kelvin
    FahrenheitToKelvin = ((temperature - 32) / 1.8) + 273.15
    print(f"Your temperature is {FahrenheitToKelvin:.2f} Kelvin")

# If the user enters an invalid temperature type, display an error message
else:
    print("Error: Invalid temperature type. Please enter 'C', 'K', or 'F'.")
