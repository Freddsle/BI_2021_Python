# simple units converter

def get_value_to_convert():
    """Reads the string and checks is it possible to convert it to a float number."""
    value_to_convert = None

    while True:
        value_to_convert = input('Now, please enter a value (only numbers): ')

        try:
            value_to_float = float(value_to_convert)
        except ValueError:
            print('Oops, It`s not a float number. Try again.')
        else:
            return value_to_float


def value_to_standart(value_to_convert, units):
    """
    Convert units to CelCelsius
    """

    if units == 'Celsius' or units == 'C':
        return value_to_convert

    if units == 'Kelvin' or units == 'K':
        return value_to_convert - 273.15

    if units == 'Fahrenheit' or units == 'F':
        return (value_to_convert - 32) * 5 / 9

    if units == 'Rankine Scale' or units == 'Ra':
        return (value_to_convert - 491.67) * 5 / 9

    if units == 'Reaumur Scale' or units == 'Re':
        return value_to_convert * 5 / 4


def get_temp_units_to_convert(value_to_convert):
    """Reads the units and checks are they acceptable."""
    unit = None

    units_list = {'Celsius', 'C', 'Kelvin', 'K', 'Fahrenheit', 'F',
                  'Rankine Scale', 'Ra', 'Reaumur Scale', 'Re'}

    while True:
        print('Available units: Celsius - "C", Kelvin - "K", Fahrenheit - "F"')
        print('Rankine Scale - "Ra", Reaumur Scale - "Re"')
        unit = input('Please, select units of value to convert: ')

        if unit not in units_list:
            print('Oops, something wrong. Please, choose valid units:')
            continue

        return value_to_standart(value_to_convert, unit)


def convert_temperature(converted_value_to_convert):
    """
    Convert standart - Celsius - to other units/=.
    """
    Kelvin = converted_value_to_convert + 273.15
    Fahrenheit = converted_value_to_convert * (9 / 5) + 32
    Rankine = (converted_value_to_convert + 273.15) * (9 / 5)
    Reaumur = converted_value_to_convert * 4 / 5

    return([converted_value_to_convert, Kelvin, Fahrenheit, Rankine, Reaumur])


def main():
    print('Hi! It`s simple temperature converter.')

    # reads the command
    while True:

        command = input('Please, choose convert ("T") or "exit": ')

        if command != 'T':
            print('Oops, something wrong. Please, choose valid command: "T"; or "exit"')
            continue

        if command == 'exit':
            print('Goodbye!')
            break

        value_to_convert = get_value_to_convert()

        if command == 'temperature' or command == 'T':
            # standart - Celsius

            get_temp_units_to_convert(value_to_convert)

            converted_value = convert_temperature(value_to_convert)

            final_values = [round(num, 2) for num in converted_value]

            final_units = ['Celsius', 'Kelvin', 'Fahrenheit', 'Rankine', 'Reaumur']

            print('Converted values:')
            for value, unit in zip(final_values, final_units):
                print(value, unit)


if __name__ == '__main__':
    main()
