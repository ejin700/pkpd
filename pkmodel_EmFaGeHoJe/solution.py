#
# Solution class
#
#from model import Model
from pkmodel_EmFaGeHoJe.model import Model

import matplotlib.pylab as plt
import numpy as np
import scipy.integrate


class Solution:
    """A class that solves a Pharmacokinetics model

    Methods
    -------

    solve_and_plot_ODE
        takes a set of parameters and a type of dosing and returns a plot of the pk model
    """
    def __init__(self):
        self.Model = Model()

    def solve_and_plot_ODE(self, parameters, model='IV'):
        '''
        Solves ODE and plots pk model.

        :param parameters: list of dictionaries
            a set of parameters for an individual model is formated in a dictionary:
            model1_args = {
                'name': 'str',      #name of model
                'Q_p': [float],     #transition rate constant between the central and peripheral compartment [mL/h]
                'V_c': float,       #Volume of the central compartment [mL]
                'V_p': [float],     #Volume of peripheral compartments [mL]
                'CL': float,        #clearance rate [mL/h]
                'X': float,         #input dose, [ng]
                'N': int,           #number of compartments
                'dosing' : 'str'    #options: 'constant' or 'injection'
                }
            several sets of parameters to plot multiple models can be passed to the method inside a list.
        :param model: string, optional
            specify type of dosing, model='IV' for intravenous (default), model='sub' for subcutaneous

        :retuns: plot of the PK model
        '''
        self.parameters = parameters
        # Set the times evaluated to be 1000 points equally spaced between
        # 0 and 1 hours (inclusive)
        self.t_eval = np.linspace(0, 1, 1000, endpoint=False)
        self.fig = plt.figure()

        if model == 'IV':
            for parameter in parameters:

                # Create a list of the arguments to the rhs function
                args = [
                    parameter['Q_p'], parameter['V_c'], parameter['V_p'],
                    parameter['CL'], parameter['X'], parameter['N'], parameter['dosing']
                ]

                # Set the initial amounts of the drug in the central and first peripheral compartments,
                # respectively, to both 0
                self.y0 = np.zeros(parameter['N'] + 1)

                # Solve and plot
                sol = scipy.integrate.solve_ivp(
                    fun=lambda t, y: self.Model.get_rhs_IV(t, y, *args),
                    t_span=[self.t_eval[0], self.t_eval[-1]],
                    y0=self.y0, t_eval=self.t_eval
                )
                plt.plot(sol.t, sol.y[0, :], label=parameter['name'] + '- q_c')
                for i in range(1, parameter['N'] + 1):
                    plt.plot(sol.t, sol.y[i, :], label=parameter['name'] + f'- q_p{i}')

        elif model == 'sub':
            for parameter in parameters:
                args = [
                    parameter['Q_p'], parameter['V_c'], parameter['V_p'], parameter['CL'], parameter['X'], parameter['k_a'],
                    parameter['N'], parameter['dosing'],
                ]
                self.y0 = np.zeros(parameter['N'] + 2)
                sol = scipy.integrate.solve_ivp(
                    fun=lambda t, y: self.Model.get_rhs_sub(t, y, *args),
                    t_span=[self.t_eval[0], self.t_eval[-1]],
                    y0=self.y0, t_eval=self.t_eval
                )
                plt.plot(sol.t, sol.y[0, :], label=parameter['name'] + '- q0')
                plt.plot(sol.t, sol.y[1, :], label=parameter['name'] + '- q_c')
                for i in range(1, parameter['N'] + 1):
                    plt.plot(sol.t, sol.y[i + 1, :], label=parameter['name'] + f'- q_p{i}')

        else:
            raise ValueError("the two possible models are 'IV' and 'sub")

        plt.legend()
        plt.ylabel('drug mass [ng]')
        plt.xlabel('time [h]')
        plt.show()
