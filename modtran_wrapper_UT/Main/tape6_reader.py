'''
Created on 17.11.2015

@author: Basti
'''

import os
from Main.modtran_functions import ModtranFunctions

class Tape6_Reader(object):
    def __init__(self):
        pass

    def read_tape6(self, directory, filename):
        '''read_tape6 does currently not take any input parameters.
        It uses the directory and filename specified in the beginning of the function.
        They should point to a .tp6 modtran output file with MODTRAN format.
        The function returns the line numbers from the beginning and end of a block of data,
        as well as a list of parameters, which label each row of data in the .tp7 file'''
        
        modtran_functions = ModtranFunctions()
        
        results_directory = directory
        results_filename = filename
        tape6_directory = os.path.join(results_directory, results_filename)
        
        beginning_data = []
        end_data = []
                
        '''searches for keywords in tape 7 and determines the lines in which data begins and stops'''
        
        with open(tape6_directory, 'r') as tape6:
            searchlines = tape6.readlines()
        for i, line in enumerate(searchlines):
            if 'FREQ' in line:
                list_parameters = line.split(' ')
                modtran_functions.remove_from_list(list_parameters, '')
                if 'CM-1' in searchlines[i+1]:
                    beginning_data.append(i+2)
                else:
                    beginning_data.append(i+1)
            elif 'WAVELENGTH' in line:
                list_parameters = line.split(' ')
                modtran_functions.remove_from_list(list_parameters, '')
                # needs to be verified, if 'NM' is the correct term used in tp7 files
                if 'NM' in searchlines[i+1]:
                    beginning_data.append(i+2)
                else:
                    beginning_data.append(i+1)
            elif '-9999.' in line:
                end_data.append(i-1)
         
        if len(beginning_data) != len(end_data):
            print('reading tape6: number of starting points is not equal to number of endpoints')
            
        
        #print (beginning_data)
        #print (end_data)
        #print (list_parameters)
        return({'beginning_data': beginning_data, 'end_data': end_data, 'list_parameters': list_parameters})

