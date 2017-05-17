import numpy as np
import math
import pandas as pd
import pylab

class Simple_figures(object):
    def __init__(self,h):
        self.X = [-800, -400, -200, -100, -80, -60, -40, -20, -10, -5, 0, 5, 10, 20, 40, 60, 80, 100, 200, 400, 800]
        self.h = h

class Sphere(Simple_figures):
    '''
    solves direct problem of magnetometry for the uniformly magnetized sphere
    '''
    def __init__(self, h, J, r):
        '''
        Initializes sphere's parameters
        '''
        Simple_figures.__init__(self,h)
        self.M = 4* math.pi/3 * math.pow(r,3) * J
        self.Ha1, self.Za1, self.Ta1 = [], [], []
        self.Ha1_nTl, self.Za1_nTl, self.Ta1_nTl = [], [], []


    def gamma_sphere(self):
        for i in range(0, len(self.X)):
            self.Ha1.append(-3 * self.M * self.X[i] * self.h /math.sqrt(math.pow((self.X[i]*self.X[i]+self.h*self.h),5)))
            self.Za1.append(self.M * (2 * self.h*self.h - self.X[i]*self.X[i]) / math.sqrt(math.pow((self.X[i]*self.X[i]+self.h*self.h),5)))
            self.Ta1.append(self.M * self.h / math.sqrt(math.pow((self.X[i]*self.X[i]+self.h*self.h),5)))

    def nTl_sphere(self):
        for i in range(0, len(self.Ha1)):
            self.Ha1_nTl.append(self.Ha1[i] * math.pow(10,5))
            self.Za1_nTl.append(self.Za1[i] * math.pow(10,5))
            self.Ta1_nTl.append(self.Ta1[i] * math.pow(10,5))

    def get_sphere_output(self):
        table_sphere = pd.DataFrame({'Ha,gamma': self.Ha1,
                'Ta, gamma': self.Ta1,
                'Za, gamma': self.Za1,
                'Ha, nTl': self.Ha1_nTl,
                'Za, nTl': self.Za1_nTl,
                'Ta, nTl': self.Ta1_nTl}, index=self.X)
        print table_sphere


    def visualize_sphere(self):
        pylab.plot(np.polyval(self.X,self.Ha1))
        pylab.grid(True)
        pylab.show()


class Cylinder(Simple_figures):
    '''
        solves direct problem of magnetometry for the cylinder
    '''
    def __init__(self, h, R, sigma):
        Simple_figures.__init__(self, h)
        self.M1 = math.pi*math.pow(R,2)*sigma
        self.Ha2, self.Za2 = [], []
        self.Ha2_nTl, self.Za2_nTl, = [], []

    def gamma_cylinder(self):
        for i in range(0, len(self.X)):
            self.Ha2.append(4*self.M1*self.h*self.X[i]/math.pow((self.X[i]*self.X[i]+self.h*self.h),2))
            self.Za2.append(2*self.M1*(self.h*self.h-self.X[i]*self.X[i])/math.pow((self.X[i]*self.X[i]+self.h*self.h),2))

    def nTl_cylinder(self):
        for i in range(0, len(self.Ha2)):
            self.Ha2_nTl.append(self.Ha2[i] * math.pow(10,5))
            self.Za2_nTl.append(self.Za2[i] * math.pow(10,5))

    def get_cylinder_output(self):
        table_cylinder = pd.DataFrame({'Ha,gamma': self.Ha2,
                                      'Za, gamma': self.Za2,
                                     'Ha, nTl': self.Ha2_nTl,
                                     'Za, nTl': self.Za2_nTl}, index=self.X)
        print table_cylinder

class Cylinder_slanting_m(Simple_figures):
    '''
        solves direct problem of magnetometry for the cylinder with slanting magnetization
    '''
    def __init__(self, h, ksi, R, sigma):
        Simple_figures.__init__(self, h)
        self.ksi = ksi
        self.M1 = math.pi * math.pow(R, 2) * sigma
        self.Ha3, self.Za3 = [], []
        self.Ha3_nTl, self.Za3_nTl, = [], []

    def gamma_slanting_m(self):
        for i in range(0, len(self.X)):
            self.Ha3.append(-2*self.M1*((self.h*self.h-self.X[i]*self.X[i])*math.sin(self.ksi)+2*self.h*self.X[i]*math.cos(self.ksi))/math.pow((self.X[i]*self.X[i]+self.h*self.h),2))
            self.Za3.append(2*self.M1*((self.h*self.h-self.X[i]*self.X[i])*math.sin(self.ksi)-2*self.h*self.X[i]*math.cos(self.ksi))/math.pow((self.X[i]*self.X[i]+self.h*self.h),2))

    def nTl_sl_cylinder(self):
        for i in range(0, len(self.Ha3)):
            self.Ha3_nTl.append(self.Ha3[i] * math.pow(10, 5))
            self.Za3_nTl.append(self.Za3[i] * math.pow(10, 5))

    def get_slanting_m(self):
        sl_cylinder = pd.DataFrame({'Ha,gamma': self.Ha3,
                                       'Za, gamma': self.Za3,
                                       'Ha, nTl': self.Ha3_nTl,
                                       'Za, nTl': self.Za3_nTl}, index=self.X)
        print sl_cylinder

class Stock(Simple_figures):
    '''solver direct problem for restricted vertical stock'''
    def __init__(self, h, R, sigma, h1, a):
        Simple_figures.__init__(self, h)
        self.M1 = math.pi*R^2*sigma
        self.h1 = h1
        self.a = a
        self.Ha4, self.Za4 = [], []
        self.Ha4_nTl, self.Za4_nTl, = [], []

    def gamma_stock(self):
        for i in range(0, len(self.X)):
            self.Ha4.append(self.M*(self.X[i]/math.sqrt(math.pow((self.h*self.h+self.X[i]*self.X[i]),3))-(self.X[i]-self.a))/math.sqrt(math.pow((self.h*self.h+math.pow((self.X[i]-self.a),2),3))))
            self.Za4.append(self.M*(self.h/math.sqrt(math.pow((self.h*self.h+self.X[i]*self.X[i]),3))-self.h1)/math.sqrt(math.pow((self.h1*self.h1+math.pow((self.X[i]-self.a),2),3))))

    def nTl_stock(self):
        for i in range(0, len(self.Ha4)):
            self.Ha4_nTl.append(self.Ha4[i] * math.pow(10, 5))
            self.Za4_nTl.append(self.Za4[i] * math.pow(10, 5))

    def get_stock(self):
        table_stock = pd.DataFrame({'Ha,gamma': self.Ha4,
                                    'Za, gamma': self.Za4,
                                    'Ha, nTl': self.Ha4_nTl,
                                    'Za, nTl': self.Za4_nTl}, index=self.X)
        print table_stock

class Stock_deep(Simple_figures):
    def __init__(self, h, r, J):
        Simple_figures.__init__(self, h)
        self.M = 4 * math.pi / 3 * math.pow(r, 3) * J
        self.Ha5, self.Za5 = [], []
        self.Ha5_nTl, self.Za5_nTl, = [], []

    def gamma_deep_stock(self):
        for i in range(0, len(self.X)):
            self.Ha5.append(self.M*self.X[i]/math.sqrt(math.pow((self.h*self.h+self.X[i]*self.X[i]),3)))
            self.Za5.append(self.M*self.h/math.sqrt(math.pow((self.h*self.h+self.X[i]*self.X[i]),3)))

    def nTl_deep_stock(self):
        for i in range(0, len(self.Ha5)):
            self.Ha5_nTl.append(self.Ha5[i] * math.pow(10, 5))
            self.Za5_nTl.append(self.Za5[i] * math.pow(10, 5))

    def get_deep_stock(self):
        deep_stock = pd.DataFrame({'Ha,gamma': self.Ha5,
                                    'Za, gamma': self.Za5,
                                    'Ha, nTl': self.Ha5_nTl,
                                    'Za, nTl': self.Za5_nTl}, index=self.X)
        print deep_stock

#test = Sphere(50, 0.21, 40)
#test.gamma_sphere()
#test.nTl_sphere()
#test.get_sphere_output()
#test.visualize_sphere()

test2 = Stock_deep(50,40,0.21)
test2.gamma_deep_stock()
test2.nTl_deep_stock()
test2.get_deep_stock()
