#from solution import Solution
from pkmodel_EmFaGeHoJe.solution import Solution

PKmodel = Solution()


# Implement the model


# Initialize the parameters


model1_args = {
    'name': 'model1',
    'Q_p': [1.0, 2.0],
    """
    here even with 1 peripheral compartment, we also have to put the Q_P value 
    in a list instead of a float, but do we need to consider the case where we 
    have no peripheral compartments? And similar for V_p below
    """
    'V_c': 1.0,
    'V_p': [1.0, 3.0],
    'CL': 1.0,
    'X': 1.0,
    'N': 2,  # N is the number of peripheral compartments, and must be an integer
}

model2_args = {
    'name': 'model2',
    'Q_p': [2.0],
    'V_c': 1.0,
    'V_p': [1.0],
    'CL': 1.0,
    'X': 1.0,
    'N': 1,
}

#PKmodel.solveODE([model1_args, model2_args], model='IV')

model3_args = {
    'name': 'model1',
    'Q_p': [1.0, 2.5, 3.5],
    'V_c': 1.0,
    'V_p': [1.0, 2.4, 1.0],
    'CL': 1.0,
    'X': 1.0,
    'k_a': 5.0,
    'N' : 3
}

PKmodel.solve_and_plot_ODE([model3_args], model='sub')
