#
# Model class
#

class Model:
    """A Pharmokinetic (PK) model

    Parameters: 
    'name': name of the model,
    'Q_p1': the transition rate between central compartment and peripheral compartment,
    'V_c': the volume of the central compartment,
    'V_p1': the volume of the first peripheral compartment,
    'CL': the clearance/elimination rate from the central compartment,
    'X': the dose function,
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self, value=42):
        self.value = value

