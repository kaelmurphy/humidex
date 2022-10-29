# Kael Murphy
# COMP 1026B ASSIGNMENT 1
# Windchill and humidex calculator
import math

# created a testable variable for the while loop
runAgain = 'y'

# while loop that will run if prompted by the users input for runAgain
while runAgain == 'y':

    # gathers input from the user for the air temperature
    airTemp = float(input('Enter a temperature between -50 and 50: '))

    # ensures that the user inputs a temperature between -50 and 50
    while -50 > airTemp or airTemp > 50:
        print('That temperature is invalid.')
        airTemp = float(input('Enter a temperature between -50 and 50: '))

    # if statement allows me to separate windchill and humidex calculations
    if airTemp <= 0:

        # gathers input from the user for windspeed
        print('Calculating windchill.')
        windSpeed = float(input('Enter a wind speed between 1 and 99 km/h: '))
        # ensures that the user inputs a valid windspeed

        while windSpeed < 1 or windSpeed > 99:
            print('That wind speed is invalid.')
            windSpeed = float(input('Enter a wind speed between 1 and 99 km/h: '))

        # creates a variable with the value of windspeed
        feelsLike = 13.12 + (0.6125*airTemp) - (11.37 * windSpeed ** 0.16) + ((0.3965*airTemp) * (windSpeed ** 0.16))
        feelsLike = round(feelsLike)

        # tests what the value of the windspeed is and pairs it with the appropriate response
        if feelsLike <= -40:
            print('The windchill is {}. Very High Risk. Skin can freeze in under 10 minutes.'.format(
                feelsLike))
        elif feelsLike <= -28:
            print('The windchill is {}. High Risk. Skin can freeze in 10-30 minutes.'.format(feelsLike))
        elif feelsLike <= -10:
            print('The windchill is {}. Moderate risk.'.format(feelsLike))
        else:
            print('The windchill is {}. Low risk.'.format(feelsLike))

    # if the air temperature that was input >=20 then this section will calculate humidex
    elif airTemp >= 20:

        print('Calculating humidex.')
        # gathers input from the user for the value of the dew point
        dewPoint = float(input('Enter the dewpoint between -50 and 50: '))

        # ensures that the user selects a valid dewpoint
        while dewPoint > airTemp or dewPoint < -50:
            print('That dew point is invalid.')
            dewPoint = float(input('Enter the dewpoint between -50 and 50: '))

        # calculations for the dewpoint using two variables
        F = 6.11 * (math.exp(5417.7530 * ((1 / 273.16) - (1 / (273.16 + dewPoint)))))
        G = (5 / 9) * (F - 10)

        # creates a testable variable that can be used in an if statement
        feelsLike = airTemp + G
        feelsLike = round(feelsLike)

        # tests the value of the humidex and pairs it with the appropriate response
        if feelsLike > 45:
            print('The humidex is {}. Dangerous. Heat stroke possible.'.format(feelsLike))
        elif feelsLike >= 40:
            print('The humidex is {}. Great discomfort. Avoid exertion.'.format(feelsLike))
        elif feelsLike >= 30:
            print('The humidex is {}. Some discomfort.'.format(feelsLike))
        else:
            print('The humidex is {}. Little or no discomfort.'.format(feelsLike))

    # if the user inputs a value 0 < x < 20 then no calculations need to be made
    else:
        print('Windchill and humidex are not a factor at this temperature.')

    # gives the variable tested in the main while loop a new value
    # if the answer is y the program will run again, if the answer is n the program stops
    runAgain = input('Check another weather condition (Y/N)? ').lower()

    # ensures that the user inputs a valid answer to the question
    while runAgain != 'y' and runAgain != 'n':
        print('That input is invalid.')
        runAgain = input('Check another weather condition (Y/N)? ').lower()
