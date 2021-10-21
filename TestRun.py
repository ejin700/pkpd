#from solution import Solution
from pkmodel_EmFaGeHoJe.solution import Solution

PKmodel = Solution()


# Implement the model


# Initialize the parameters


model1_args = {
    'name': 'model1',
    'Q_p': [1.0, 2.0],
    'V_c': 1.0,
    'V_p': [1.0, 3.0],
    'CL': 1.0,
    'X': 1.0,
    'N': 2, #Note that N is the number of peripheral compartments, has to be an integer
    'dosing' : 'injection'
}

model2_args = {
    'name': 'model2',
    'Q_p': [2.0],
    'V_c': 1.0,
    'V_p': [1.0],
    'CL': 1.0,
    'X': 1.0,
    'N': 1,
    'dosing' : 'injection'
}

PKmodel.solve_and_plot_ODE([model1_args, model2_args], model='IV')

model3_args = {
    'name': 'model1',
    'Q_p': [1.0, 2.5, 3.5],
    'V_c': 1.0,
    'V_p': [1.0, 2.4, 1.0],
    'CL': 1.0,
    'X': 1.0,
    'k_a': 5.0,
    'N' : 3,
    'dosing' : 'injection'
}

#PKmodel.solve_and_plot_ODE([model3_args], model='sub')
