#
# Model class
#

class Model:
    """A Pharmokinetic (PK) model

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
        if t < 0.01:
            return X * 100
        else:
            return 0

    def get_rhs_IV(self, t, y, Q_p, V_c, V_p, CL, X, N, dosing):
        """

        Calculate the right hand side (rhs) for the differential equations of the
        intravenous bolus dosing protocol with linear linear clearance from the central
        compartment.

        :param t: float, current time, [h]
        :param y: list, initial quantities of the drug in the peripheral and central
        compartments, [ng, ng]
        :param Q_p: list, each entry(float) is the transition rate constant between the central
        compartment and the peripheral compartments, [mL/h]
        :param V_c: float, the volume of the central compartment, [mL]
        :param V_p: list, each entry(float) is the the volume of the peripheral compartments, [mL]
        :param CL: float, the clearance/elimination rate from the central compartment, [mL/h]
        :param X: float, input dose, [ng],
        :param N: int, the number of peripheral compartments,
        :param dosing: string, indicating if the dosing protocal is "constant" or "injection"

        :returns: list, first entry (float) is the rate of change of the quantity of the drug
        in the central compartment with respect to (wrt) time [ng/h]. Likewise, the rest of the
        entries (float) are the rates of change wrt time of the quantity of the drug in the
        peripheral compartments [ng/h]
        """

        # We set the inital quantities of the drug in the central and peripheral compartments
        # equal, this is the steady state, a natural choice for y is [0, 0] (no drug present)
        if type(Q_p) is not list or type(V_p) is not list:
            raise TypeError("The type of Q_p and V_p should be a list")
        if type(N) is not int:
            raise TypeError("The type of N should be int")
        if N != len(Q_p) or N != len(V_p):
            raise IndexError("The length of Q_p and V_p should be equal to N")
        if dosing == "constant":
            dose = self.dose_constant
        elif dosing == "injection":
            dose = self.dose_injection
        else:
            raise ValueError("the two possible dosing protocals are 'constant' and 'injection'")

        list_of_q = y
        list_of_rhs = [None] * (N + 1)
        list_of_rhs[0] = dose(t, X) - list_of_q[0] / V_c * CL
        for i in range(1, N + 1):
            list_of_rhs[i] = Q_p[i - 1] * (list_of_q[0] / V_c - list_of_q[i] / V_p[i - 1])
            list_of_rhs[0] = list_of_rhs[0] - list_of_rhs[i]
        return list_of_rhs

    def get_rhs_sub(self, t, y, Q_p, V_c, V_p, CL, X, k_a, N, dosing):
        """

        Calculate the right hand side (rhs) for the differential equations of the
        subcutaneous dosing protocol with linear linear clearance from the central
        compartment.

        :param t: float, current time, [h]
        :param y: list, initial quantities of the drug in the peripheral and central
        compartments, [ng, ng]
        :param Q_p: list, each entry(float) is the transition rate constant between the central
        compartment and the peripheral compartments, [mL/h]
        :param V_c: float, the volume of the central compartment, [mL]
        :param V_p: list, each entry(float) is the the volume of the peripheral compartments, [mL]
        :param CL: float, the clearance/elimination rate from the central compartment, [mL/h]
        :param X: float, input dose, [ng]
        :param k_a: float, the ???absorption??? rate for the s.c dosing[/h],
        :param N: int, the number of peripheral compartments,
        :param dosing: string, indicating if the dosing protocal is "constant" or "injection"

        :returns: list, first entry (float) is the rate of change of the quantity of the drug
        in the first compartment with respect to (wrt) time [ng/h] and second entry (float) is
        the rate of change of the quantity of the drug in the central compartment with respect
        to (wrt) time [ng/h]. Likewise, the rest of the entries (float) are the rates of change
        wrt time of the quantity of the drug in the peripheral compartments [ng/h]
        """
        if type(Q_p) is not list or type(V_p) is not list:
            raise TypeError("The type of Q_p and V_p should be a list")
        if type(N) is not int:
            raise TypeError("The type of N should be int")
        if N != len(Q_p) or N != len(V_p):
            raise IndexError("The length of Q_p and V_p should be equal to N")
        if dosing == "constant":
            dose = self.dose_constant
        elif dosing == "injection":
            dose = self.dose_injection
        else:
            raise ValueError("the two possible dosing protocals are 'constant' and 'injection'")
        list_of_q = y
        list_of_rhs = [None] * (N + 2)
        list_of_rhs[0] = dose(t, X) - k_a * list_of_q[0]
        list_of_rhs[1] = k_a * list_of_q[0] - list_of_q[1] / V_c * CL
        for i in range(2, N + 2):
            list_of_rhs[i] = Q_p[i - 2] * (list_of_q[1] / V_c - list_of_q[i] / V_p[i - 2])
            list_of_rhs[1] = list_of_rhs[1] - list_of_rhs[i]
        return list_of_rhs
