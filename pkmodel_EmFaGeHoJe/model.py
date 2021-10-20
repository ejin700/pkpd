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
        

#    def add_parameters_IV(self, Q_p1, V_c, V_p1, CL, dose):
#        """"""
#        dict_parameter = {
#            'Q_p1' : Q_p1,
#            'V_c' : V_c,
#            'V_p1' : V_p1,
#            'CL' : CL,
#            'dose' : dose
#        }
#        self.param = dict_parameter
#        return dict_parameter
    def dose(self, t, X):
        """
        Calculate the instantaneous dose for a given time (t) and input dose (X).

        :param t: float, time [h]
        :param X: float, input dose [ng]
        :returns: float, instantaneous dose [ng]
        """
        return X

    def get_rhs_IV(self,t, y, Q_p1, V_c, V_p1, CL, X):
        """
        :returns: list, first entry (float) is the rate of change of the quantity of the drug 
        in the central compartment with respect to (wrt) time [ng/h]. Likewise, the second 
        entry (float) is the rate of change wrt time of the quantity of the drug in the first 
        peripheral compartment [ng/h]
        """
        q_c, q_p1 = y
        transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
        dqc_dt = self.dose(t, X) - q_c / V_c * CL - transition
        dqp1_dt = transition
        return [dqc_dt, dqp1_dt]



