import pyOSC3
import numpy as np
from constants import *
from agents import *
from creation_of_oscdefs_and_clients import *
from foods import *

##def init_clients(n_clients):
##    clients = {}
##    for client in range(n_clients):
##        clients['client'+str(client)] = pyOSC3.OSCClient()
##        clients['client'+str(client)].connect(('127.0.0.1',57120))
##    return clients

##def init_msgs(n_msgs):
##    msgs = {}
##    for msg in range(n_msgs):
##        msgs['msg'+str(msg)] = pyOSC3.OSCMessage()
##        print('/msg'+str(msg))
##        msgs['msg'+str(msg)].setAddress('/msg'+str(msg))
##
##    return msgs



def init_agents(n_agents,env,individual_timesteps,creator):
    agents = []
    #initial_state = np.random.randint(min(env.ptss['pts'+idx_pts],env.ntss['nts'+idx_nts]),max(env.ptss['pts'+idx_pts],env.ntss['nts'+idx_nts]))
    for i in range(n_agents):
        #agents['agent'+str(agent)] = QAgent(2,len(states))
        initial_state = np.random.randint(NSTATES)#np.random.randint(min(env.ptss[f'pts{i}'],env.ntss[f'nts{i}']),max(env.ptss[f'pts{i}'],env.ntss[f'nts{i}']))
        agents.append(Agent(env,current_state=initial_state,individual_timestep=individual_timesteps[i]))
        creator.create_oscdef_organisms(i)
    return agents   

def init_food(n_food,env,creator):
    foods = []

    for i in range(n_food):
        initial_state = np.random.randint(NSTATES)
        f = Food(env,initial_state)
        foods.append(f)
        
        creator.create_oscdef_food(i,f)
        #foods[-1].send_msg_to_sc()
    return foods

def init_individual_timestep(n_agents):
    timesteps = []
    for _ in range(n_agents):
        #Inizialización arbitraria de individual timesteps rango de (80,120)
        timesteps.append(np.random.randint(1,5))

    return timesteps
            

##def init_tss(n_agents):
##    ptss = {}
##    ntss = {}
##    idxs_ss = np.array([x for x in range(NSTATES)])
##    for agent in range(n_agents):
##        pts = np.random.choice(idxs_ss)
##        nts = np.random.choice(idxs_ss[[x for x in idxs_ss if x!=pts]])
##
##        ptss['pts'+str(agent)] = pts
##        ntss['nts'+str(agent)] = nts
##    return ptss,ntss

