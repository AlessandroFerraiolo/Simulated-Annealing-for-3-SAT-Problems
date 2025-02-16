import numpy as np
from copy import deepcopy

class KSAT:
    def __init__(self, N, M, K, seed = None):
        if not (isinstance(K, int) and K >= 2):
            raise Exception("k must be an int greater or equal than 2")
        self.K = K
        self.M = M
        self.N = N

        ## Optionally set up the random number generator state
        if seed is not None:
            np.random.seed(seed)
    
        # s is the sign matrix
        s = np.random.choice([-1,1], size=(M,K))
        
        # index is the matrix reporting the index of the K variables of the m-th clause 
        index = np.zeros((M,K), dtype = int)        
        for m in range(M):
            index[m] = np.random.choice(N, size=(K), replace=False)
            
        # Dictionary for keeping track of literals in clauses
        clauses = []   
        for n in range(N):
            clauses.append([i for i, row in enumerate(index) if n in row])
        
        self.s, self.index, self.clauses = s, index, clauses        
        
        ## Inizializza la configurazione
        x = np.ones(N, dtype=int)
        self.x = x
        self.init_config()

    ## Initialize (or reset) the current configuration
    def init_config(self):
        N = self.N 
        self.x[:] = np.random.choice([-1,1], size=(N))
        
        
    ## Definition of the cost function
    # Here you need to complete the function computing the cost using eq.(4) of pdf file
    def cost(self,affected_clauses=None):
        
        if affected_clauses is None:
            # Compute cost for all clauses
            x = self.x[self.index]
            s = self.s
        else:
            # Compute cost only for clauses affected in the proposed move
            x = self.x[self.index[affected_clauses]]
            s = self.s[affected_clauses]
        
        # Compute the cost of each clause
        clauses_cost = np.prod((1 - s * x) / 2, axis=1)
        
        # Return  the sum of the cost of all clauses
        return clauses_cost.sum()
    
    ## Propose a valid random move. 
    def propose_move(self):
        N = self.N
        move = np.random.choice(N)
        return move
    
    ## Modify the current configuration, accepting the proposed move
    def accept_move(self, move):
        self.x[move] *= -1

    ## Compute the extra cost of the move (new-old, negative means convenient)
    # Here you need complete the compute_delta_cost function as explained in the pdf file
    def compute_delta_cost(self, move):
        
        # Find influenced clauses
        affected_clauses = self.clauses[move]

        # Compute old cost
        old_cost = self.cost(affected_clauses)

        # Temporarly flip x[move] accepting the proposed move
        self.accept_move(move)

        # Compute the cost for the new proposed x
        new_cost = self.cost(affected_clauses)

        # Flip back x[move] to its initial value
        self.accept_move(move)

        # Return the difference between the new and the old cost
        return new_cost - old_cost
    

    ## Make an entirely independent duplicate of the current object.
    def copy(self):
        return deepcopy(self)
    
    ## The display function should not be implemented
    def display(self):
        pass
        

