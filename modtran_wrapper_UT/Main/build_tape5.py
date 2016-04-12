'''
Created on Nov 25, 2015

@author: ried_st
'''

import subprocess, os
from Main.modtran_functions import ModtranFunctions
from Main.variable_library import StandardParameters



class BuildTape5(object):
    def __init__(self):
        self.stan_parm = StandardParameters()
        self.tp5_directory = self.stan_parm.output_directory
        self.filename = self.stan_parm.tp5_filename
        
        self.modtran_functions = ModtranFunctions()
    
    
    def assemble_tape5(self, mat):
        
        self.card1 = self.modtran_functions.build_card1(self.modtran_functions.find_in_array(mat, 'MODTRN'), self.modtran_functions.find_in_array(mat, 'LYMOLC'),
                                                        self.modtran_functions.find_in_array(mat, 'MODEL'), self.modtran_functions.find_in_array(mat, 'ITYPE'),
                                                        self.modtran_functions.find_in_array(mat, 'IEMSCT'), self.modtran_functions.find_in_array(mat, 'IMULT'), 
                                                        self.modtran_functions.find_in_array(mat, 'I_RD2C'), self.modtran_functions.find_in_array(mat, 'NOPRNT'))
        
        self.card1a = self.modtran_functions.build_card1a(self.modtran_functions.find_in_array(mat, 'DIS'), self.modtran_functions.find_in_array(mat, 'NSTR'), 
                                                          self.modtran_functions.find_in_array(mat, 'CO2MX'), self.modtran_functions.find_in_array(mat, 'H2OSTR'), 
                                                          self.modtran_functions.find_in_array(mat, 'O3STR'), self.modtran_functions.find_in_array(mat, 'LBMNAM'),
                                                          self.modtran_functions.find_in_array(mat, 'SOLCON'), self.modtran_functions.find_in_array(mat, 'CDASTM'))
        
        self.card1a2 = self.modtran_functions.build_card1a2(self.modtran_functions.find_in_array(mat, 'BMNAME'))
        
        self.card2 = self.modtran_functions.build_card2(self.modtran_functions.find_in_array(mat, 'IHAZE'), self.modtran_functions.find_in_array(mat, 'ICSTL'), 
                                                        self.modtran_functions.find_in_array(mat, 'ICLD'), self.modtran_functions.find_in_array(mat, 'VIS'), 
                                                        self.modtran_functions.find_in_array(mat, 'WSS'), self.modtran_functions.find_in_array(mat, 'WHH'), 
                                                        self.modtran_functions.find_in_array(mat, 'GNDALT'))
        
        self.card3sta = self.modtran_functions.build_card3_sta(self.modtran_functions.find_in_array(mat, 'H1_sta'), self.modtran_functions.find_in_array(mat, 'H2_sta'), 
                                                               self.modtran_functions.find_in_array(mat, 'ANGLE_sta'), self.modtran_functions.find_in_array(mat, 'RANGE_sta'))
        
        self.card3alt = self.modtran_functions.build_card3_alt(self.modtran_functions.find_in_array(mat, 'H1ALT'), self.modtran_functions.find_in_array(mat, 'H2_alt'), 
                                                               self.modtran_functions.find_in_array(mat, 'ANGLE_alt'), self.modtran_functions.find_in_array(mat, 'IDAY_alt'))
        
        self.card3a1 = self.modtran_functions.build_card3a1(self.modtran_functions.find_in_array(mat, 'IPARM'), self.modtran_functions.find_in_array(mat, 'IDAY'))
        
        self.card3a2 = self.modtran_functions.build_card3a2(self.modtran_functions.find_in_array(mat, 'PARM1'), self.modtran_functions.find_in_array(mat, 'PARM2'))
        
        self.card4 = self.modtran_functions.build_card4(self.modtran_functions.find_in_array(mat, 'V1'), self.modtran_functions.find_in_array(mat, 'V2'), 
                                                        self.modtran_functions.find_in_array(mat, 'DV'), self.modtran_functions.find_in_array(mat, 'FWHM'), 
                                                        self.modtran_functions.find_in_array(mat, 'YFLAG'), self.modtran_functions.find_in_array(mat, 'XFLAG'), 
                                                        self.modtran_functions.find_in_array(mat, 'DLIMIT'), self.modtran_functions.find_in_array(mat, 'FLAGS'))


        self.modtran_functions.check_tape5(self.card1, self.card1a, self.card2, self.card3sta, self.card3alt, self.card3a1, self.card3a2, self.card4, self.card5)
        
    def write_tape5(self, mat):
        '''Caution: the order in 'used_cards' is important for the correct assembly of tape5'''
        self.filename = self.stan_parm.tp5_filename
        self.assemble_tape5(mat)
        
        available_cards = {'card1': self.card1, 'card1a': self.card1a, 'card1a2': self.card1a2, 'card2': self.card2, 'card3sta': self.card3sta,
                           'card3alt': self.card3alt, 'card3a1': self.card3a1, 'card3a2': self.card3a2, 'card4': self.card4, 'card5': self.card5}
        used_cards = ['card1', 'card1a']
        
        if any(str(self.stan_parm.LBMNAM) in s for s in ['T', 't', '2', '4']):
            used_cards.append('card1a2')
        
        used_cards.append('card2')
        
        if any(str(self.stan_parm.IEMSCT) in s for s in ['2', '4']):
            used_cards.extend(['card3sta', 'card3a1', 'card3a2'])
        elif str(self.stan_parm.IEMSCT) == '3':
            used_cards.extend(['card3alt', 'card3a1', 'card3a2'])
        else:
            used_cards.append('card3sta')

        used_cards.extend(['card4', 'card5'])
        
        
        tape5 = []
        for card in used_cards:
            if card in available_cards:
                tape5.append(available_cards[card])
                tape5.append('\n')
        
        tape5.extend(['\n', '\n', '\n'])
        
        new_tape5 = open(self.tp5_directory + '/' + self.filename + '.tp5', 'a')

        new_tape5.writelines(tape5)
        new_tape5.close()
    

    
    
    def execute_modtran(self, parameter, beginning, end, step, list_values):
        '''this function creates a .tp5 file and starts a MODTRAN run
        It has the ability to iterate over a specific parameter
        Needs to set tape5'''
        
        
        MODTRN = self.stan_parm.MODTRN
        MODEL = self.stan_parm.MODEL
        LYMOLC = self.stan_parm.LYMOLC
        ITYPE = self.stan_parm.ITYPE
        IEMSCT = self.stan_parm.IEMSCT
        IMULT = self.stan_parm.IMULT
        I_RD2C = self.stan_parm.I_RD2C
        NOPRNT = self.stan_parm.NOPRNT
        DIS = self.stan_parm.DIS
        NSTR = self.stan_parm.NSTR
        CO2MX = self.stan_parm.CO2MX 
        H2OSTR = self.stan_parm.H2OSTR
        O3STR = self.stan_parm.O3STR
        LBMNAM = self.stan_parm.LBMNAM
        SOLCON = self.stan_parm.SOLCON
        CDASTM = self.stan_parm.CDASTM
        BMNAME = self.stan_parm.BMNAME
        IHAZE = self.stan_parm.IHAZE
        ICSTL = self.stan_parm.ICSTL
        ICLD = self.stan_parm.ICLD
        VIS = self.stan_parm.VIS
        WSS = self.stan_parm.WSS
        WHH = self.stan_parm.WHH
        GNDALT = self.stan_parm.GNDALT
        H1_sta = self.stan_parm.H1_sta
        H2_sta = self.stan_parm.H2_sta
        ANGLE_sta = self.stan_parm.ANGLE_sta
        RANGE_sta = self.stan_parm.RANGE_sta
        H1ALT = self.stan_parm.H1ALT
        H2_alt = self.stan_parm.H2_alt
        ANGLE_alt = self.stan_parm.ANGLE_alt
        IDAY_alt = self.stan_parm.IDAY_alt
        IPARM = self.stan_parm.IPARM
        IDAY = self.stan_parm.IDAY
        PARM1 = self.stan_parm.PARM1
        PARM2 = self.stan_parm.PARM2
        V1 = self.stan_parm.V1
        V2 = self.stan_parm.V2
        DV = self.stan_parm.DV
        FWHM = self.stan_parm.FWHM
        YFLAG = self.stan_parm.YFLAG
        XFLAG = self.stan_parm.XFLAG
        DLIMIT = self.stan_parm.DLIMIT
        FLAGS = self.stan_parm.FLAGS
        

        parameter_mat = [[MODTRN, 'MODTRN', 1], [LYMOLC, 'LYMOLC', 1], [MODEL, 'MODEL', 1], [ITYPE, 'ITYPE', 4], [IEMSCT, 'IEMSCT', 5],
                       [IMULT, 'IMULT', 5], [I_RD2C, 'I_RD2C', 5], [NOPRNT, 'NOPRNT', 5], [DIS, 'DIS', 1], [NSTR, 'NSTR', 3],
                       [CO2MX, 'CO2MX', 10], [H2OSTR, 'H2OSTR', 10], [O3STR, 'O3STR', 10], [LBMNAM, 'LBMNAM', 2], [SOLCON, 'SOLCON', 10], [CDASTM, 'CDASTM', 1],
                       [BMNAME, 'BMNAME', 80], [IHAZE, 'IHAZE', 3], [ICSTL, 'ICSTL', 5], [ICLD, 'ICLD', 5], [VIS, 'VIS', 10], [WSS, 'WSS', 10],
                       [WHH, 'WHH', 10], [GNDALT, 'GNDALT', 10], [H1_sta, 'H1_sta', 10], [H2_sta, 'H2_sta', 10], [ANGLE_sta, 'ANGLE_sta', 10],
                       [RANGE_sta, 'RANGE_sta', 10], [H1ALT, 'H1ALT', 10], [H2_alt, 'H2_alt', 10], [ANGLE_alt, 'ANGLE_alt', 10],
                       [IDAY_alt, 'IDAY_alt', 5], [IPARM, 'IPARM', 5], [IDAY, 'IDAY', 5], [PARM1, 'PARM1', 10], [PARM2, 'PARM2', 10],
                       [V1, 'V1', 10], [V2, 'V2', 10], [DV, 'DV', 10], [FWHM, 'FWHM', 10], [YFLAG, 'YFLAG', 1], [XFLAG, 'XFLAG', 1],
                       [DLIMIT, 'DLIMIT', 8], [FLAGS, 'FLAGS', 7]]
        
        for row in parameter_mat:
            self.modtran_functions.adjust_length(str(row[0]), row[2])


        
        open(self.tp5_directory + '/' + self.filename + '.tp5', 'w').close()
        '''erases all contents from this file'''
        
        
        for key in parameter_mat:
            if key[1] == parameter:
                if list_values == []:
                    key[0] = self.modtran_functions.adjust_length(str(beginning), key[2])
                    self.card5 = '    1!card 5'
                    self.write_tape5(mat = parameter_mat)
                    
                    i = beginning
                    while i < end-step:
                        i += step
                        key[0] = self.modtran_functions.adjust_length(str(i), key[2]) 
                        self.card5 = '    1!card 5'
                        self.write_tape5(mat = parameter_mat)
                    
                    key[0] = self.modtran_functions.adjust_length(str(end), key[2])
                    self.card5 = '    0!card 5'
                    self.write_tape5(mat = parameter_mat)
                
                else:
                    i2 = 1
                    while i2 < len(list_values):
                        print (len(list_values))
                        i2 += 1
                        key[0] = self.modtran_functions.adjust_length(str(list_values[i2]), key[2])
                        self.card5 = '    1!card 5'
                        self.write_tape5(mat = parameter_mat)
                    
                    key[0] = self.modtran_functions.adjust_length(str(list_values[-1]), key[2])
                    self.card5 = '    0!card 5'
                    self.write_tape5(mat = parameter_mat)
                    
                    
        '''modtran_exe = (r'C:\Program Files SR\Spectral Sciences, Inc\MODTRAN(R)\5.2.1\Mod5.2.1qwin.exe')
        process = subprocess.Popen(modtran_exe, stdout=subprocess.PIPE)
        process.wait()'''
        
        #subprocess.call(os.path.join(self.stan_parm.output_directory + 'Mod5.2.1qwin.exe'))
        #subprocess.call(r'C:\Programme_SR\Spectral Sciences, Inc\MODTRAN(R)\5.2.1Mod5.2.1qwin.exe')



        

            
                

#BuildTape5().execute_modtran(parameter = 'ITYPE', beginning = 1, end = 5, step = 0.5, list_values = [])