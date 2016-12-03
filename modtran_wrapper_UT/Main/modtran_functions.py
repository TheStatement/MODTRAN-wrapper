'''created 17.11. python 3.4.3 interpreter'''

# implement the adjust length for all parameters. Raise error in adjust_length if too long beforehand
class ModtranFunctions(object):
    def __init__(self):
        #self.stan_parm = StandardParameters()
        pass



### this function checks, if all cards have the required length. It returns error messages to the ui window if smth is out of range
    def check_tape5(self, CARD_1, CARD_1A, CARD_2, CARD_3_STA, CARD_3_ALT, CARD_3A1, CARD_3A2, CARD_4, CARD_4A, CARD_4L1, CARD_4L2, CARD_5):
        answer = ''
        
        name_of_cards = {CARD_1: 'CARD_1', CARD_1A: 'CARD_1A', CARD_2: 'CARD_2', CARD_3_STA: 'CARD_3 (standart)', CARD_3_ALT: 'CARD_3 (alternative)',
        CARD_3A1: 'CARD_3A1', CARD_3A2: 'CARD_3A2', CARD_4: 'CARD_4', 'CARD_4A': CARD_4A, 'CARD_4L1': CARD_4L1, 'CARD_4L2': CARD_4L2, CARD_5: 'CARD_5'}
        
        list_of_cards = {CARD_1: 88, CARD_1A: 119, CARD_2: 88, CARD_3_STA: 96, CARD_3_ALT: 84, CARD_3A1: 29, CARD_3A2: 89, CARD_4: 78, CARD_4A: 28, CARD_4L1: 265, CARD_4L2: 89,  CARD_5: 13}
        
        if len(CARD_1) == list_of_cards[CARD_1] and len(CARD_1A) == list_of_cards[CARD_1A] and len(CARD_2) == list_of_cards[CARD_2] \
            and len(CARD_3_STA) == list_of_cards[CARD_3_STA] and len(CARD_3_ALT) == list_of_cards[CARD_3_ALT] \
            and len(CARD_3A1) == list_of_cards[CARD_3A1] and len(CARD_3A2) == list_of_cards[CARD_3A2] \
            and len(CARD_4) == list_of_cards[CARD_4] and len(CARD_4A) == list_of_cards[CARD_4A] and len(CARD_4L1) == list_of_cards[CARD_4L1] \
            and len(CARD_4L2) == list_of_cards[CARD_4L2] and len(CARD_5) == list_of_cards[CARD_5]:
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
            


