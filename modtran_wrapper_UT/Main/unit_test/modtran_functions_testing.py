'''
Created on 17.11.2015

@author: Basti
'''


# Mehrere Tests pro Funktion, Ergebnis kennen und nicht erzeugen?

import unittest
from Main.modtran_functions import ModtranFunctions

class TestModtranFunctions(unittest.TestCase):
    
    modtran_functions = ModtranFunctions()
    def test_build_card1(self):
        result = modtran_functions.build_card1(self, MODEL = '2', LYMOLC = '+', ITYPE = '2', IEMSCT = '2', IMULT = '1')
        self.assertEqual(result, 'TM +2    2    2    1    0    0    0    0    0    0    0    0    1   0.300   0.00!Card 1', 'Card 1 is deficient')
        
    def test_build_card1a(self):
        result = modtran_functions.build_card1a(self, DIS = 'T', NSTR = '8', CO2MX = ' 365.00000', H2OSTR = '', O3STR = '')
        self.assertEqual(result, 'T  8  0. 365.00000                    0F 4 F F F          D                   !Card 1a', 'Card 1a is deficient')
        
    def test_build_card2(self):
        pass
    
    def test_build_card3_sta(self):
        pass
    
    def test_build_card3_alt(self):
        pass
    
    def test_build_card3a1(self):
        pass
    
    def test_build_card3a2(self):
        pass
    
    def test_build_card4(self):
        pass
    
    def test_check_tape5(self):
        result1 = modtran_functions.check_tape5(self, CARD_1 = '                                                                                ', 
        CARD_1A = '                                                                                ', CARD_2 = '                                                                                ', 
        CARD_3_STA = '                                                                                ', CARD_3_ALT = '                                                                 ', 
        CARD_3A1 = '                    ', CARD_3A2 = '                                                                                ', 
        CARD_4 = '                                                                      ', CARD_5 = '     ')
        self.assertEqual(result1, 'Tape length OK', 'check_tape5 failed')
        
        result2 = modtran_functions.check_tape5(self, CARD_1 = '                                                                             ', 
        CARD_1A = '                                                                                ', CARD_2 = '                                                                                ', 
        CARD_3_STA = '                                                                                ', CARD_3_ALT = '                                                                 ', 
        CARD_3A1 = '                    ', CARD_3A2 = '                                                                                ', 
        CARD_4 = '                                                                      ', CARD_5 = '     ')
        self.assertEqual(result2, 'Card 1 is deficient. Length 77 instead of 80\n', 'check_tape5 failed at card 1')
        
        result3 = modtran_functions.check_tape5(self, CARD_1 = '                                                                                ', 
        CARD_1A = '                                                                            ', CARD_2 = '                                                                                ', 
        CARD_3_STA = '                                                                                ', CARD_3_ALT = '                                                                 ', 
        CARD_3A1 = '                    ', CARD_3A2 = '                                                                                ', 
        CARD_4 = '                                                                      ', CARD_5 = '     ')
        self.assertEqual(result3, 'Card 1A is deficient. Length 76 instead of 80\n', 'check_tape5 failed at card 1a')
        
        result4 = modtran_functions.check_tape5(self, CARD_1 = '                                                                                ', 
        CARD_1A = '                                                                                ', CARD_2 = '                                                                           ', 
        CARD_3_STA = '                                                                                ', CARD_3_ALT = '                                                                 ', 
        CARD_3A1 = '                    ', CARD_3A2 = '                                                                                ', 
        CARD_4 = '                                                                      ', CARD_5 = '     ')
        self.assertEqual(result4, 'Card 2 is deficient. Length 75 instead of 80\n', 'check_tape5 failed at card 2')
        
        result5 = modtran_functions.check_tape5(self, CARD_1 = '                                                                                ', 
        CARD_1A = '                                                                                ', CARD_2 = '                                                                                ', 
        CARD_3_STA = '                                                                          ', CARD_3_ALT = '                                                                 ', 
        CARD_3A1 = '                    ', CARD_3A2 = '                                                                                ', 
        CARD_4 = '                                                                      ', CARD_5 = '     ')
        self.assertEqual(result5, 'Card 3 (standart) is deficient. Length 74 instead of 80\n', 'check_tape5 failed at card 3 (standart)')
        
        result6 = modtran_functions.check_tape5(self, CARD_1 = '                                                                                ', 
        CARD_1A = '                                                                                ', CARD_2 = '                                                                                ', 
        CARD_3_STA = '                                                                                ', CARD_3_ALT = '                                                              ', 
        CARD_3A1 = '                    ', CARD_3A2 = '                                                                                ', 
        CARD_4 = '                                                                      ', CARD_5 = '     ')
        self.assertEqual(result6, 'Card 3 (alternative) is deficient. Length 62 instead of 65\n', 'check_tape5 failed at card 3 (alternative)')
        
        result7 = modtran_functions.check_tape5(self, CARD_1 = '                                                                                ', 
        CARD_1A = '                                                                                ', CARD_2 = '                                                                                ', 
        CARD_3_STA = '                                                                                ', CARD_3_ALT = '                                                                 ', 
        CARD_3A1 = '                 ', CARD_3A2 = '                                                                                ', 
        CARD_4 = '                                                                      ', CARD_5 = '     ')
        self.assertEqual(result7, 'Card 3A1 is deficient. Length 17 instead of 20\n', 'check_tape5 failed at card 3a1')
        
        result8 = modtran_functions.check_tape5(self, CARD_1 = '                                                                                ', 
        CARD_1A = '                                                                                ', CARD_2 = '                                                                                ', 
        CARD_3_STA = '                                                                                ', CARD_3_ALT = '                                                                 ', 
        CARD_3A1 = '                    ', CARD_3A2 = '                                                                             ', 
        CARD_4 = '                                                                      ', CARD_5 = '     ')
        self.assertEqual(result8, 'Card 3A2 is deficient. Length 77 instead of 80\n', 'check_tape5 failed at card 3a2')
        
        result9 = modtran_functions.check_tape5(self, CARD_1 = '                                                                                ', 
        CARD_1A = '                                                                                ', CARD_2 = '                                                                                  ', 
        CARD_3_STA = '                                                                                ', CARD_3_ALT = '                                                                 ', 
        CARD_3A1 = '                 ', CARD_3A2 = '                                                                                ', 
        CARD_4 = '                                                                         ', CARD_5 = '     ')
        self.assertEqual(result9, 'Card 4 is deficient. Length 73 instead of 70\nCard 2 is deficient. Length 82 instead of 80\nCard 3A1 is deficient. Length 17 instead of 20\n', 'check_tape5 failed at multiple cards')
        
    def test_adjust_length(self):
        result = modtran_functions.adjust_length(self, '', 10)
        self.assertEqual(result, '          ', 'adjust length failed')
        
        result2 = modtran_functions.adjust_length(self, '456', 8)
        self.assertEqual(result2, '456     ', 'adjust length failed')