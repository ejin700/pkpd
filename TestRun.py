#from solution import Solution
from pkmodel_EmFaGeHoJe.solution import Solution

PKmodel = Solution()

model1_args = {
    'name': 'model1',
    'Q_p': [1.0,2.0],
    """
    here even with 1 peripheral compartment, we also have to put the Q_P value in a list instead of a float, but do we need to consider 
    the case where we have no peripheral compartments?
    And similar for V_p below
    """
    'V_c': 1.0,
    'V_p': [1.0,3.0],
    'CL': 1.0,
    'X': 1.0,
    'N': 2, #Note that N is the number of peripheral compartments, has to be an integer
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

PKmodel.solveODE([model1_args, model2_args], model='IV')

model3_args = {
    'name': 'model1',
    'Q_p1': 1.0,
    'V_c': 1.0,
    'V_p1': 1.0,
    'CL': 1.0,
    'X': 1.0,
    'k_a': 1.0,
}

#PKmodel.solveODE([model3_args], model='sub')