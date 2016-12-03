class StandardParameters(object):
    def __init__(self):
        
#         This class contains a list of all MODTRAN parameters, which are currently implemented into the program.
#         The requirements of MODTRAN concearning the definition of parameters need to be fulfilled, however
#         - all parameters will be brought to the correct length, if to short
#         - there will be a warning if a parameter is too long
#         - everything will be converted to a string
        
        

        # general input parameters
        self.output_directory = r'C:\Program Files SR\Spectral Sciences, Inc\MODTRAN(R)\5.2.1\TEST'
        self.tp5_filename = 'test_modtran_returns'
        
        # Card 1#
    
        self.MODTRN = 'T'
        # Modtran band model, choose 'C' for more accurate but slower model
        self.SPEED = ' '
        self.BINARY = ' '
        self.LYMOLC = ' '        
        # Modtran band model, choose 'C' for more accurate but slower model
        self.MODEL = 3
        self.ITYPE = 3
        self.IEMSCT = 4
#         0  Program executes in spectral transmittance only mode. 
#         1  Program executes in spectral thermal radiance (no sun / moon) mode.
#         2  Program executes in spectral thermal plus solar / lunar radiance mode (if IMULT = 0, only single scatter solar radiance is included). 
#         3 Program calculates directly transmitted spectral solar / lunar irradiance. 
#         4  Program executes in spectral solar / lunar radiance mode with no thermal scatter.  Thermal path and surface emission is included.
        self.IMULT = 1
        # 0 = without multiple scattering, +-1 = with multiple scattering
        self.I_RD2C = 0
        # 0 = normal operation mode, 1 = user input data are read
        self.NOPRNT = 0
        # defines form of output data [-2,3]
        self.SURREF = ''
        
        
        
        # Card 1A
        
        self.DIS = 'F'
#         T = discrete ordinate multiple scattering algorithm
#         F = less  accurate  but  faster  Isaacs  two-stream  algorithm
        self.NSTR = '8'
        self.CO2MX = ''
        self.H2OSTR = ''
        self.O3STR = ''
        self.LBMNAM = 'F'
        # band model data base. Do not leave blank. Use 'F' if standard band model database files should be used
        self.SOLCON = ''   
        # scale solar irradiance. Blank = default
        self.CDASTM = ''            
        # Aerosol extinction settings
        self.ASTMC = '         '
        self.ASTMX = '          '
        self.ASTMO = '          '
        self.AERRH = '        0.'
        self.NSSALB = '         0'
        
        
        # Card 1A2
        
        self.BMNAME = '15_2009'
        
        
        
        # Card 2
        
        self.IHAZE = 2
        # Aerosol model
        self.ICSTL = 0
        # Airmass character: 1-10 = Open ocean-strong continental influence
        self.ICLD = 0
        self.VIS = 23.
        self.WSS = 0.
        self.WHH = 0.
        self.GNDALT = 0.0
        
        
        
        # Card 3 standart
        
        self.H1_sta = 0.0
        # Initial Altitude
        self.H2_sta = 0.0
        # Final/tangent altitude, only relevant for ITYPE = 2,3
        self.ANGLE_sta = 30.0
        # Initial zenith angle as measured from H1
        self.RANGE_sta = 0.
        
        
        
        # Card 3 alternative
        
        self.H1ALT = 0.401
        self.H2_alt = 0.4
        self.ANGLE_alt = 180.0
        self.IDAY_alt = 93

        
        
        # Card 3A1
        
        self.IPARM = 2
        self.IDAY = 93

        
        
        # Card 3A2
        
        self.PARM1 = 0
        self.PARM2 = 30
        
        
        
        # Card 4
        
        self.V1 = 300.0
        self.V2 = 2500.0
        self.DV = 0.5
        self.FWHM = 2.0
        self.YFLAG = 'R'
        # Transmittances (T) or radiances (R) are written in .plt output file
        self.XFLAG = 'N'
        self.DLIMIT = 'DLIMIT'
        self.FLAGS = 'N      '
        # needs to be 7 characters long. Watch correct format, this is not automatically corrected


        # Card 4A
        self.NSURF = 1
        self.AATEMP = 20
        # Area-averaged ground surface temperature
        self.DH2O = 0
        # Liquid water option, water layer thickness input [mm]
        self.MLTRFL = 'F'
#         F  Embedded surface moisture attenuation model. 
#         T  Surface water layer model. 


        # Card 4L1
        self.SALBFL = 'DATA/spec_alb.dat'
#         Name  of  the  spectral  albedo  data  file.    The  default  spectral  albedo  file, 
#         'DATA/spec_alb.dat' may be used or a user-supplied file.  If a user-supplied file is 
#         specified, it must conform to the format described in the default file. 


        # ard 4L2
        self.CSALB = 5
        # Number  or  name  of  a  spectral  albedo  curve  in  the  SALBFL  file. 