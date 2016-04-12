'''
Created on Jan 14, 2016

@author: ried_st

This program reads .tp5 files and converts the content into parameters (with description), which can be more easily understood.
Input: one .tp5 file
Output: one .txt file

The program requires the name of each card to be specified within the line in exactly the following form (additional spaces at the end are not a problem):
'!card 1.'
'!card 1a.'
'!card 1a2'
'!card 2.'
'!card 3 standart'
'!card 3 alternative'
'!card 3a1'
'!card 3a2'
'!card 4.'
'!card 5.'

Everything else is ignored.
The output file is written into the same directory and named '<input_filename>.txt'

Posssible improvement: extend parameter_mat from Main.main and use it to loop over each card
'''

#check if card5 is 1 or 0 -> read multiple tape 5?

import os
# from Main.modtran_functions import ModtranFunctions
#from Main.variable_library import StandardParameters

class Tape5_reader(object):
    def __init__(self):
        pass

    def read_tape5(self, input_directory, filename):
        
        input_filename = filename + '.tp5'
        tape5_directory = os.path.join(input_directory, input_filename)
        
        output_file = ''
                
        with open(tape5_directory, 'r') as tape5:
            searchlines = tape5.readlines()
        for i, line in enumerate(searchlines):
            if '!card 1.' in line:
                output_file += ('CARD 1: \n' + 'MODTRN = ' + line[0:1] + '\n' + 'SPEED = ' + line[1:2] + '\n' + 'BINARY = ' + line[2:3] + '\n'
                + 'LYMOLC = ' + line[3:4] + '\n' + 'MODEL = ' + line[4:5] + '\n' + ' T_BEST = ' + line[5:6] + '\n' + 'ITYPE = ' + line[6:10] + '\n'
                + 'IEMSCT = ' + line[10:15] + '\n' + 'IMULT = ' + line[15:20] + '\n' + 'M1 = ' + line[20:25] + '\n' + 'M2 = ' + line[25:30] + '\n' 
                + 'M3 = ' + line[30:35] + '\n' + 'M4 = ' + line[35:40] + '\n' + 'M5 = ' + line[40:45] + '\n' + 'M6 = ' + line[45:50] + '\n' 
                + 'MDEF = ' + line[50:55] + '\n' + 'I_RD2C = ' + line[55:60] + '\n' + 'NOPRNT = ' + line[60:65] + '\n' 
                + 'TPTEMP = ' + line[65:73] + '\n' + 'SURREF = ' + line[73:80] + '\n' + '\n' + '\n')
                
            if '!card 1a.' in line:
                output_file += ('CARD 1A: \n' + 'DIS = ' + line[0:1] + '\n' + 'DISAZM = ' + line[1:2] + '\n' + 'DISALB = ' + line[2:3] + '\n'
                + 'NSTR = ' + line[3:6] + '\n' + 'SFWHM = ' + line[6:10] + '\n' + 'CO2MX = ' + line[10:20] + '\n' + 'H2OSTR = ' + line[20:30] + '\n'
                + 'O3STR = ' + line[30:40] + '\n' + 'C_PROF = ' + line[40:41] + '\n' + 'LSUNFL = ' + line[41:42] + '\n' + 'LBMNAM = ' + line[42:44] + '\n'
                + 'LFLTNM = ' + line[44:46] + '\n' + 'H2OAER = ' + line[46:48] + '\n' + 'CDTDIR = ' + line[48:50] + '\n' + 'SOLCON = ' + line[50:60] + '\n'
                + 'CDASTM = ' + line[60:61] + '\n' + 'ASTMC = ' + line[61:70] + '\n' + 'ASTMX = ' + line[70:80] + '\n' + 'ASTMO = ' + line[80:90] + '\n'
                + 'AERRH = ' + line[90:100] + '\n' + 'NSSALB = ' + line[100:110] + '\n' + '\n' + '\n')
                
            if '!card 1a2' in line:
                output_file += ('CARD 1A2: \n' + 'BMNAME = ' + line[0:256] + '\n' + '\n' + '\n')
                
            if '!card 2.' in line:
                output_file += ('CARD 2: \n' + 'APLUS = ' + line[0:2] + '\n' + 'IHAZE = ' + line[2:5] + '\n' + 'CNOVAM = ' + line[5:6] + '\n' + 'ISEASN = ' + line[6:10] + '\n'
                + 'ARUSS = ' + line[10:13] + '\n' + 'IVULCN = ' + line[13:15] + '\n' + 'ICSTL = ' + line[15:20] + '\n' + 'ICLD = ' + line[20:25] + '\n' + 'IVSA = ' + line[25:30] + '\n'
                + 'VIS = ' + line[30:40] + '\n' + 'WSS = ' + line[40:50] + '\n' + 'WHH = ' + line[50:60] + '\n' + 'RAINRT = ' + line[60:70] + '\n' + 'GNDALT = ' + line[70:80] + '\n' + '\n' + '\n')
                
            if '!card 3 standart' in line:
                output_file += ('CARD 3 STANDART: \n' + 'H1 = ' + line[0:10] + '\n' + 'H2 = ' + line[10:20] + '\n' + 'ANGLE = ' + line[20:30] + '\n'
                + 'RANGE = ' + line[30:40] + '\n' + 'BETA = ' + line[40:50] + '\n' + 'RO = ' + line[50:60] + '\n' + 'LENN = ' + line[60:65] + '\n' + 'PHI = ' + line[65:75] + '\n' + '\n' + '\n')
                
            if '!card 3 alternative' in line:
                output_file += ('CARD 3 ALTERNATIVE: \n' + 'H1ALT = ' + line[0:10] + '\n' + 'H2 = ' + line[10:20] + '\n' + 'ANGLE = ' + line[20:30] + '\n'
                + 'IDAY = ' + line[30:35] + '\n' + 'RO = ' + line[35:45] + '\n' + 'ISOURC = ' + line[45:50] + '\n' + 'ANGLEM = ' + line[50:60] + '\n' + '\n' + '\n')
                
            if '!card 3a1' in line:
                output_file += ('CARD 3A1: \n' + 'IPARM = ' + line[0:5] + '\n' + 'IPH = ' + line[5:10] + '\n' + 'IDAY = ' + line[10:15] + '\n'
                + 'ISOURC = ' + line[15:20] + '\n' + '\n' + '\n')
                
            if '!card 3a2' in line:
                output_file += ('CARD 3A2: \n' + 'PARM1 = ' + line[0:10] + '\n' + 'PARM2 = ' + line[10:20] + '\n' + 'PARM3 = ' + line[20:30] + '\n'
                + 'PARM4 = ' + line[30:40] + '\n' + 'TIME = ' + line[40:50] + '\n' + 'PSIPO = ' + line[50:60] + '\n' + 'ANGLEM = ' + line[60:70] + '\n'
                + 'G = ' + line[70:80] + '\n' + '\n' + '\n')
                
            if '!card 4.' in line:
                output_file += ('CARD 4: \n' + 'V1 = ' + line[0:10] + '\n' + 'V2 = ' + line[10:20] + '\n' + 'DV = ' + line[20:30] + '\n' + 'FWHM = ' + line[30:40] + '\n'
                + 'YFLAG = ' + line[40:41] + '\n' + 'XFLAG = ' + line[41:42] + '\n' + 'DLIMIT = ' + line[42:50] + '\n' + 'FLAGS = ' + line[50:57] + '\n'
                + 'MLFLX = ' + line[57:60] + '\n' + 'VRFRAC = ' + line[60:70] + '\n' + '\n' + '\n')
                
            if '!card 5.' in line:
                output_file += ('CARD 5: \n' + 'card 5 = ' + line[0:5] + '\n' + '\n' + '___________next tape5___________________________________________________________' + '\n' + '\n')
                
        print (output_file)
        
        new_tape5 = open(input_directory + '/' + filename + '.dat', 'w')
        new_tape5.writelines(output_file)
        new_tape5.close()
                
                
