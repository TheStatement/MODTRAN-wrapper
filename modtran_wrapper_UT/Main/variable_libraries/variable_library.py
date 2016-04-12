class StandardParameters(object):
    def __init__(self):
        
        '''This class contains a list of all MODTRAN parameters, which are currently implemented into the program.
        The requirements of MODTRAN concearning the definition of parameters need to be fulfilled, however
        - all parameters will be brought to the correct length, if to short
        - there will be a warning if a parameter is too long
        - everything will be converted to a string
        '''
        

        '''general input parameters'''
        self.output_directory = r'C:\Program Files SR\Spectral Sciences, Inc\MODTRAN(R)\5.2.1\TEST'
        self.tp5_filename = 'test_ried_st_1'
        
        '''Card 1'''
    
        self.MODTRN = 'T'
        '''Modtran band model, choose 'C' for more accurate but slower model'''
        self.LYMOLC = ' '        
        '''Modtran band model, choose 'C' for more accurate but slower model'''
        self.MODEL = 2
        self.ITYPE = 2
        self.IEMSCT = 4
        self.IMULT = 1
        self.I_RD2C = 1         
        '''0 = normal operation mode, 1 = user input data are read'''
        self.NOPRNT = 1
        '''defines form of output data [-2,3]'''
        
        
        
        '''Card 1A'''
        
        self.DIS = 'T'
        self.NSTR = 8
        self.CO2MX =  365.00000
        self.H2OSTR = ''
        self.O3STR = ''
        self.LBMNAM = '4'
        self.SOLCON = ''   
        '''scale solar irradiance. Blank = default'''
        self.CDASTM = 'D'            
        '''Aerosol extinction settings'''
        
        
        'Card 1A2'
        
        self.BMNAME = '15_2009'
        
        
        
        '''Card 2'''
        
        self.IHAZE = 1
        self.ICSTL = 1
        self.ICLD = 0
        self.VIS = 23.
        self.WSS = 0.
        self.WHH = 0.
        self.GNDALT = 0.4
        
        
        
        '''Card 3 standart'''
        
        self.H1_sta = 0.401
        self.H2_sta = 0.4
        self.ANGLE_sta = 180.0
        self.RANGE_sta = 0.
        
        
        
        '''Card 3 alternative'''
        
        self.H1ALT = 0.401
        self.H2_alt = 0.4
        self.ANGLE_alt = 180.0
        self.IDAY_alt = 93

        
        
        '''Card 3A1'''
        
        self.IPARM = 2
        self.IDAY = 93

        
        
        '''Card 3A2'''
        
        self.PARM1 = 90
        self.PARM2 = 50.4
        
        
        
        '''Card 4'''
        
        self.V1 = 280.0
        self.V2 = 3000.0
        self.DV = 0.5
        self.FWHM = 15.0
        self.YFLAG = 'T'
        '''Transmittances (T) or radiances (R) are written in output file'''
        self.XFLAG = 'N'
        self.DLIMIT = 'DLIMIT'
        self.FLAGS = 'NGA'

