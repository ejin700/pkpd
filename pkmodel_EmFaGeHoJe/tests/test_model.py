import unittest


import pkmodel_EmFaGeHoJe.model as pkm
import numpy as np


class ModelTest(unittest.TestCase):
    """
    Tests the :class:`Model` class.
    """
    def test_dose_constant(self):
        """
        Tests Model creation.
        """

        t_eval = np.linspace(0, 1, 1000, endpoint=False)

        X = 1.0
        PKmodel = pkm.Model()

        total_dose = 0
        for t in t_eval:
            total_dose += PKmodel.dose_constant(t=t, X=X)

        self.assertEqual(total_dose, 1000 * X)


if __name__ == '__main__':
    unittest.main()


