# Deductible Simulation Model

## About
This project simulates insurance claim costs using a Monte Carlo framework. 
Claim frequency is modeled with a Poisson distribution, and claim severity with an exponential distribution.

The model compares total losses with and without deductibles, and allows users to explore how changes in frequency and severity impact profitability.

To see a sample output, click [here](sample-output.png).

## Example Output

### Baseline Scenario
First, we run with no deductible.
Assume there are 100 policyholders, each with risk of accident modeled by a Poisson distribution with mean 0.14. 
Each accident's severity is modeled by an exponential distribution with mean 1500.
1000 years' worth of simulations produced the following data.

| Metric   | Accidents | Sum       | Average  | 95th Pctle | 99th Pctle |
|----------|----------:|----------:|---------:|-----------:|-----------:|
| Mean     | 14.16     | 21,151.27 | 1,499.12 | 3,852.49   | 4,650.06   |
| Std Dev  | 3.86      | 7,918.54  | 432.66   | 1,291.14   | 1,757.47   |
| Min      | 4.00      | 1,610.01  | 400.01   | 785.63     | 790.17     |
| 25th %   | 11.00     | 15,587.49 | 1,200.46 | 2,924.62   | 3,358.39   |
| Median   | 14.00     | 20,509.17 | 1,454.48 | 3,681.03   | 4,364.80   |
| 75th %   | 17.00     | 26,383.64 | 1,758.24 | 4,525.18   | 5,617.98   |
| Max      | 28.00     | 56,752.57 | 3,783.50 | 11,774.12  | 14,260.59  |

### Deductible Introduction

We now introduce a deductible of $20.00, keeping all other variables constant, and we get the following output.

| Metric        | Accidents | Sum      | Average | 95th Pctle | 99th Pctle |
|--------------|----------:|---------:|--------:|-----------:|-----------:|
| Mean         | 14.16     | 20,962.78 | 1,477.90 | 3,823.67   | 4,628.39   |
| Std Dev      | 3.90      | 8,221.48  | 422.56   | 1,265.78   | 1,831.50   |
| Min          | 4.00      | 2,617.20  | 436.20   | 628.47     | 636.50     |
| 25th %       | 11.00     | 15,002.54 | 1,174.99 | 2,934.13   | 3,301.31   |
| Median       | 14.00     | 20,202.08 | 1,445.63 | 3,662.90   | 4,319.91   |
| 75th %       | 17.00     | 26,086.94 | 1,737.21 | 4,559.85   | 5,589.50   |
| Max          | 26.00     | 56,822.53 | 3,333.57 | 8,722.98   | 14,894.50  |

### Analysis

Note: The probability of profit is calculated using two separate simulations.
Therefore, the probability is indicative of the distribution, rather than on a case-by-case basis.

| Metric        | Profit   | 
|--------------|----------:|
| Mean         | 256.91     |
| Std Dev      | 11,339.14      | 
| Min          | -37,078.36      | 
| 25th %       | -6,928.70     | 
| Median       | 484.16     | 
| 75th %       | 7,339.02     | 
| Max          | 35,526.08     | 

The probability of the company making more money next year after adding a $20 deductible is calculated to be 50.50%. The chances barely improved (from coin flip odds of 50%) due to the 
small size of the deductible (about 1.3% of the mean claim size).

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
- Probability of profit (percentage of simulations where adding the deductible yields a more favorable outcome for the company)

## Interpretation

- A higher deductible reduces insurer payouts but may increase variability.
- The model helps quantify trade-offs between expected savings and risk.

## How to Run

- Open and run the notebook:
[deductible_simulator.ipynb](deductible_simulator.ipynb)
- Or, you can open in Python, and you can use the script to do full simulation runs:
[deductible_simulation.py](deductible_simulation.py)
