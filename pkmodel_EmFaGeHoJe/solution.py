#
# Solution class
#
from model import Model
#from pkmodel_EmFaGeHoJe.model import Model

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
        self.y0 = np.array([0.0, 0.0])
    
    def solveODE(self, parameters):
        self.fig = plt.figure()
        self.parameters = parameters
        self.Model = Model()

        for parameter in parameters:
            args = [
                parameter['Q_p1'], parameter['V_c'], parameter['V_p1'], parameter['CL'], parameter['X']
            ]
            sol = scipy.integrate.solve_ivp(
                fun=lambda t, y: self.Model.get_rhs_IV(t, y, *args),
                t_span=[self.t_eval[0], self.t_eval[-1]],
                y0=self.y0, t_eval=self.t_eval
            )
            plt.plot(sol.t, sol.y[0, :], label=parameter['name'] + '- q_c')
            plt.plot(sol.t, sol.y[1, :], label=parameter['name'] + '- q_p1')

        plt.legend()
        plt.ylabel('drug mass [ng]')
        plt.xlabel('time [h]')
        plt.show()