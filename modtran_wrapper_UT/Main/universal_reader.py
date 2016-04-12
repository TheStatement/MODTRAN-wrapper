'''
Created on Feb 4, 2016

@author: ried_st
'''

import os
from Main.modtran_functions import ModtranFunctions

class Universal_reader(object):
    def __init__(self):
        pass

    def read_universal(self, file_directory, filename, file_extension, number_rows):
        '''read_tape6 does currently not take any input parameters.
        It uses the directory and filename specified in the beginning of the function.
        They should point to a .tp7 modtran output file with common format.
        The function returns the line numbers from the beginning and end of a block of data,
        as well as a list of parameters, which label each row of data in the .tp7 file'''
        
        modtran_functions = ModtranFunctions()

        filename = filename + file_extension
        universal_directory = os.path.join(file_directory, filename)
        
        beginning_data = []
        end_data = []
                
        '''searches for keywords in tape 7 and determines the lines in which data begins and stops'''
        
        with open(universal_directory, 'r') as universal:
            searchlines = universal.readlines()
        for i, line in enumerate(searchlines):
            if 'FREQ' in line:
                list_parameters = line.split(' ')
                print(list_parameters)
                modtran_functions.remove_from_list(list_parameters, '')
                if 'CM-1' in searchlines[i+1]:
                    beginning_data.append(i+2)
                else:
                    beginning_data.append(i+1)
            elif 'WAVLEN (NM)' in line:
                list_parameters = line.split(' ')
                modtran_functions.remove_from_list(list_parameters, '')
                if 'NM' in searchlines[i+1]:
                    beginning_data.append(i+2)
                else:
                    beginning_data.append(i+1)
            elif '-9999.' in line:
                end_data.append(i-1)
         
        if len(beginning_data) != len(end_data):
            print('reading .7sc: number of starting points is not equal to number of endpoints')
            
        list_parameters2 = []
        for string in list_parameters:
            tmp = string.strip('\n')
            list_parameters2.append(tmp)
        
        complete_data = []
                
        for i in range(0, len(beginning_data)):
            #if tape5 contains multiple input blocks, there are also multiple output blocks. len(beginning_data) is the number of output blocks
            block = []
            for j in range(0, number_rows):
                #each parameter row need to be extracted separately
                
                tmp = []
                for k in range(beginning_data[i], end_data[i]+1):
                    tmp2 = searchlines[k].split(' ')
                    modtran_functions.remove_from_list(tmp2, '')
                    tmp4 = []
                    for string in tmp2:
                        tmp3 = string.strip('\n')
                        tmp4.append(tmp3)
                    
                    tmp.append(tmp4[j])
                
                block.append(tmp)
                
            complete_data.append(block)    
        
        #print (beginning_data)
        #print (end_data)
        #print (list_parameters)
        return([beginning_data, end_data, list_parameters2, complete_data])
    
    
    def get_list_parameters(self, file_directory, filename, file_extension):
        
        modtran_functions = ModtranFunctions()

        filename = filename + file_extension
        universal_directory = os.path.join(file_directory, filename)
        
        beginning_data = []
        end_data = []
                
        '''searches for keywords in tape 7 and determines the lines in which data begins and stops'''
        
        with open(universal_directory, 'r') as universal:
            searchlines = universal.readlines()
        for i, line in enumerate(searchlines):
            if 'FREQ' in line:
                list_parameters = line.split(' ')
                print(list_parameters)
                modtran_functions.remove_from_list(list_parameters, '')
                if 'CM-1' in searchlines[i+1]:
                    beginning_data.append(i+2)
                else:
                    beginning_data.append(i+1)
            elif 'WAVLEN (NM)' in line:
                list_parameters = line.split(' ')
                modtran_functions.remove_from_list(list_parameters, '')
                if 'NM' in searchlines[i+1]:
                    beginning_data.append(i+2)
                else:
                    beginning_data.append(i+1)
            elif '-9999.' in line:
                end_data.append(i-1)
         
        if len(beginning_data) != len(end_data):
            print('reading .7sc: number of starting points is not equal to number of endpoints')
            
        list_parameters2 = []
        for string in list_parameters:
            tmp = string.strip('\n')
            list_parameters2.append(tmp)
            
        print(list(enumerate(list_parameters2)))