import SimAnn
import KSAT

def empirical_probability(M, N=200, iterations=100, mcmc_steps=200, anneal_steps=20, beta0=1, beta1=10, seed=None):
    # Create a K-SAT problem instance with N variables, M clauses, and K=3 (3-SAT).
    ksat = KSAT.KSAT(N=N, M=M, K=3, seed=seed)
    # Initialize a counter to track the number of iterations where a solution is found.
    n_solved = 0
    # Perform the Simulated Annealing algorithm over the specified number of iterations.
    for i in range(iterations):

        best_c = SimAnn.simann(ksat,
                               mcmc_steps=mcmc_steps,           # Number of MCMC steps in each annealing step.
                               anneal_steps=anneal_steps,       # Number of annealing steps.
                               beta0=beta0,                     # Initial inverse temperature (beta).
                               beta1=beta1,                     # Final inverse temperature (beta).
                               seed=seed,                       # No seed specified for randomness( set None in the outer function).
                               debug_delta_cost=False,
                               optimize = True) 
        # If the cost of the best solution found is 0 (all clauses satisfied), increment the counter.
        if best_c == 0:
            n_solved += 1
    # Return the fraction of successful iterations, representing the empirical probability of solving the K-SAT problem.
    return n_solved / iterations

