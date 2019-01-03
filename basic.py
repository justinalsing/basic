import pystan
import numpy as np

def run_basic_sampler(d, s, transition_prior, gamma=100, beta=0.1):
    
    # Build the stan model
    code = """
        
        data {
            int N; // number of time steps
            int n; // number of composited to be merged
            real beta; // beta for the BT likelihood
            real gamma; // gamma for the BT likelihood
            vector[N] d[n]; // n-composites vectors of N-time-steps -- the data
            vector[N] s[n]; // corresponding standard deviation for each data point
            vector[N] m; // mean jump value for the transition prior
            vector[N] q; // standard deviations for the transition prior
        }
        
        parameters {
            vector[N] y; // true-time series
        }
        
        model{
        
            // initial y-value has a broad uniform prior (default in stan if unspecified)
            y[2:N] ~ normal(y[1:N-1] + m[2:N], q[2:N]);
        
            // Likelihood
        
            // for every time step
            for(t in 1:N){
        
                // for every composite
                for(c in 1:n){
                
                    // add Box-Tiao likelihood to the "target", ie the log-likleihood
                    target += log_sum_exp( log(beta) + normal_lpdf(y[t] | d[c][t], gamma*s[c][t]), log(1-beta) + normal_lpdf(y[t] | d[c][t], s[c][t]) );
                }
            }
        }
    """
    
    # Compile the model
    model = pystan.StanModel(model_code=code)

    # Number of composites
    n = len(d)
    
    # Length of composites (number of time steps)
    N = len(d[0])
    
    # Construct transition prior will go here in the end...
    
    # Construct SVD errors will go here in the end...
    
    # Define the data
    composite_data = {
                        'd':np.array(d),
                        's':np.array(s),
                        'n':n,
                        'N':N,
                        'beta':beta,
                        'gamma':gamma,
                        'm':transition_prior[0],
                        'q':transition_prior[1]
                    }

    # Starting point for the chains
    initialization = []
    for k in range(0,n):
        initialization.append({'y':d[k]})
    initialization.append({'y':np.mean(np.array(d), axis=0)})
                      
    # Run the sampler
    fit = model.sampling(data=composite_data, iter=20000, chains=n+1, init=initialization, warmup=1000)

    # Extract the chain
    chain = fit.extract()['y']

    return chain
