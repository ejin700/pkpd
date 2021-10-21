import unittest
import pkmodel_EmFaGeHoJe.solution as pks


class SolutionTest(unittest.TestCase):
    """
    Tests the :class:`Solution` class.
    """
    def test_model_type(self):
        """
        Test if a different argument than 'IV' or 'sub' is passed to the solve_and_plot_ODE method it raises a value error.
        """
        model1_args = {
            'name': 'model2',
            'Q_p': [2.0],
            'V_c': 1.0,
            'V_p': [1.0],
            'CL': 1.0,
            'X': 1.0,
            'N': 1,
            'dosing': 'injection'
        }

        PKmodel = pks.Solution()
        with self.assertRaises(ValueError):
            PKmodel.solve_and_plot_ODE([model1_args], model='abc')

    def test_input_arguments1(self):
        """
        Test that specifying 3 compartments leads to the correct size of the solution.
        """
        model2_args = {
            'name': 'model1',
            'Q_p': [1.0, 2.5, 3.5],
            'V_c': 1.0,
            'V_p': [1.0, 2.4, 1.0],
            'CL': 1.0,
            'X': 1.0,
            'k_a': 5.0,
            'N': 3,
            'dosing': 'injection'
        }

        PKmodel = pks.Solution()
        PKmodel.solve_and_plot_ODE([model2_args], model='IV')

        assert(len(PKmodel.y0) == 4)

    def test_input_arguments2(self):
        """
        Test that specifying 3 compartments leads to the correct size of the solution.
        """
        model3_args = {
            'name': 'model1',
            'Q_p': [1.0, 2.5, 3.5],
            'V_c': 1.0,
            'V_p': [1.0, 2.4, 1.0],
            'CL': 1.0,
            'X': 1.0,
            'k_a': 5.0,
            'N': 3,
            'dosing': 'injection'
        }

        PKmodel = pks.Solution()
        PKmodel.solve_and_plot_ODE([model3_args], model='sub')

        assert(len(PKmodel.y0) == 5)

    def test_input_arguments3(self):
        """
        Test if number of compartments doesn't match with the number of volumes and concentrations an IndexError is raised.
        """
        model4_args = {
            'name': 'model1',
            'Q_p': [1.0, 2.5, 3.5],
            'V_c': 1.0,
            'V_p': [1.0, 2.4, 1.0],
            'CL': 1.0,
            'X': 1.0,
            'k_a': 5.0,
            'N': 6,
            'dosing': 'injection'
        }

        PKmodel = pks.Solution()
        with self.assertRaises(IndexError):
            PKmodel.solve_and_plot_ODE([model4_args], model='IV')


if __name__ == '__main__':
    unittest.main()
