'''
Created on 17.11.2015

@author: Basti
'''

import os
from Main.modtran_functions import ModtranFunctions

class Tape7_reader(object):
    def __init__(self):
        pass

    def read_tape7(self, tape7_directory, filename):
        '''Input:
        - tape7_directory: the path directory where the .tp7 is located
        - filename: filename of the .tp7 file
        The function returns the line numbers from the beginning and end of a block of data,
        as well as a list of parameters, which label each row of data in the .tp7 file
        
        The output is a list with the form: [beginning_data, end_data, list_parameters2, complete_data]
        complete_data contains all the data from the file in a matrix. The first index accesses the block,
        the second one the line inside a block (according to list_parameters, which can be accessed by Tape7_reader.get_list_parameters()
        
        Example:
        tape7 = Tape7.read_tape7(r'C:\\Users\\ried_st\\Desktop\\Temporal eclipse workspace\\PG_Alte Modtran Rechnungen\\neu gerechnet\\20160217_1', '20160217_1', 'y')
        tape7[3][0][2]

        would return the third line of the first block of complete_data'''
        
        modtran_functions = ModtranFunctions()
        
        #results_directory = r'C:\Users\ried_st\OneDrive\Austausch\Programming\TEST'
        #results_filename = 'ASCIIwrite.tp7'
        filename = filename + '.tp7'
        tape7_directory = os.path.join(tape7_directory, filename)
        
        beginning_data = []
        end_data = []
                
        '''searches for keywords in tape 7 and determines the lines in which data begins and stops'''
        
        with open(tape7_directory, 'r') as tape7:
            searchlines = tape7.readlines()
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
            print('reading tape 7: number of starting points is not equal to number of endpoints')
            
        list_parameters2 = []
        for string in list_parameters:
            tmp = string.strip('\n')
            list_parameters2.append(tmp)
            
        complete_data = []
                
        for i in range(0, len(beginning_data)):
            '''if tape5 contains multiple input blocks, there are also multiple output blocks. len(beginning_data) is the number of output blocks'''
            block = []
            for j in range(0, len(list_parameters)):
                '''each parameter row needs to be extracted separately'''
                
                tmp = []
                for k in range(beginning_data[i], end_data[i]+1):
                    '''iterates over all lines of one row in one block and writes the values into '''
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
    
    
    
    def get_list_parameters(self, tape7_directory, filename):
        
        modtran_functions = ModtranFunctions()
        filename = filename + '.tp7'
        tape7_directory = os.path.join(tape7_directory, filename)
        
        beginning_data = []
        end_data = []
                
        '''searches for keywords in tape 7 and determines the lines in which data begins and stops'''
        
        with open(tape7_directory, 'r') as tape7:
            searchlines = tape7.readlines()
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
            print('reading tape 7: number of starting points is not equal to number of endpoints')
            
        list_parameters2 = []
        for string in list_parameters:
            tmp = string.strip('\n')
            list_parameters2.append(tmp)
            
        print(list(enumerate(list_parameters2)))