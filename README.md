# Deductible Simulation Model

## About
This project simulates insurance claim costs using a Monte Carlo framework. 
Claim frequency is modeled with a Poisson distribution, and claim severity with an exponential distribution.

The model compares total losses with and without deductibles, and allows users to explore how changes in frequency and severity impact profitability.

## Features
- Adjustable frequency and severity
- Scalable Monte Carlo, actuarial-style simulation
- Deductible impact analysis and profit margin estimation

## Motivation
- Insurance companies must balance profitability with changing frequency and severity on a year-to-year basis. 
Deductibles play a key role in shifting risk between insurer and policyholder.

This model explores how different deductible levels impact:
- Total claim payouts
- Loss distributions
- Probability of profitability (percentage of simulations where adding the deductible yields a more favorable outcome for the company)

## How to Run

- Open and run the notebook:
[deductible_simulator.ipynb](deductible_simulator.ipynb)
- Or, you can open in Python, and you can use the script to do full simulation runs:
[deductible_simulation.py](deductible_simulation.py)
