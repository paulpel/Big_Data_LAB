import numpy as np
import matplotlib.pyplot as plt

class Autocorrelation:
    '''Klasa zajmująca się autokorelacja'''

    def __init__(self):
        '''Inicjalizacja zmiennych'''
        self.number_of_probes = 1000
        self.time_delatation = 500
        self.arguments_t = np.linspace(-1,1,self.number_of_probes)
        self.signal = np.sin(np.pi * self.arguments_t)
        self.results =[]

    def autocorrelation(self):
        for r in range(self.time_delatation):
            temp = 0
            for i in range(1,self.number_of_probes-r):
                temp += self.signal[i] * self.signal[i-r]
            temp = (1/(self.number_of_probes-r))*temp
            self.results.append(temp)

    def visualization(self):
        ''''''
        plt.plot(self.results)
        plt.show()

au = Autocorrelation()
au.autocorrelation()
au.visualization()
