'''
Created on Feb 18, 2016

@author: ried_st
'''

import matplotlib.pyplot as plt

class Plot_series(object):
    def __init__(self):
        pass

    def plot_series(self, matrix, col1, col2, labels):
        
        colors2 = ['#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c',
                  '#98df8a', '#d62728', '#ff9896', '#9467bd', '#c5b0d5',
                  '#8c564b', '#c49c94', '#e377c2', '#f7b6d2', '#7f7f7f',
                  '#c7c7c7', '#bcbd22', '#dbdb8d', '#17becf', '#9edae5']

        
        fig = plt.figure()
        for i in range(0, len(matrix)):
            xi = matrix[i][col1]
            yi = matrix[i][col2]
            plt.plot(xi, yi, colors2[i], label = labels[i])
            
        plt.xlabel('Wavelength', fontsize = 18)
        plt.ylabel('Transmission atmosphere', fontsize = 18)
        legend = plt.legend(shadow=True, loc = 'upper left')
        
        plt.show()