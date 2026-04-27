import numpy as np
import pandas as pd
import time

print("Welcome to this deductible calculator! This is to provide an estimate based on changing accident numbers.")

print()
print("We start with the initial year.")

policyholders = int(input("How many policyholders do you have? "))
accident_pct = float(input("What is the expected number of accidents per policyholder per year? "))
accident_cost = float(input("What is the expected cost of an accident? "))
years = int(input("How many years would you like the program to run? " ))

lam = policyholders * accident_pct

def simulate_year():
    accidents = np.random.poisson(lam)
    if accidents == 0:
        return{
            "Accidents": 0.0,
            "Sum": 0.0,
            "Average": 0.0,
            "95th Pctle": 0.0,
            "99th Pctle": 0.0
        }
    acc_list = np.random.exponential(accident_cost, size=accidents)
    return {
        "Accidents": len(acc_list), 
        "Sum": acc_list.sum(), 
        "Average": acc_list.mean(), 
        "95th Pctle": np.quantile(acc_list, 0.95),
        "99th Pctle": np.quantile(acc_list, 0.99)
}

def run_sim():
    results = [simulate_year() for _ in range(years)]
    df_2 = pd.DataFrame(results)
    return df_2

print("First, we run with no deductible.")
no_ded = run_sim()
table = no_ded.describe()
print(table.round(2))

print()
print("Now, let's change the conditions. Let's say the frequency/severity of the accidents changes.")
print()
accident_pct_2 = float(input(f"What is the expected number of accidents per policyholder in the new year? (Previous input: {accident_pct:.2f}) "))
accident_cost_2 = float(input(f"What is the expected cost of an accident in the new year? (Previous input: {accident_cost:.2f}) "))
lam_2 = policyholders * accident_pct_2




def ded_sim(ded):
    accidents = np.random.poisson(lam_2)
    if accidents == 0:
        return{
            "Accidents": 0.0,
            "Sum": 0.0,
            "Average": 0.0,
            "95th Pctle": 0.0,
            "99th Pctle": 0.0
        }
    acc_list = np.random.exponential(accident_cost_2, size=accidents)
    acc_list = np.maximum(acc_list - ded, 0)
    return {
        "Accidents": len(acc_list), 
         "Sum": acc_list.sum(), 
         "Average": acc_list.mean(), 
         "95th Pctle": np.quantile(acc_list,0.95),
         "99th Pctle": np.quantile(acc_list,0.99)
    }

def run_ded_sim(ded):
    results = [ded_sim(ded) for _ in range(years)]
    df = pd.DataFrame(results)
    return df

    
while True:
    ded = float(input("What is the deductible you'd like to analyze? (Type -1 to quit) "))
    if ded == -1: 
        break
    print(f"\nRunning with deductible ${ded:.2f}.")
    ded_df = run_ded_sim(ded)
    print(ded_df.describe().round(2))
    print("\n")
    if no_ded['Sum'].mean() > ded_df['Sum'].mean():
        print(f"On average, this deductible makes ${no_ded['Sum'].mean() - ded_df['Sum'].mean():.2f} per year for the company over last year.")
    else: 
        print(f"On average, this deductible loses ${ded_df['Sum'].mean() - no_ded['Sum'].mean():.2f} per year for the company over last year.")
    print("\n")
    new_df = pd.DataFrame()
    new_df['Deductible Analysis'] = no_ded['Sum'] - ded_df['Sum']
    new_df['Profit'] = no_ded['Sum'] - ded_df['Sum'] > 0
    print(new_df['Deductible Analysis'].describe().round(2))
    print(f"{new_df['Profit'].sum()/new_df['Profit'].count()*100:.2f}% of all scenarios result in a net profit.")
