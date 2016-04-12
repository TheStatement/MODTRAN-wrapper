'''
Created on Feb 3, 2016

@author: ried_st
'''

import matplotlib.pyplot as plt
from Main.modtran_functions import ModtranFunctions
from Main.tape7_reader import Tape7_reader
from Main.seven_sc_reader import Seven_sc_reader
from Main.universal_reader import Universal_reader
from Main.plot_series import Plot_series


Main = ModtranFunctions()
Tape7 = Tape7_reader()
Seven_sc = Seven_sc_reader()
Universal = Universal_reader()
Plot = Plot_series()


#tape7 = Tape7.read_tape7(r'C:\Users\ried_st\Desktop\Temporal eclipse workspace\PG_Alte Modtran Rechnungen\neu gerechnet\20160217_1', '20160217_1', 'y')
#plt.plot(tape7[3][0][0], tape7[3][0][2])
#plt.show()

#nanometers = Main.convert_wn_nm(tape7[3][0][0])


seven_sc = Seven_sc.read_seven_sc(r'C:\Users\ried_st\Desktop\Temporal eclipse workspace\PG_Alte Modtran Rechnungen\neu gerechnet\20160218_4_H2OSTR Serie', '20160218_4')
#plt.plot(seven_sc[3][0][0], seven_sc[3][0][1])
#plt.show()

#Universal.get_list_parameters(file_directory = r'C:\Users\Basti\Desktop\Temporal eclipse workspace\PG_Alte Modtran Rechnungen', filename = 'Modtran_T', file_extension = '.dat')
universal = Universal.read_universal(file_directory = r'C:\Users\ried_st\Desktop\Temporal eclipse workspace\PG_Alte Modtran Rechnungen', filename = 'Modtran_T', file_extension = '.dat', number_rows = 8)
#plt.plot(universal[3][0][0], universal[3][0][2])
#plt.show()

labels = ['almost no water', 'standart water atmosphere*0.5', '*1', '*1.5', '*2', '*2.5', '*3']
Plot.plot_series(seven_sc[3], 0, 1, labels)

'''x1 = seven_sc[3][0][0]
y1 = seven_sc[3][0][1]

x2 = seven_sc[3][1][0]
y2 = seven_sc[3][1][1]

x3 = seven_sc[3][2][0]
y3 = seven_sc[3][2][1]

fig = plt.figure()
#plt.plot(x1, y1, 'b-', label = '1')
plt.plot(x2, y2, 'g-', label = '2')
plt.plot(x3, y3, 'r-', label = '3')
plt.xlabel('Wavelength', fontsize = 18)
plt.ylabel('Transmission atmosphere', fontsize = 18)
legend = plt.legend(shadow=True)


plt.show()'''
