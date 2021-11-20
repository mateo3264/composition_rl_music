import numpy as np

test = False
debugging = False
NAGENTS = 1
NFOOD = 0
NSTATES = 20
STATE_FACTOR = 10
NULL_ACTION = 100
MAX_INDIVIDUAL_TIMESTEP = 5000
##individual_timestep = [50]#[2,3,5,4,7]#init_individual_timestep(NAGENTS)        

#states = (np.arange(NSTATES,dtype=np.float32)+20)*STATE_FACTOR
#states = np.linspace(50,1000,NSTATES)
#print(states)
episodes = 1000
EPSILON_FOOD = 0.00035
EPSILON_NEW_AGENT = 0.00055
STEP_BEFORE_FIRST_AGENT = 100

SPECIES = ['spe1','spe2','spe3','spe4','spe5','spe6']




attributes = {'spe3':{'reproduction':'slow','movement':'fast',
                      'range':'large','params':{'midRange':[3,2400]}},
              'spe4':{'range':'large'},
              'spe5':{}
              }
freq_zones = []

for i in range(len(SPECIES)):
    if i == 2:
        min_freq = np.random.randint(50,100)
        max_freq = np.random.randint(100,500) + min_freq
    elif i == 3:
        min_freq = np.random.randint(100,250)
        max_freq = np.random.randint(700,1100) + min_freq
    elif i == 4:
        min_freq = np.random.randint(10,50)
        max_freq = np.random.randint(100,200) + min_freq
    elif i == 5:
        min_freq = np.random.randint(100,150)
        max_freq = np.random.randint(100,150) + min_freq
    else:
        min_freq = np.random.randint(50,100)
        max_freq = np.random.randint(50,100) + min_freq
    zone = np.linspace(min_freq,max_freq,NSTATES)
    freq_zones.append(zone)

states = freq_zones#np.array(freq_zones)
print(states)
#print(freq_zones)

    
#FEATURES
#0:current_state
#1:direction of nearest food
#2:direction of most food
#3:get own action as feat
#4:susceptible to rf by proximity to food
STATE_DIMS = {0:NSTATES,1:3,2:3}



