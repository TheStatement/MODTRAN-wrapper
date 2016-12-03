'''
Created on Nov 25, 2015

@author: ried_st


This is the main file of the program. It uses functions from various other files to
- assemble a tape5 in the proper way (it also contains the logic, which optional cards are active or inactive)
- check this tape5 for errors
- write it to a .tp5 file in the directory, which is also also specified here

Add parameter:
- add to variable library
- Write tape5
- execute modtran 2x
- adjust in modtran functions
- add input variable in modtran functions

to do:
rework tape7_reader
implement more parameters
plotting
Andere files readen und plotten
'''

import subprocess, os
import numpy as np
from Main.modtran_functions import ModtranFunctions
from Main.variable_libraries.variable_library_20161114 import StandardParameters



class BuildTape5(object):
    def __init__(self):
        self.stan_parm = StandardParameters()
        self.tp5_directory = self.stan_parm.output_directory
        self.filename = self.stan_parm.tp5_filename # This is the filename of the future tape5
        
        self.mod_fun = ModtranFunctions()
    
    
    def assemble_tape5(self, mat):
        
        # CARD_1
        T_BEST = ' '
        M1 = M2 = M3 = M4 = M5 = M6 = MDEF = '    0'
        TPTEMP = '    .000'
        self.CARD_1 = (self.mod_fun.find_in_array(mat, 'MODTRN') + self.mod_fun.find_in_array(mat, 'SPEED') + self.mod_fun.find_in_array(mat, 'BINARY') + self.mod_fun.find_in_array(mat, 'LYMOLC') + 
                    self.mod_fun.find_in_array(mat, 'MODEL') + T_BEST + self.mod_fun.find_in_array(mat, 'ITYPE') + self.mod_fun.find_in_array(mat, 'IEMSCT') + self.mod_fun.find_in_array(mat, 'IMULT') + 
                    M1 + M2 + M3 + M4 + M5 + M6 + MDEF + self.mod_fun.find_in_array(mat, 'I_RD2C') + self.mod_fun.find_in_array(mat, 'NOPRNT') + TPTEMP + self.mod_fun.find_in_array(mat, 'SURREF') + '!card 1.')
        
        
        # CARD_1A
        DISAZM = ' '
        DISALB = ' '
        SFWHM = '  0.'
        C_PROF = ' '
        LSUNFL = ' '
        LFLTNM = H2OAER = '  '
        CDTDIR = '  '
        
        self.CARD_1A = (self.mod_fun.find_in_array(mat, 'DIS') + DISAZM + DISALB + self.mod_fun.find_in_array(mat, 'NSTR') + SFWHM + self.mod_fun.find_in_array(mat, 'CO2MX') + 
                       self.mod_fun.find_in_array(mat, 'H2OSTR') + self.mod_fun.find_in_array(mat, 'O3STR') + C_PROF + LSUNFL + self.mod_fun.find_in_array(mat, 'LBMNAM') + LFLTNM + H2OAER + CDTDIR +
                       self.mod_fun.find_in_array(mat, 'SOLCON') + self.mod_fun.find_in_array(mat, 'CDASTM') + self.mod_fun.find_in_array(mat, 'ASTMC') + self.mod_fun.find_in_array(mat, 'ASTMX') +
                       self.mod_fun.find_in_array(mat, 'ASTMO') + self.mod_fun.find_in_array(mat, 'AERRH') + self.mod_fun.find_in_array(mat, 'NSSALB') + '!card 1a.')
        
        
        #CARD_1A2
        BMNAME = self.mod_fun.find_in_array(mat, 'BMNAME')
        SPACER = self.mod_fun.adjust_length('', (256-len(str(BMNAME))))
        
        self.CARD_1A2 = (BMNAME + SPACER + '!card 1a2')
            
        
        #CARD_2
        APLUS = '  '
        CNOVAM = ' '
        ISEASN = '   0'
        ARUSS = '   '
        IVULCN = ' 0'
        IVSA = '    0'
        RAINRT = '          '
        
        self.CARD_2 = (APLUS + self.mod_fun.find_in_array(mat, 'IHAZE') + CNOVAM + ISEASN + ARUSS + IVULCN + self.mod_fun.find_in_array(mat, 'ICSTL') + self.mod_fun.find_in_array(mat, 'ICLD') + 
                      IVSA + self.mod_fun.find_in_array(mat, 'VIS') + self.mod_fun.find_in_array(mat, 'WSS') + self.mod_fun.find_in_array(mat, 'WHH') + RAINRT + self.mod_fun.find_in_array(mat, 'GNDALT') + '!card 2.')
        
        
        #CARD3_Standard
        BETA = '        0.'
        RO = '        0.'
        LENN = '    0'
        PHI = '          '
        self.STA = (self.mod_fun.find_in_array(mat, 'H1_sta') + self.mod_fun.find_in_array(mat, 'H2_sta') + self.mod_fun.find_in_array(mat, 'ANGLE_sta') + 
                         self.mod_fun.find_in_array(mat, 'RANGE_sta') + BETA + RO + LENN + '     ' + PHI + '!card 3 standart')
        
        
        #CARD3_Alternative
        RO = '          '
        ISOURC = '    0'
        ANGLEM = '         0'
        self.CARD3_ALT = (self.mod_fun.find_in_array(mat, 'H1ALT') + self.mod_fun.find_in_array(mat, 'H2_alt') + self.mod_fun.find_in_array(mat, 'ANGLE_alt') + 
                         self.mod_fun.find_in_array(mat, 'IDAY_alt') + '     ' + RO + ISOURC + ANGLEM + '!card 3 alternative') # no idea why I added the 5 spaces
        
        
        #A1
        IPH = '    2'
        ISOURC = '    0'
        self.A1 = (self.mod_fun.find_in_array(mat, 'IPARM') + IPH + self.mod_fun.find_in_array(mat, 'IDAY') + ISOURC + '!card 3a1')
        
        
        #A2
        PARM3 = '         1'
        PARM4 = '         2'
        TIME = '         3'
        PSIPO = '         4'
        ANGLEM = '         5'
        G = '         6'
        self.A2 = (self.mod_fun.find_in_array(mat, 'PARM1') + self.mod_fun.find_in_array(mat, 'PARM2') + PARM3 + PARM4 + TIME + PSIPO + ANGLEM + G + '!card 3a2')
        
        
        #CARD_4
        MLFLX = '   '
        VRFRAC = '          '
        self.CARD_4 = (self.mod_fun.find_in_array(mat, 'V1') + self.mod_fun.find_in_array(mat, 'V2') + self.mod_fun.find_in_array(mat, 'DV') + self.mod_fun.find_in_array(mat, 'FWHM') + 
                      self.mod_fun.find_in_array(mat, 'YFLAG') + self.mod_fun.find_in_array(mat, 'XFLAG') + self.mod_fun.find_in_array(mat, 'DLIMIT') + 
                      self.mod_fun.find_in_array(mat, 'FLAGS') + MLFLX + VRFRAC + '!card 4.')
        
        
        #CARD_4A
        self.CARD_4A = (self.mod_fun.find_in_array(mat, 'NSURF') + self.mod_fun.find_in_array(mat, 'AATEMP') + self.mod_fun.find_in_array(mat, 'DH2O') + self.mod_fun.find_in_array(mat, 'MLTRFL') + '!card 4a')
        
        
        #CARD_4L1
        SALBFL = self.mod_fun.find_in_array(mat, 'SALBFL')
        SPACER = self.mod_fun.adjust_length('', (256-len(str(SALBFL))))
        self.CARD_4L1 = (SALBFL + SPACER + '!card 4l1')
        
        
        #CARD_4L2
        CSALB = self.mod_fun.find_in_array(mat, 'CSALB')
        SPACER = self.mod_fun.adjust_length('', (80-len(str(CSALB))))
        self.CARD_4L2 = (CSALB + SPACER + '!card 4l2')
        
        
        self.mod_fun.check_tape5(self.CARD_1, self.CARD_1A, self.CARD_2, self.STA, self.CARD3_ALT, self.A1, self.A2, self.CARD_4, self.CARD_4A, self.CARD_4L1, self.CARD_4L2, self.CARD_5)
        
        
        
    def write_tape5(self, mat):
        '''Caution: the order in 'used_cards' is important for the correct assembly of tape5'''
        self.assemble_tape5(mat)
        
        available_cards = {'CARD_1': self.CARD_1, 'CARD_1A': self.CARD_1A, 'CARD_1A2': self.CARD_1A2, 'CARD_2': self.CARD_2, 'STA': self.STA,
                           'ALT': self.CARD3_ALT, 'A1': self.A1, 'A2': self.A2, 'CARD_4': self.CARD_4, 'CARD_4A': self.CARD_4A, 
                           'CARD_4L1': self.CARD_4L1, 'CARD_4L2': self.CARD_4L2, 'CARD_5': self.CARD_5}
        used_cards = ['CARD_1', 'CARD_1A']
        
        if any(str(self.stan_parm.LBMNAM) in s for s in ['T', 't', '2', '4']): # should get value not from stan_parm, but from parameter_mat
            used_cards.append('CARD_1A2')
        
        used_cards.append('CARD_2')
        
        if any(str(self.stan_parm.IEMSCT) in s for s in ['2', '4']):
            used_cards.extend(['STA', 'A1', 'A2'])
        elif str(self.stan_parm.IEMSCT) == '3':
            used_cards.extend(['ALT', 'A1', 'A2'])
        else:
            used_cards.append('STA')
            
        if any(str(self.mod_fun.find_in_array(mat, 'PARM1')) in s for s in ['L', 'l']):
            used_cards.extend(['CARD_4A', 'CARD_4L1', 'CARD_4L2'])

        used_cards.extend(['CARD_4', 'CARD_5'])
        
        
        
        
        tape5 = []
        for card in used_cards:
            if card in available_cards:
                tape5.append(available_cards[card])
                tape5.append('\n')
        
        new_tape5 = open(self.tp5_directory + '/' + self.filename + '.tp5', 'a')

        new_tape5.writelines(tape5)
        new_tape5.close()
    

    
    
    def execute_modtran(self, parameter, beginning, end, step, list_values):
        '''this function creates a .tp5 file and starts a MODTRAN run
        It has the ability to iterate over a specific parameter
        Needs to set tape5
        Possible improvement: modify function to perform a single run with all specified values if parameter = ''
        '''
        
        
        MODTRN = str(self.stan_parm.MODTRN)
        SPEED = str(self.stan_parm.SPEED)
        BINARY = str(self.stan_parm.BINARY)
        MODEL = str(self.stan_parm.MODEL)
        LYMOLC = str(self.stan_parm.LYMOLC)
        ITYPE = str(self.stan_parm.ITYPE)
        IEMSCT = str(self.stan_parm.IEMSCT)
        IMULT = str(self.stan_parm.IMULT)
        I_RD2C = str(self.stan_parm.I_RD2C)
        NOPRNT = str(self.stan_parm.NOPRNT)
        SURREF = str(self.stan_parm.SURREF)
        DIS = str(self.stan_parm.DIS)
        NSTR = str(self.stan_parm.NSTR)
        CO2MX = str(self.stan_parm.CO2MX)
        H2OSTR = str(self.stan_parm.H2OSTR)
        O3STR = str(self.stan_parm.O3STR)
        LBMNAM = str(self.stan_parm.LBMNAM)
        SOLCON = str(self.stan_parm.SOLCON)
        CDASTM = str(self.stan_parm.CDASTM)
        BMNAME = str(self.stan_parm.BMNAME)
        IHAZE = str(self.stan_parm.IHAZE)
        ICSTL = str(self.stan_parm.ICSTL)
        ICLD = str(self.stan_parm.ICLD)
        VIS = str(self.stan_parm.VIS)
        WSS = str(self.stan_parm.WSS)
        WHH = str(self.stan_parm.WHH)
        GNDALT = str(self.stan_parm.GNDALT)
        H1_sta = str(self.stan_parm.H1_sta)
        H2_sta = str(self.stan_parm.H2_sta)
        ANGLE_sta = str(self.stan_parm.ANGLE_sta)
        RANGE_sta = str(self.stan_parm.RANGE_sta)
        H1ALT = str(self.stan_parm.H1ALT)
        H2_alt = str(self.stan_parm.H2_alt)
        ANGLE_alt = str(self.stan_parm.ANGLE_alt)
        IDAY_alt = str(self.stan_parm.IDAY_alt)
        IPARM = str(self.stan_parm.IPARM)
        IDAY = str(self.stan_parm.IDAY)
        PARM1 = str(self.stan_parm.PARM1)
        PARM2 = str(self.stan_parm.PARM2)
        V1 = str(self.stan_parm.V1)
        V2 = str(self.stan_parm.V2)
        DV = str(self.stan_parm.DV)
        FWHM = str(self.stan_parm.FWHM)
        YFLAG = str(self.stan_parm.YFLAG)
        XFLAG = str(self.stan_parm.XFLAG)
        DLIMIT = str(self.stan_parm.DLIMIT)
        FLAGS = str(self.stan_parm.FLAGS)
        
        ASTMC = str(self.stan_parm.ASTMC)
        ASTMX = str(self.stan_parm.ASTMX)
        ASTMO = str(self.stan_parm.ASTMO)
        AERRH = str(self.stan_parm.AERRH)
        NSSALB = str(self.stan_parm.NSSALB)
        # CARD_4A
        NSURF = str(self.stan_parm.NSURF)
        AATEMP = str(self.stan_parm.AATEMP)
        DH2O = str(self.stan_parm.DH2O)
        MLTRFL = str(self.stan_parm.MLTRFL)
        SALBFL = str(self.stan_parm.SALBFL)
        CSALB = str(self.stan_parm.CSALB)
        

        parameter_mat = [[MODTRN, 'MODTRN', 1], [SPEED, 'SPEED', 1], [BINARY, 'BINARY', 1], [LYMOLC, 'LYMOLC', 1], [MODEL, 'MODEL', 1], [ITYPE, 'ITYPE', 4], [IEMSCT, 'IEMSCT', 5],
                       [IMULT, 'IMULT', 5], [I_RD2C, 'I_RD2C', 5], [NOPRNT, 'NOPRNT', 5], [SURREF, 'SURREF', 7], [DIS, 'DIS', 1], [NSTR, 'NSTR', 3],
                       [CO2MX, 'CO2MX', 10], [H2OSTR, 'H2OSTR', 10], [O3STR, 'O3STR', 10], [LBMNAM, 'LBMNAM', 2], [SOLCON, 'SOLCON', 10], [CDASTM, 'CDASTM', 1],
                       [BMNAME, 'BMNAME', 256], [IHAZE, 'IHAZE', 3], [ICSTL, 'ICSTL', 5], [ICLD, 'ICLD', 5], [VIS, 'VIS', 10], [WSS, 'WSS', 10],
                       [WHH, 'WHH', 10], [GNDALT, 'GNDALT', 10], [H1_sta, 'H1_sta', 10], [H2_sta, 'H2_sta', 10], [ANGLE_sta, 'ANGLE_sta', 10],
                       [RANGE_sta, 'RANGE_sta', 10], [H1ALT, 'H1ALT', 10], [H2_alt, 'H2_alt', 10], [ANGLE_alt, 'ANGLE_alt', 10],
                       [IDAY_alt, 'IDAY_alt', 5], [IPARM, 'IPARM', 5], [IDAY, 'IDAY', 5], [PARM1, 'PARM1', 10], [PARM2, 'PARM2', 10],
                       [V1, 'V1', 10], [V2, 'V2', 10], [DV, 'DV', 10], [FWHM, 'FWHM', 10], [YFLAG, 'YFLAG', 1], [XFLAG, 'XFLAG', 1],
                       [DLIMIT, 'DLIMIT', 8], [FLAGS, 'FLAGS', 7], [ASTMC, 'ASTMC', 9], [ASTMX, 'ASTMX', 10], [ASTMO, 'ASTMO', 10], [AERRH, 'AERRH', 10], [NSSALB, 'NSSALB', 10],
                       [NSURF, 'NSURF', 1], [AATEMP, 'AATEMP', 9], [DH2O, 'DH2O', 9], [MLTRFL, 'MLTRFL', 1], [SALBFL, 'SALBFL', 256], [CSALB, 'CSALB', 80]]
        
        for row in parameter_mat:
            row[0] = self.mod_fun.adjust_length(str(row[0]), row[2])


        
        open(self.tp5_directory + '/' + self.filename + '.tp5', 'w').close()
        '''erases all contents from this file'''
        
        
        for key in parameter_mat:
            if key[1] == parameter: # checks if the parameter given as function input matches a parameter in parameter_mat
                if list_values == []: # only uses beginning/end/step if there is no parameter given in parameter_mat
                    key[0] = self.mod_fun.adjust_length(str(beginning), key[2])
                    self.CARD_5 = '    1!card 5.'
                    self.write_tape5(mat = parameter_mat)
                    
                    i = beginning # here the values for the different steps are calculated and then a tape5 added to the .tp5 file
                    while i < end-step:
                        i = np.add(i, step)
                        key[0] = self.mod_fun.adjust_length(str(i), key[2]) 
                        self.CARD_5 = '    1!card 5.'
                        self.write_tape5(mat = parameter_mat)
                    
                    key[0] = self.mod_fun.adjust_length(str(end), key[2])
                    self.CARD_5 = '    0!card 5.'
                    self.write_tape5(mat = parameter_mat)
                
                else: # if list_values contains values
                    i2 = 0
                    while i2 < len(list_values)-1: # takes all values except for the last in list_values and writes a tape5 with each value to the .tp5 file
                        key[0] = self.mod_fun.adjust_length(str(list_values[i2]), key[2])
                        self.CARD_5 = '    1!card 5.'
                        self.write_tape5(mat = parameter_mat)
                        i2 += 1
                    
                    key[0] = self.mod_fun.adjust_length(str(list_values[-1]), key[2]) # takes the last value of list_values and writes the last tape5 to the file
                    self.CARD_5 = '    0!card 5.'
                    self.write_tape5(mat = parameter_mat)
                    
                    
        filename_2 = r'C:\Program Files SR\Spectral Sciences, Inc\MODTRAN(R)\5.2.1\mod5root.in' # the mod5root.in file tells MODTRAN which tape5 should be processed
        input_line = 'TEST/' + self.filename
        
        self.mod_fun.line_prepender(filename_2, '\n') # the name of the current tape5 is added to the mod5root.in file
        self.mod_fun.line_prepender(filename_2, input_line)
                    
        os.chdir(r'C:\Program Files SR\Spectral Sciences, Inc\MODTRAN(R)\5.2.1')
        subprocess.Popen('Mod5.2.1cons.exe')



        

            
                

#BuildTape5().execute_modtran(parameter = 'ITYPE', beginning = 1, end = 5, step = 0.5, list_values = [])