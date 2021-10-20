#
# Solution class
#
from model import Model

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
        self.fig = plt.figure()
        self.parameters = parameters
    
    def solveODE(parameters, func):
        self.fig = plt.figure()
        self.parameters = parameters

        for parameter in parameters:
            args = [
                parameter['Q_p1'], parameter['V_c'], parameter['V_p1'], parameter['CL'], parameter['X']
            ]
            sol = scipy.integrate.solve_ivp(
                fun=lambda t, y: Model.func(t, y, *args),
                t_span=[t_eval[0], t_eval[-1]],
                y0=y0, t_eval=t_eval
            )
            plt.plot(sol.t, sol.y[0, :], label=model['name'] + '- q_c')
            plt.plot(sol.t, sol.y[1, :], label=model['name'] + '- q_p1')

        plt.legend()
        plt.ylabel('drug mass [ng]')
        plt.xlabel('time [h]')
        plt.show()