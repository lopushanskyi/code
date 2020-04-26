""" Simple BMI Calculator """


def bmi():
    """ function that input weight and height and output
    BMI calculations """

    while True:
        try:
            weight = float(input('Enter your weight: '))
            height = float(input('Enter your height: '))
            if height > 2.5:
                height /= 100
            result = weight / height**2
            """ print calculation """
            print(f'Your BMI is: {result:.2f} kg/sq.m')
            """ print additional information """
            if 16 <= result <= 17:
                print('Moderate Thinness')
            elif 17 < result <= 18.5:
                print('Mild Thinness')
            elif 18.5 < result <= 25:
                print('Normal')
            elif 25 < result <= 30:
                print('Overweight')
            elif 30 < result <= 35:
                print('Obese Class I')
            elif 35 < result <= 40:
                print('Obese Class II')
            elif result > 40:
                print('Obese Class III')
            break

        except TypeError:
            """ if user input String instead Numbers """
            print('Use only numbers. Try again')
            continue

        except ValueError:
            """ if user input a few Numbers """
            print('It is not a number. Try again')
            continue


bmi()
