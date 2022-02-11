import datetime
import os.path
import itertools
import csv

import matplotlib.pyplot as plt
import numpy as np

from Bio.Seq import Seq, back_transcribe
from Bio import SeqIO


class Hamster:
    '''
    Python Class that describes hamsters.
    For creation "hamster" object it is nedeed to know its name and age (in months).
    Optionally, one can specify the type of hamster (for example, Syrian or Chinese). Default "Not defined".
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
        Method returns the age of a hamster: young, adult or old.
        '''        
        return f"{self.name} is an {self.stage} hamster. It's {self.age} months."


    def is_active(self):
        '''
        Checks if the hamster is probably asleep now. The system time is used. Return the string with state.
        '''
        time_now = datetime.datetime.now().hour
        
        if time_now > 7 and time_now < 20:
            return f'{self.name} is probably sleeping now.'
            
        else:
            return f'{self.name} is probably active now and wants treats.'


    def properties(self):
        '''
        Return string with the basic parameters of the hamster.
        '''
        if self.hamster_type == 'Not defined':            
            return f"The hamster\'s name is {self.name}. It\'s {self.stage} hamster, {self.age} months."
        else:
            return f"The hamster\'s name is {self.name}. It\'s {self.stage} {self.hamster_type} hamster, {self.age} months."


class RNASequence(str):
    '''
    Class for operations with RNA sequences. Parent class - str.
    '''
    acid_type = 'RNA'
    
    def __init__(self, rna_sequence):
        self.rna_sequence = rna_sequence
        
    def RNA_translation(self):
        '''
        Translation - returns a string corresponding to the protein from the RNA,
        according to the standard code, using Biopython.
        '''
        self.protein = Bio.Seq.translate(self.rna_sequence)
        return self.protein
        
    def RNA_to_DNA(self):
        '''
        Reverse transcription method - returns a string corresponding to the DNA from RNA, using Biopython.
        '''
        self.template_dna = Bio.Seq.back_transcribe(self.rna_sequence)
        return self.template_dna


class PositiveSet(set):
    '''
    Sets with only positive numbers.
    Two methods supports: add and update (but not |=).
    '''
    
    def __init__(self, old_numbers):
        '''
        Initializes PositiveSet, adding only positive numbers using the add method.
        '''
        for number in old_numbers:
            self.add(number)
    
    def add(self, element):
        '''
        Check if number for adding is positive. 
        If so, it adds it to the PositiveSet using the regular set 'add' method.
        '''
        if element >= 0:
            super().add(element)
        
    def update(self, *args):
        '''
        Update PositiveSet using positive values (PositiveSet 'add' method) from the given args.
        '''
        if len(args) == 1:
            for element in args[0]:
                self.add(element)
        else:
            for added_set in args[:-1]:
                for element in added_set:
                    self.add(element)
    



def main():
    pass


if __name__ == '__main__':
    main()
