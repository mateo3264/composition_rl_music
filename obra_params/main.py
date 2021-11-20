#A TENER EN CUENTA
#-Si el individual step es muy largo puede que el organismo no se mueva
#HACER:una clase que comunique el current_state de un agente en el env
# con el propio agente de modo que este actualize su current state (hacer
# variable current state para la clase agente)s
#HACER:Reproduccion
#HACER:Que cada organismo tenga su timestep
#HACER:aleatoriedad en cada iteracion
#HACER:Cambiar codigo debajo de la palabra INEFICIENTE 
#HACER:separar la velocidad de movimiento de un organismo
# y que tan rapido se reproduce
#HACER:
import pyOSC3
import time
from time import sleep as s
import random
from agents import Agent
import numpy as np
from visualize_agents import *#draw_env,draw_agents,show_all
from environments import Env
from initializing_functions import *
import constants
from constants import *
from new_organisms_module import add_new_agent,add_new_food
from creation_of_oscdefs_and_clients import Creator
import matplotlib.pyplot as plt
from perception_functions import *


creator = Creator()

matplotvis = MatplotVis()






agents = []
foods = []
env = Env(NSTATES)



total_steps = 0
timess = []

def turn_off_connection_with_sc(total_timesteps,timesteps_to_change_state=3000):
    if total_timesteps >= timesteps_to_change_state:
        return True
    return False


for e in range(episodes):



    #CORREGIR
    if test:
        agents = {}
        for agent in agents:
            agents[agent].params2['Qs'] = np.load('agent'+str(agent[-1])+'.npy')
            agents[agent].params['epsilon'] = 0.0 


    print('***NEW EPISODE***',e)
    steps = 0

    first = True
    first_agent = False

    for i,agent in enumerate(agents):
        agent.reset(i)
        
    while True:
        initial_time = time.time()

        environ = draw_env(NSTATES,foods)

        draw_agents(environ,[agent.params2['current_state'] for agent in agents])
        show_all(environ)
        if e % 10 == 0:
            for agent in agents:
                if first:
                    if debugging:
                        print('agent.Qs',np.round(agent.params2['Qs'],4))
                    
            first = False

        #MODIFICAR: Con NNs, este for loop se vuelve muy costoso (sin mencionar
        # el incremento del costo en funcion del numero de acciones) por lo que
        # debe hacerse solo cuando sea momento de actuar (segun individual timestep)
        #acts = []
        #INEFICIENTE

        new_states = []

        num_agents = env.n_agents
        
        
        for i in range(num_agents):
            if agents[i].is_trying_to_reproduce():
#            if agents[i].params['n_steps_to_reproduce'] - 3 <= \
 #              agents[i].params2['timesteps_alive'] % agents[i].params['n_steps_to_reproduce']:
                
                agents[i].params2['steps_prereproduction'] +=1
                agents[i].msg.append([agents[i].params2['idx'],'rateOfChange',0.995**agents[i].params2['steps_prereproduction'],
                                      'se',-1,'amp',0.1,'pan',agents[i].params2['pan'],'gesture',1,1,'times',1])
                agents[i].client.send(agents[i].msg)
                
                del agents[i].msg[:]
  #          if agents[i].params2['timesteps_alive'] % agents[i].params['n_steps_to_reproduce'] == 0:
   #             print('aca')
    #            if agents[i].params2['timesteps_alive'] != 0:
     #               agents[i].params2['timesteps_alive'] +=1
            if agents[i].params2['timestep_to_act'] == agents[i].params['individual_timestep']:
                if agents[i].reproduce():
                    print('agents[i]',agents[i])
                    print('SUCCEDING IN REPRODUCING')
                    add_new_agent(creator,env,agents,steps,i)


        if np.random.rand() < EPSILON_FOOD and steps > 120:
            add_new_food(creator,env,foods)
            constants.states = np.linspace(np.random.randint(50,100),np.random.randint(200,1500),NSTATES)

            
        #MODIFICAR: solo cuando individual_timestep == steps
        if steps % 1000 == 0:
            print('steps',steps)
        if np.random.rand() < EPSILON_NEW_AGENT:
                add_new_agent(creator,env,agents,steps)
        
        for agent in agents:
            
            agent.choose_action()
            
        env.step(agents,foods)


        if debugging:
            if e>=0:
                for i,agent in enumerate(agents):
                    pass
        if not test:
            for agent in agents:
              
                if agent.params2['current_action'] != 2:

                    agent.learn()
                    agent.params2['current_state'] = agent.params2['next_state']
                    feat_idx = 0
                    if 0 in agent.params2['feats']:
                        agent.params2['total_current_state'][feat_idx] = agent.params2['current_state']
                        feat_idx +=1
                    if 1 in agent.params2['feats']:
                        agent.params2['total_current_state'][feat_idx] = get_direction_of_nearest_food(agent.params2['current_state'],env.food_locs)
                        feat_idx +=1
                    if 2 in agent.params2['feats']:
                        agent.params2['total_current_state'][feat_idx] = get_direction_of_most_food(agent.params2['current_state'],env.food_locs)
                        feat_idx +=1

        steps +=1
        total_steps +=1


    


        
        
