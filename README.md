# Non-Canonical Two Particle Hamiltonian Monte Carlo(NCTP-HMC)
Python implementatin of NCTP-HMC

# Installation
You need to set Python environment, 'pip' or 'anaconda'
## Anaconda (in anaconda prompt)
```bash
(base) ~$ git clone git@github.com:kim-hyunsu/nctp-hmc.git
(base) ~$ cd nctp-hmc
(base) ~$ conda install --yes --file requirements.txt
```
## Virtual environment
```bash
~$ git clone git@github.com:kim-hyunsu/nctp-hmc.git
~$ cd nctp-hmc
~/nctp-hmc$ sudo python3 -m pip install virtualenv
~/nctp-hmc$ virtualenv .venv
~/nctp-hmc$ . .venv/bin/activate
(.venv) ~/nctp-hmc$ python3 -m pip3 -r requirements.txt
```
## **You can use any environment that can run tensorflow and numpy

# File Structure
```
docs/             # Report to explain NCTP-HMC  
experiments/
| example.py      # Experiment example.
hmc/              # Implementation of HMC
| __init__.py
mhmc/             # Implementation of MHMC
| __init__.py     
nctphmc/          # Implemenataion of NCTP-HMC
| __init__.py
requirements.txt  # List of dependent modules
run.py            # Run specific experiment
```

# Add an experiment
1. Add a Python file into 'experiments' directory (e.g. experiments/2d_gaussian.py)
1. Write codes including 'main' function (test.py runs the 'main' function)
1. Run command below
```bash
~/nctp-hmc$ python3 run.py 2d_gaussian
```
