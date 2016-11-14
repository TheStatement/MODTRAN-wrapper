'''
Created on 29.11.2015

@author: Basti
'''

from Main.tape5_reader import Tape5_reader
from Main.main import BuildTape5
from Main.tape7_reader import Tape7_reader
from Main.seven_sc_reader import Seven_sc_reader
from Main.tape6_reader import Tape6_Reader

Tape5 = Tape5_reader()
execute = BuildTape5()
Tape7 = Tape7_reader()
Tape6 = Tape6_Reader()
seven_sc = Seven_sc_reader()

# execute.execute_modtran('H2OSTR', beginning = 0.00001, end = 3, step = 1, list_values = [])
#Tape5.read_tape5(r'C:\Users\ried_st\Desktop\Temporal eclipse workspace\PG_Alte Modtran Rechnungen\neu gerechnet', 'test_ried_st_1')
#test = Tape7.read_tape7(r'C:\Users\ried_st\OneDrive\Austausch\Programming\PG_Alte Modtran Rechnungen\neu gerechnet', 'test_ried_st_1')
#print (test)

# seven_sc = seven_sc.read_seven_sc(r'C:\Users\ried_st\OneDrive\Austausch\Programming_2\PG_Alte Modtran Rechnungen\neu gerechnet', 'test_ried_st_1')
# print(seven_sc[3][0][1])

tape6 = Tape6.read_tape6(directory = r'C:\Program Files SR\Spectral Sciences, Inc\MODTRAN(R)\5.2.1\TEST', filename = 'test_modtran_returns.tp6')
print(tape6['beginning_data'])