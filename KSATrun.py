import SimAnn
import KSAT
import importlib

importlib.reload(SimAnn)
importlib.reload(KSAT)

seed = 42

def run3sat(N=200, M=200, mcmc_steps=100, anneal_steps=10, beta0=1, beta1=10, seed=seed, acceptance_rate=True):
        ksat = KSAT.KSAT(N, M, 3, seed = seed)
        
        res = SimAnn.simann(ksat,
                               mcmc_steps = mcmc_steps, anneal_steps = anneal_steps,
                               beta0 = beta0, beta1 = beta1,
                               seed = seed,
                               debug_delta_cost = False, # set to True to enable the check
                               acceptance_rate=acceptance_rate)
        return res

