import matplotlib.pylab as plt
import numpy as np
import scipy.integrate



# This prototype implements the pharmokinetic (PK) model of the intravenous bolus 
# dosing protocol.
# The equations  can be found in the following module:
# https://sabs-r3.github.io/software-engineering-projects/01-introduction/index.html






### Define the model ####

def dose(t, X):
    """
    Calculate the instantaneous dose for a given time (t) and input dose (X).

    :param t: float, current time, [h]
    :param X: float, input dose, [ng]

    :returns: float, instantaneous dose, [ng/h]
    """

    # The instantaneous dose is constant over time, analogous to an intravenous 
    # injection (IV)
    return X


def rhs(t, y, Q_p1, V_c, V_p1, CL, X):
    """
    Calculate the right hand side (rhs) for the differential equations of the
    intravenous bolus dosing protocol with linear linear clearance from the central
    compartment.

    :param y: float, initial


    :param t: float, current time, [h]
    :param y: list, initial quantities of the drug in the peripheral and and central
    compartments, [ng, ng]
    :param Q_p1: float, the transition rate constant between the central compartment and 
    the first peripheral compartment, [mL/h]
    :param V_c: float, the volume of the central compartment, [mL]
    :param V_p1: float, the volume of the first peripheral compartment, [mL]
    :param CL: float, the clearance/elimination rate from the central compartment, [mL/h]
    :param X: float, input dose, [ng]

    :returns: list, first entry (float) is the rate of change of the quantity of the drug 
    in the central compartment with respect to (wrt) time [ng/h]. Likewise, the second 
    entry (float) is the rate of change wrt time of the quantity of the drug in the first 
    peripheral compartment [ng/h]

    """
    # We set the inital quantities of the drug in the central and peripheral compartments
    # equal, this is the steady state, a natural choice for y is [0, 0] (no drug present)
    q_c, q_p1 = y


    # dqp1_dt is the rate of transition from the central compartment into the peripheral 
    # compartment, (which has rate constant Q_p1). Note that if the concentration of the 
    # drug in the central compartment (q_c / V_c) is greater than that of the peripheral 
    # compartment, the transition rate is positive (into the peripheral component). It is 
    # clear that the transition rate is proportional to the difference in concentrations 
    # between the central and peripheral compartments. 
    dqp1_dt = Q_p1 * (q_c / V_c - q_p1 / V_p1)


    # dqc_dt is the net rate of transition into the central compartment. 
    dqc_dt = dose(t, X) - q_c / V_c * CL - dqp1_dt

    return [dqc_dt, dqp1_dt]






### Implement the model ####


## Initialize the parameters ##

# Create two 'models', the only difference is that the rate constant Q_p1 in model
# two is twice that of model one. 

# Set the parameters for the first 'model'


model1_args = {
    'name': 'model1',
    'Q_p1': 1.0,
    'V_c': 1.0,
    'V_p1': 1.0,
    'CL': 1.0,
    'X': 1.0,
}

# Set the parameters for the second 'model'
model2_args = {
    'name': 'model2',
    'Q_p1': 2.0,
    'V_c': 1.0,
    'V_p1': 1.0,
    'CL': 1.0,
    'X': 1.0,
}

# Set the times evaluated to be 1000 points equally spaced between 
# 0 and 1 hours (inclusive)
t_eval = np.linspace(0, 1, 1000)

# Set the initial amounts of the drug in the central and first peripheral compartments, 
# respectively, to both 0
y0 = np.array([0.0, 0.0])




## Plot the model with the initializations above ##



# Create a figure to show the quantity of the drug in the central and first peripheral
# compartments over time.
fig = plt.figure()

# Solve and plot each model
for model in [model1_args, model2_args]:
    
    # Create a list of the arguments to the rhs function
    args = [
        model['Q_p1'], model['V_c'], model['V_p1'], model['CL'], model['X']
    ]

    # Solve for q_c and q_p1
    sol = scipy.integrate.solve_ivp(
        fun=lambda t, y: rhs(t, y, *args),
        t_span=[t_eval[0], t_eval[-1]],
        y0=y0, t_eval=t_eval
    )

    # Plot the results for themodel
    plt.plot(sol.t, sol.y[0, :], label=model['name'] + '- q_c')
    plt.plot(sol.t, sol.y[1, :], label=model['name'] + '- q_p1')

plt.legend()
plt.ylabel('drug mass [ng]')
plt.xlabel('time [h]')
plt.show()
