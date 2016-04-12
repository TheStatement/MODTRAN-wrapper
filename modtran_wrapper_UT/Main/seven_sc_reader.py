'''
Created on Feb 4, 2016

@author: ried_st
'''

import os
from Main.modtran_functions import ModtranFunctions

class Seven_sc_reader(object):
    def __init__(self):
        pass

    def read_seven_sc(self, seven_sc_directory, filename):
        '''read_seven_sc does currently not take any input parameters.
        It uses the directory and filename specified in the beginning of the function.
        They should point to a .tp7 modtran output file with common format.
        The function returns the line numbers from the beginning and end of a block of data,
        as well as a list of parameters, which label each row of data in the .tp7 file'''
        
        modtran_functions = ModtranFunctions()
        
        #results_directory = r'C:\Users\ried_st\OneDrive\Austausch\Programming\TEST'
        #results_filename = 'ASCIIwrite.tp7'
        filename = filename + '.7sc'
        seven_sc_directory = os.path.join(seven_sc_directory, filename)
        
        beginning_data = []
        end_data = []
                
        '''searches for keywords in tape 7 and determines the lines in which data begins and stops'''
        
        with open(seven_sc_directory, 'r') as seven_sc:
            searchlines = seven_sc.readlines()
        for i, line in enumerate(searchlines):
            if 'FREQ' in line:
                list_parameters = line.split(' ')
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
            for j in range(0, 2):
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