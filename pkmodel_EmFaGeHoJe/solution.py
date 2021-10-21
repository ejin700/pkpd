#
# Solution class
#
#from model import Model
from pkmodel_EmFaGeHoJe.model import Model

import matplotlib.pylab as plt
import numpy as np
import scipy.integrate

class Solution:
    """A Pharmokinetic (PK) model solution

    Parameters
    ----------

    parameters: list of dictionaries
        Specifies parameters for solving the ODE. Format:
        model1_args = {
            'name': 'model1',
            'Q_p1': 1.0,
            'V_c': 1.0,
            'V_p1': 1.0,
            'CL': 1.0,
            'X': 1.0,
            }

    Methods
    -------

    solveODE
    """
    def __init__(self):
        self.t_eval = np.linspace(0, 1, 1000)
        
    
    def solveODE(self, parameters, model='IV'):
        self.fig = plt.figure()
        self.parameters = parameters
        self.Model = Model()

        if model == 'IV':
            for parameter in parameters:
                args = [
                    parameter['Q_p'], parameter['V_c'], parameter['V_p'], parameter['CL'], parameter['X'], parameter['N']
                ]
                self.y0 = np.zeros(parameter['N']+1)
                sol = scipy.integrate.solve_ivp(
                    fun=lambda t, y: self.Model.get_rhs_IV(t, y, *args),
                    t_span=[self.t_eval[0], self.t_eval[-1]],
                    y0=self.y0, t_eval=self.t_eval
                )
                plt.plot(sol.t, sol.y[0, :], label=parameter['name'] + '- q_c')
                for i in range(1,parameter['N']+1):
                    plt.plot(sol.t, sol.y[i, :], label=parameter['name'] + f'- q_p{i}')

                
                

        elif model == 'sub':
            
            for parameter in parameters:
                args = [
                    parameter['Q_p'], parameter['V_c'], parameter['V_p'], parameter['CL'], parameter['X'], parameter['k_a'],
                    parameter['N'],
                ]
                self.y0 = np.zeros(parameter['N']+2)
                sol = scipy.integrate.solve_ivp(
                    fun=lambda t, y: self.Model.get_rhs_sub(t, y, *args),
                    t_span=[self.t_eval[0], self.t_eval[-1]],
                    y0=self.y0, t_eval=self.t_eval
                )
                plt.plot(sol.t, sol.y[0, :], label=parameter['name'] + '- q0')
                plt.plot(sol.t, sol.y[1, :], label=parameter['name'] + '- q_c')
                for i in range(1, parameter['N']+1):
                    plt.plot(sol.t, sol.y[i+1, :], label=parameter['name'] + f'- q_p{i}')
        
        else:
            raise ValueError("the two possible models are 'IV' and 'sub")

        plt.legend()
        plt.ylabel('drug mass [ng]')
        plt.xlabel('time [h]')
        plt.show()