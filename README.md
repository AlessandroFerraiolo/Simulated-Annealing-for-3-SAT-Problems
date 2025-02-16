# Simulated Annealing for 3-SAT Problems

## Overview
This project implements a **Simulated Annealing (SA) algorithm** to solve random **3-SAT problems**. The objective is to study the performance of SA in finding satisfiable assignments for randomly generated 3-SAT instances and analyze the impact of key parameters on the algorithm's effectiveness.

## Project Structure
The project consists of the following files:

### Python Scripts:
- **`KSAT.py`**: Defines the **K-SAT problem** class, including instance generation, cost function computation, and Monte Carlo moves.
- **`SimAnn.py`**: Implements the **Simulated Annealing algorithm**, defining the acceptance probability based on the **Metropolis rule** and executing the annealing schedule.
- **`KSAT_properties.py`**: Contains a function to compute the **empirical probability** of solving a K-SAT problem using Simulated Annealing.
- **`KSATrun.py`**: A script to run the **3-SAT solver** with specific parameters and configurations.

### Report:
- **`Report_Alessandro_Ferraiolo.pdf`**: Contains the analysis of SA performance for solving **3-SAT instances**, parameter tuning insights, empirical probability analysis, and solver efficiency comparisons.
- **`Report (Jupyter Notebook).ipynb`**: A Jupyter Notebook version of the report with code execution and visualizations.

## How It Works
1. **Problem Generation:**
   - The `KSAT` class generates a **random 3-SAT instance** with `N` variables and `M` clauses.
   - Each clause consists of **K=3 literals**, randomly assigned with a positive or negative sign.

2. **Simulated Annealing Execution:**
   - The `simann` function in `SimAnn.py` performs **simulated annealing** with the following steps:
     - Initialize a random configuration.
     - Perform **Monte Carlo moves**, flipping variable assignments to minimize cost.
     - Accept or reject moves based on **Metropolis acceptance probability**.
     - Reduce temperature over `anneal_steps` until convergence.

3. **Empirical Probability Calculation:**
   - `empirical_probability` in `KSAT_properties.py` computes the **probability of solving** a 3-SAT instance for different values of `M`.

4. **Performance Analysis:**
   - The **Jupyter Notebook and PDF report** analyze key parameters:
     - Monte Carlo steps (`mcmc_steps`)
     - Annealing steps (`anneal_steps`)
     - Temperature range (`β0` to `β1`)
     - Algorithmic threshold (`M(alg)`) where success probability reaches 50%

### Configurable Parameters:
- `N`: Number of variables (default = 200)
- `M`: Number of clauses (default = 200)
- `mcmc_steps`: Monte Carlo moves per annealing step
- `anneal_steps`: Number of annealing steps
- `beta0`: Initial inverse temperature
- `beta1`: Final inverse temperature
- `seed`: Random seed for reproducibility


## Results & Insights
- **Success Probability Trends:** The probability of solving a problem (`P(N,M)`) depends on the solver accuracy.
- **Algorithmic Threshold:** The ratio `M/N` determines problem complexity, with a threshold converging to `4.27`.
- **Solver Power Influence:** Stronger solvers achieve a higher `M(alg)`, improving solution rates.

## References
1. Mézard, Mertens, and Zecchina (2003). "Threshold Values of Random K-SAT from the Cavity Method." arXiv preprint: [arXiv:cs/0309020](https://arxiv.org/abs/cs/0309020)

---
**Author:** Alessandro Ferraiolo  
**Course:** 30509 Computer Programming Assignment 2024 - Bocconi University

