[![Run unit tests](https://github.com/ejin700/pkpd/actions/workflows/unit_tests.yml/badge.svg)](https://github.com/ejin700/pkpd/actions/workflows/unit_tests.yml)

[![Run on multiple OS](https://github.com/ejin700/pkpd/actions/workflows/os_tests.yml/badge.svg)](https://github.com/ejin700/pkpd/actions/workflows/os_tests.yml)

[![Documentation Status](https://readthedocs.org/projects/pk-project/badge/?version=latest)](https://pk-project.readthedocs.io/en/latest/?badge=latest)

[![codecov](https://codecov.io/gh/ejin700/pkpd/branch/master/graph/badge.svg?token=Y6F96TKO7W)](https://codecov.io/gh/ejin700/pkpd)

# **Software engineering project 2021**
## **Pharmacokinetic modelling**

[Link to project description](https://sabs-r3.github.io/software-engineering-projects/01-introduction/index.html)

*This repository contains a Python library that can specify, solve and visualise the solution of a PK model. The library can be downloaded and installed using pip.*

`$ pip install -i https://test.pypi.org/simple/ pkmodel_EmFaGeHoJe`

### **Features**

1. The user can specify the form of the PK model. This includes the number of peripheral compartments, the type of dosing (intravenous bolus versus subcutaneous), and the dosing protocol.
2. The user can specify the protocol independently from the model (e.g. be able to solve a one and two compartment model for the same dosing protocol)
3. The user can solve for the drug quantity in each compartment over time, given a model and a protocol
4. Visualisation of the solution of a model. The user can compare two different solutions.

### **Example of using the library**
*For an example how to use the library see TestRun.py or the code below:*

`>>> from pkmodel_EmFaGeHoJe.solution import Solution`

`>>> PKmodel = Solution()`

`>>> model1_args = {
                'name': 'str' (name of model),
                'Q_p': [float] (transition rate constant between the central and peripheral compartment [mL/h]),
                'V_c': float (Volume of the central compartment [mL]),
                'V_p': [float] (Volume of peripheral compartments [mL]),
                'CL': float (clearance rate [mL/h]),
                'X': float (input dose, [ng]),
                'N': int (number of compartments),
                'dosing' : 'str' (options: 'constant' or 'injection')
                }`

`>>> PKmodel.solve_and_plot_ODE([model1_args], model='IV')`

 
### **License**

 This project is licensed under the terms of the MIT license.





