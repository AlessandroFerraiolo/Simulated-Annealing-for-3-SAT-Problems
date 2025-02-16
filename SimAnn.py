import numpy as np

## Stochastically determine whether to acccept a move according to the
## Metropolis rule (valid for symmetric proposals)
def accept(delta_c, beta):
    ## If the cost doesn't increase, we always accept
    if delta_c <= 0:
        return True
    ## If the cost increases and beta is infinite, we always reject
    if beta == np.inf:
        return False
    ## Otherwise the probability is going to be somwhere between 0 and 1
    p = np.exp(-beta * delta_c)
    ## Returns True with probability p
    return np.random.rand() < p

## The simulated annealing generic solver.
## Assumes that the proposals are symmetric.
## The `probl` object must implement these methods:
##    init_config()               # returns None [changes internal config]
##    cost()                      # returns a real number
##    propose_move()              # returns a (problem-dependent) move - must be symmetric!
##    compute_delta_cost(move)    # returns a real number
##    accept_move(move)           # returns None [changes internal config]
##    copy()                      # returns a new, independent opbject
## NOTE: The default beta0 and beta1 are arbitrary.
def simann(probl,
           anneal_steps = 10, mcmc_steps = 100,
           beta0 = 0.1, beta1 = 10.0,
           seed = None, debug_delta_cost = False, 
           optimize = False, #Boolean variable that when True stops the algorithm once a solution to the problem is found
           acceptance_rate = False, #Boolean variable that when True, the function return also the acceptance rate at each anenaling step
           solved = False #Boolean variable to keep track at which annealing step the problem was solved
           ):
    ## Optionally set up the random number generator state
    if seed is not None:
        np.random.seed(seed)

    # Set up the list of betas.
    # First allocate an array with the required number of steps
    beta_list = np.zeros(anneal_steps)
    # All but the last one are evenly spaced between beta0 and beta1 (included)
    beta_list[:-1] = np.linspace(beta0, beta1, anneal_steps - 1)
    # The last one is set to infinty
    beta_list[-1] = np.inf

    # Set up the initial configuration, compute and print the initial cost
    probl.init_config()
    c = probl.cost()
    #print(f"initial cost = {c}")
    #print(probl.x)

    ## Keep the best cost seen so far, and its associated configuration.
    # best = probl.copy()   #Commented to reduce computational cost because my analysis focuses only on the best cost of the solution found
    best_c = c

    counter = 0 #Initialize this counter to keep track after how many annealing steps the problem is solved 
    acc_rate = [] #List to keep track of the acceptance rate over the annealing steps
    # Main loop of the annaling: Loop over the betas
    for beta in beta_list:
        ## At each beta, we want to record the acceptance rate, so we need a
        ## counter for the number of accepted moves
        accepted = 0 #Initialize this variable to count the number of accepted moves at each annealing step in order to compute its acceptance rate
        # For each beta, perform a number of MCMC steps
        for t in range(mcmc_steps):
            move = probl.propose_move()
            #print(probl.x)
            delta_c = probl.compute_delta_cost(move)
            ## Optinal (expensive) check that `compute_delta_cost` works
            if debug_delta_cost:
                probl_copy = probl.copy()
                probl_copy.accept_move(move)
                assert abs(c + delta_c - probl_copy.cost()) < 1e-10
            ## Metropolis rule
            #print(probl.x, c, move, delta_c, accept(delta_c, beta))

            if accept(delta_c, beta):
                probl.accept_move(move)
                #print(probl.x)
                c += delta_c
                accepted += 1
                if c <= best_c:
                    best_c = c
                    # best = probl.copy() #Not necessary for this analysis, commented to reduce computational cost

                    # Return the best cost (=0) if the solution is found
                    if best_c == 0:
                        solved = True
                        if optimize:
                            #print(f"acc.rate={accepted / mcmc_steps} beta={beta} c={c} [best={best_c}]")                            
                            return best_c
        # print(f"acc.rate={accepted / mcmc_steps} beta={beta} c={c} [best={best_c}]")
        if acceptance_rate:
            acc_rate.append(accepted / mcmc_steps)
        if not solved:
            counter += 1
    ## Return the best instance
    # print(f"final cost = {best_c}")
    if acceptance_rate:
        return best_c, acc_rate, counter+1 #+1 to the counter because the last annealing step is not counted by setting solved = True (line 88)
    # return best
    return best_c