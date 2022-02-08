import datetime

# 1. Class that describes hamsters.
# Python class for hamsters.
# For creation "hamster" object it is nedeed to know its name and age (in months).
# Optionally, one can specify the type of hamster (for example, Syrian or Chinese). Default "Not defined".


class Hamster:
    '''
    Python class for hamsters.
    '''

    def __init__(self, name, age, hamster_type='Not defined'):
        '''
        For creation "hamster" object it is nedeed to know its name and age (in months).
        Optionally, one can specify the type of hamster (for example, Syrian or Chinese). Default "Not defined".
        '''
        self.name = name
        self.hamster_type = hamster_type
        self.age = age
        
        if self.age <= 4:
            self.stage = 'young'            
            
        elif self.age >= 12:
            self.stage = 'old'
        
        else:
            self.stage = 'adult'
        

    def life_stage(self):
        '''
        Method for printing the age of a hamster: young, adult or old.
        '''        
        print(f'{self.name} is an {self.stage} hamster. It\'s {self.age} months.')


    def is_active(self):
        '''
        Checks if the hamster is probably asleep now. The system time is used.
        '''
        time_now = datetime.datetime.now().hour
        
        if time_now > 7 and time_now < 20:
            print(f'{self.name} is probably sleeping now.')
            
        else:
            print(f'{self.name} is probably active now and wants treats.')


    def properties(self):
        '''
        Displays the basic parameters of the hamster.
        '''
        print(f'The hamster\'s name is {self.name}.')

        if self.hamster_type == 'Not defined':            
            print(f'It\'s {self.stage} hamster, {self.age} months.')
        else:
            print(f'It\'s {self.stage} {self.hamster_type} hamster, {self.age} months.')


def main():

    # test output for first class Hamster.
    Bun = Hamster('Bun', 23, 'Djungarian hamster')
    Bun.is_active()
    Bun.properties()


if __name__ == '__main__':
    main()