'''created 17.11. python 3.4.3 interpreter'''

# implement the adjust length for all parameters. Raise error in adjust_length if too long beforehand
class ModtranFunctions(object):
    def __init__(self):
        #self.stan_parm = StandardParameters()
        pass
    
    

    def build_card1(self, MODTRN, SPEED, BINARY, LYMOLC, MODEL, ITYPE, IEMSCT, IMULT, I_RD2C, NOPRNT):

        MODTRN = self.adjust_length(str(MODTRN), 1)
        SPEED = self.adjust_length(str(SPEED), 1)
        BINARY = self.adjust_length(str(BINARY), 1)
        LYMOLC = self.adjust_length(str(LYMOLC), 1)
        MODEL = self.adjust_length(str(MODEL), 1)
        T_BEST = ' '
        ITYPE = self.adjust_length(str(ITYPE), 4)
        IEMSCT = self.adjust_length(str(IEMSCT), 5)
        IMULT = self.adjust_length(str(IMULT), 5)
        M1 = M2 = M3 = M4 = M5 = M6 = MDEF = '    0'
        I_RD2C = self.adjust_length(str(I_RD2C), 5)
        NOPRNT = self.adjust_length(str(NOPRNT), 5)
        TPTEMP = '    .000'
        SURREF = '    .00'
        
        CARD_1 = (MODTRN + SPEED + BINARY + LYMOLC + MODEL + T_BEST + ITYPE + IEMSCT + IMULT + M1 + M2 + M3 + M4 + M5 + M6 + MDEF + I_RD2C + NOPRNT + TPTEMP + SURREF + '!card 1.')
        return (CARD_1)
        
        
    def build_card1a(self, DIS, NSTR, CO2MX, H2OSTR, O3STR, LBMNAM, SOLCON, CDASTM):
        
        DIS = self.adjust_length(str(DIS), 1)
        DISAZM = ' '
        DISALB = ' '
        NSTR = self.adjust_length(str(NSTR), 3)
        SFWHM = '  0.'
        CO2MX = self.adjust_length(str(CO2MX), 10)
        H2OSTR = self.adjust_length(str(H2OSTR), 10)
        O3STR = self.adjust_length(str(O3STR), 10)
        C_PROF = ' '
        LSUNFL = ' '
        LBMNAM = self.adjust_length(str(LBMNAM), 2)
        LFLTNM = H2OAER = '  '
        CDTDIR = '  '
        SOLCON = self.adjust_length(str(SOLCON), 10)
        CDASTM = self.adjust_length(str(CDASTM), 1)
        ASTMC = '         '
        ASTMX = '          '
        ASTMO = '          '
        AERRH = '        0.'
        NSSALB = '         0'
        
        CARD_1A = (DIS + DISAZM + DISALB + NSTR + SFWHM + CO2MX + H2OSTR + O3STR + C_PROF + LSUNFL + LBMNAM + LFLTNM + H2OAER + CDTDIR + SOLCON + CDASTM + ASTMC + ASTMX + ASTMO + AERRH + NSSALB + '!card 1a.')
        return (CARD_1A)
        
        
    def build_card1a2(self, BMNAME):
        
        BMNAME = str(BMNAME)
        SPACER = self.adjust_length('', (256-len(str(BMNAME))))
        '''BMNAME: here a A256 input is possible. It is the root name of the band model parameter data file, which needs to be located in the same directory as the tape5
        For practical reasons the input is restricted to A80'''
        
        CARD_1A2 = (BMNAME + SPACER + '!card 1a2')
        return (CARD_1A2)
    
        
    def build_card2(self, IHAZE, ICSTL, ICLD, VIS, WSS, WHH, GNDALT):
        
        APLUS = '  '
        IHAZE = self.adjust_length(str(IHAZE), 3)
        CNOVAM = ' '
        ISEASN = '   0'
        ARUSS = '   '
        IVULCN = ' 0'
        ICSTL = self.adjust_length(str(ICSTL), 5)
        ICLD = self.adjust_length(str(ICLD), 5)
        IVSA = '    0'
        VIS = self.adjust_length(str(VIS), 10)
        WSS = self.adjust_length(str(WSS), 10)
        WHH = self.adjust_length(str(WHH), 10)
        RAINRT = '          '
        GNDALT = self.adjust_length(str(GNDALT), 10)
        
        CARD_2 = (APLUS + IHAZE + CNOVAM + ISEASN + ARUSS + IVULCN + ICSTL + ICLD + IVSA + VIS + WSS + WHH + RAINRT + GNDALT + '!card 2.')
        return (CARD_2)
        
    
    def build_card3_sta(self, H1_sta, H2_sta, ANGLE_sta, RANGE_sta):
        
        H1 = self.adjust_length(str(H1_sta), 10)
        H2 = self.adjust_length(str(H2_sta), 10)
        ANGLE = self.adjust_length(str(ANGLE_sta), 10)
        RANGE = self.adjust_length(str(RANGE_sta), 10)
        BETA = '        0.'
        RO = '        0.'
        LENN = '    0'
        PHI = '          '
        CARD_3 = (H1 + H2 + ANGLE + RANGE + BETA + RO + LENN + '     ' + PHI + '!card 3 standart')
        return (CARD_3)
        
        
    def build_card3_alt(self, H1ALT, H2_alt, ANGLE_alt, IDAY_alt):
        
        H1ALT = self.adjust_length(str(H1ALT), 10)
        H2 = self.adjust_length(str(H2_alt), 10)
        ANGLE = self.adjust_length(str(ANGLE_alt), 10)
        IDAY = self.adjust_length(str(IDAY_alt), 5)
        RO = '          '
        ISOURC = '    0'
        ANGLEM = '         0'
        
        CARD_3_alt = (H1ALT + H2 + ANGLE + IDAY + '     ' + RO + ISOURC + ANGLEM + '!card 3 alternative')
        return (CARD_3_alt)
        
        
        
    def build_card3a1(self, IPARM, IDAY):
        
        IPARM = self.adjust_length(str(IPARM), 5)
        IPH = '    2'
        IDAY = self.adjust_length(str(IDAY), 5)
        ISOURC = '    0'
        
        CARD_3A1 = (IPARM + IPH + IDAY + ISOURC + '!card 3a1')
        return CARD_3A1
        
        
    
    def build_card3a2(self, PARM1, PARM2):
        
        PARM1 = self.adjust_length(str(PARM1), 10)
        PARM2 = self.adjust_length(str(PARM2), 10)
        PARM3 = '         1'
        PARM4 = '         2'
        TIME = '         3'
        PSIPO = '         4'
        ANGLEM = '         5'
        G = '         6'
        
        CARD_3A2 = (PARM1 + PARM2 + PARM3 + PARM4 + TIME + PSIPO + ANGLEM + G + '!card 3a2')
        return CARD_3A2
        
        

        
        
    def build_card4(self, V1, V2, DV, FWHM, YFLAG, XFLAG, DLIMIT, FLAGS):
        
        V1 = self.adjust_length(str(V1), 10)
        V2 = self.adjust_length(str(V2), 10)
        DV = self.adjust_length(str(DV), 10)
        FWHM = self.adjust_length(str(FWHM), 10)
        YFLAG = self.adjust_length(str(YFLAG), 1)
        XFLAG = self.adjust_length(str(XFLAG), 1)
        DLIMIT = self.adjust_length(str(DLIMIT), 8)
        FLAGS = self.adjust_length(str(FLAGS), 7)
        MLFLX = '   '
        VRFRAC = '          '
        
        CARD_4 = (V1 + V2 + DV + FWHM + YFLAG + XFLAG + DLIMIT + FLAGS + MLFLX + VRFRAC + '!card 4.')
        return (CARD_4)
        
    ### End of build card functions



### this function checks, if all cards have the required length. It returns error messages to the ui window if smth is out of range
    def check_tape5(self, CARD_1, CARD_1A, CARD_2, CARD_3_STA, CARD_3_ALT, CARD_3A1, CARD_3A2, CARD_4, CARD_5):
        answer = ''
        
        name_of_cards = {CARD_1: 'Card 1', CARD_1A: 'Card 1A', CARD_2: 'Card 2', CARD_3_STA: 'Card 3 (standart)', CARD_3_ALT: 'Card 3 (alternative)',
        CARD_3A1: 'Card 3A1', CARD_3A2: 'Card 3A2', CARD_4: 'Card 4', CARD_5: 'Card 5'}
        
        list_of_cards = {CARD_1: 88, CARD_1A: 119, CARD_2: 88, CARD_3_STA: 96, CARD_3_ALT: 84, CARD_3A1: 29, CARD_3A2: 89, CARD_4: 78, CARD_5: 13}
        
        if len(CARD_1) == list_of_cards[CARD_1] and len(CARD_1A) == list_of_cards[CARD_1A] and len(CARD_2) == list_of_cards[CARD_2] \
            and len(CARD_3_STA) == list_of_cards[CARD_3_STA] and len(CARD_3_ALT) == list_of_cards[CARD_3_ALT] \
            and len(CARD_3A1) == list_of_cards[CARD_3A1] and len(CARD_3A2) == list_of_cards[CARD_3A2] \
            and len(CARD_4) == list_of_cards[CARD_4] and len(CARD_5) == list_of_cards[CARD_5]:
            answer += ('Tape length OK')

        else:
            for card in list_of_cards:
                if len(card) != list_of_cards[card]:
                    answer += (name_of_cards[card] + ' is deficient.' + ' Length ' + str(len(card)) + ' instead of ' + str(list_of_cards[card]) + '\n')
        print (answer)
                
                
### adjust_length adds spaces to a parameter, if the length is not correct for implementation into a card. Requires a string and a int for input
    def adjust_length(self, parameter, length):
        '''adjust_length adds spaces to the left of the string to adjust, till the given length is reached
        It takes a string as 'parameter' and a integer as 'length' '''
        if type(parameter) != type('') or type(length) != type(1):
            print ('Type of adjust_length input parameters is not correct')
        if len(parameter) > length:
            print('parameter <' + parameter + '> is too long!')
        else:
            while len(parameter) < length:
                parameter = ' ' + parameter
        return (parameter)
        
        
    def remove_from_list(self, the_list, val):
        while val in the_list:
            the_list.remove(val)
            
            
    def find_in_array(self, mat, word):
        '''this function searches in an array (mat) with the form of parameter_mat in build_tape5 for a keyword (word)
        and returns the corresponding value of a different column.'''
        
        for row in mat:
            if row[1] == word:
                return row[0]
            
    
    def convert_wn_nm(self, wavenumbers):
        output = []
        for number in wavenumbers:
            tmp = 10000000/float(number)
            tmp = "%.1f" % tmp
            output.append(tmp)
            
        return(output)
    
    
    def line_prepender(self, filename, line):
        with open(filename, 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write(line.rstrip('\r\n') + '\n' + content)
            


