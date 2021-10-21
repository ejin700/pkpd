#
# Model class
#

class Model:
    """A Pharmokinetic (PK) model

    Parameters: 
    'name': name of the model,
    :param Q_p1: float, the transition rate constant between the central compartment and 
    the first peripheral compartment, [mL/h]
    :param V_c: float, the volume of the central compartment, [mL]
    :param V_p1: float, the volume of the first peripheral compartment, [mL]
    :param CL: float, the clearance/elimination rate from the central compartment, [mL/h]
    :param dose: the dose function,
    ----------

    value: numeric, optional
    'Q_p1': numeric,
    'V_c': numeric,
    'V_p1': numeric,
    'CL': numeric,
    'dose': function,

    """
    def __init__(self):
        pass
        

    def dose_constant(self, t, X):
        """
        Calculate the instantaneous dose for a given time (t) and input dose (X)
        under a constant dosing function, like an intravenous injection (IV).

        :param t: float, current time, [h]
        :param X: float, input dose, [ng]

        :returns: float, instantaneous dose, [ng/h]
        """

        # Each 1000th of an hour, X [ng] are applied, so 1000 * X [ng] are applied
        return X


    def dose_injection(self, t, X):

        """
        Calculate the instantaneous dose for a given time (t) and input dose (X)
        under a piecewise dosing function (injection).

        :param t: float, current time, [h]
        :param X: float, input dose, [ng]

        :returns: float, instantaneous dose, [ng/h]
        """

        # Here, we also want 1000 * X [ng] to be applied, so we multiply the 
        # instantaneous dose by 100, so that the total dose is 10 * 100 * X,
        # the same as in dose_constant
        if t < 10:
            return X * 100
        else:
            return 0

    def get_rhs_IV(self,t, y, Q_p, V_c, V_p, CL, X, N):
        """

        Calculate the right hand side (rhs) for the differential equations of the
        intravenous bolus dosing protocol with linear linear clearance from the central
        compartment.

        :param t: float, current time, [h]
        :param y: list, initial quantities of the drug in the peripheral and central
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

        N is the number of peripheral compartments
        Q_p is a list with len N such that each entry is the transition rate between the central and the i-th peripheral compartment
        V_P is a list with len N such that each entry is the volume of the i-th peripheral compartment
        Both y, list_of_q and list_of_rhs have length N+1 since they include both central and peripheral compartmetns



        """

        # We set the inital quantities of the drug in the central and peripheral compartments
        # equal, this is the steady state, a natural choice for y is [0, 0] (no drug present)
        list_of_q = y
        list_of_rhs = [None] * (N+1)
        list_of_rhs[0] = self.dose(t, X) - list_of_q[0] / V_c * CL
        for i in range(1,N+1):
            list_of_rhs[i] = Q_p[i-1] * (list_of_q[0] / V_c - list_of_q[i] / V_p[i-1]) 
            list_of_rhs[0] = list_of_rhs[0]-list_of_rhs[i]
        return list_of_rhs


    def get_rhs_sub(self, t, y, Q_p, V_c, V_p, CL, X, k_a, N):
        list_of_q = y
        list_of_rhs = [None] * (N+2)
        list_of_rhs[0] = self.dose(t,X) - k_a * list_of_q[0]
        list_of_rhs[1] = k_a * list_of_q[0] - list_of_q[1] / V_c * CL
        for i in range(2,N+2):
            list_of_rhs[i] = Q_p[i-2] * (list_of_q[1] / V_c - list_of_q[i] / V_p[i-2])
            list_of_rhs[1] = list_of_rhs[1] - list_of_rhs[i]
        return list_of_rhs


