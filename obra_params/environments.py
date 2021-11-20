import numpy as np
from constants import *
from new_organisms_module import *
from perception_functions import *



        
        

class Env:
    #MODIFICAR: Reemplazar el parametro de n_agents por los agentes de modo
    # que se pueda llamar a cada uno para por ejemplo llamar numero de acciones
    # de cada uno
    def __init__(self,n_states,n_actions=2):
        self.global_poss_food = np.zeros(n_states)
        self.n_agents = 0
        self.max_n_agents = self.n_agents
        self.n_food = 0
        self.max_n_food = self.n_food
        self.n_actions = n_actions
        self.n_states = n_states
        self.feats_dict = {}
#        self.ptss = ptss
#        self.ntss = ntss
        #self.initial_states,_ = self.reset(agents)
        self.last_actions = [None for _ in range(self.n_agents)]
        self.last_actions = {f'agent{a}':None for a in range(self.n_agents)}
        self.food_locs = []
        self.species_population = [0,0,0,0,0,0]
    #def reset(self):
    def add_agent(self):
        self.n_agents +=1
        self.max_n_agents +=1#self.n_agents if self.n_agents > self.max_n_agents else self.max_n_agents

    def add_food(self):
        self.n_food +=1
        self.max_n_food +=1 #self.n_food if self.n_food > self.max_n_food else self.max_n_food
        
    def del_food(self):
        if self.n_food > 0:
            self.n_food -=1
    def del_agent(self):
        if self.n_agents > 0:
            self.n_agents -=1
        
    def reset(self,agents):
        print('env.reset() USADO')

        for i,agent in enumerate(agents):
            initial_state = np.random.randint(NSTATES)
            agent.params2['current_state'] = intial_state

            
        self.current_states = initial_states.copy()
    #MODIFICAR: Cambiar para hacerla similar al api de gym
    def step(self,agents,foods):
        
        for i,agent in enumerate(agents):
            
            
            if agent.params2['timestep_to_act'] != agent.params['individual_timestep'] and \
               agent.params2['timestep_to_act'] != 0:

                action = NULL_ACTION#100 es un numero arbitrario

                agent.params2['last_action'] = agent.params2['current_action'] 

                agent.params2['current_action'] = action
            agent_indiv_time = agent.params['individual_timestep']

            if agent.params2['current_action'] == 0:

                    agent.params2['timesteps_alive'] += 1
                    if 1 <= agent.params2['current_state']:
                        agent.params2['next_state'] =  agent.params2['current_state'] - 1
                    else:
                        agent.params2['next_state'] =  agent.params2['current_state']
      
            elif agent.params2['current_action'] == 1:
                    agent.params2['timesteps_alive'] += 1
                    if agent.params2['current_state'] < self.n_states - 1:
                        agent.params2['next_state'] =  agent.params2['current_state'] + 1
                    else:
                        agent.params2['next_state'] = agent.params2['current_state']
            elif agent.params2['current_action'] == 2:
                pass
                #print('AGENT CURRENT ACTION',agent.params2['current_action'])

            feat_idx = 0
            if 0 in agent.params2['feats']:
                agent.params2['total_next_state'][feat_idx] = agent.params2['next_state']
                feat_idx +=1
            if 1 in agent.params2['feats']:
                agent.params2['total_next_state'][feat_idx] = get_direction_of_nearest_food(agent.params2['next_state'],self.food_locs)
                feat_idx +=1
            if 2 in agent.params2['feats']:
                agent.params2['total_next_state'][feat_idx] = get_direction_of_most_food(agent.params2['next_state'],self.food_locs)
                feat_idx +=1



                                            
            if agent.params2['timestep_to_act'] == agent_indiv_time:# or agent.params2['timestep_to_act'] == 0:
##                print('agent',agent)
##                print("agent.params['life_span']",agent.params['life_span'])
##                print("agent.params2['life_timestep']",agent.params2['life_timestep'])
                #print('AAGGEEENNNTTT')
                #if agent.params2['specie']
                #print(self.species_population)
                specific_args = []
##                if agent.params2['specie'] == 'spe1':
##                    n_spe_existed = self.species_population[int(agent.params2['specie'][-1])-1]
##                    min_time = 1/3*(n_spe_existed)
##                    max_time = 1/2*(n_spe_existed)
##                    min_max_harms = np.random.randint(1,n_spe_existed+1)
##                    max_max_harms = np.random.randint(1,10*n_spe_existed)
##                    div_factor = np.random.randint(1,n_spe_existed+1)
##                    specific_args = [\
##                        'min_time',min_time,'max_time',max_time,
##                        'min_max_harms',min_max_harms,
##                        'max_max_harms',max_max_harms,
##                        'div_factor',div_factor
##                        ]
                vol = 0.1/(np.sqrt(agent.params2['next_state'])+1)
                agent.update_vars(agent.params2['next_state'])
                
                if agent.params2['current_action'] == 0:
                    act0_sound = list(np.array([1.5,0.6,1.3,1])*agent.params2['gesture_factor'])
                elif agent.params2['current_action'] == 1:
                    act0_sound = list(np.array([1.2,0.7,1.4,1])*agent.params2['gesture_factor'])
                elif agent.params2['current_action'] == 2:
                    act0_sound = list(np.array([1.1,0.9,1.1,0.9])*agent.params2['gesture_factor'])
                agent.msg.append([*specific_args,agent.params2['idx'],'freq',agent.params['freq_factor']*states[agent.params2['freq_zone_idx']][agent.params2['next_state']],'amp',0.05,'pan',agent.params2['pan'],'nHarms',agent.params['nHarms'],'t_ga',1,'gesture',act0_sound,'times',[0.05,0.15,0.1]])
                agent.client.send(agent.msg)
                del agent.msg[:]


                agent.intrinsic_reward()
                self.get_reward(agent,foods,agents)
                agent.params2['timestep_to_act'] = 0
                if  agent.params2['timesteps_from_last_meal'] % agent.params['individual_timesteps_to_be_more_tired'] == 0:
#                    print('MORE TIRED')
                    agent.params['individual_timestep'] += 1
                agent.params2['life_timestep'] +=1
            agent.params2['timestep_to_act'] +=1

    def get_reward(self,agent,foods,agents):

        reward = -0.01
        if agent.params2['current_state'] == agent.params2['next_state'] and agent.params2['current_action'] != NULL_ACTION \
           and agent.params2['next_state'] not in [food.current_state for food in foods]:
            if debugging:
                print('this action',agent.params2['current_action'])
            reward = 0.0

            agent.params2['extrinsic_reward'] = reward
            

            
        if agent.params2['current_action'] == NULL_ACTION and agent.params2['next_state'] \
               not in [food.current_state for food in foods]:
           reward = 0.0
           agent.params2['extrinsic_reward'] = reward
        elif agent.params2['next_state'] in [food.current_state for food in foods] and \
            agent.params2['current_state'] != agent.params2['next_state']:
            
            remove_food(self,foods,agent)

            if agent.params['individual_timestep'] < 1:
                agent.params['individual_timestep'] =  1
            reward = 1.0
            agent.params['life_span'] += np.random.choice([2,3])
            agent.params2['extrinsic_reward'] = reward
            agent.msg.append([agent.params2['idx'],'freq',states[agent.params2['freq_zone_idx']][agent.params2['next_state']],'amp',0.1,'pan',agent.params2['pan'],'nHarms',agent.params['nHarms'],'t_ga',1,'gesture',[2.8,2.5,2.8,0.6],'times',[0.7,0.1,0.1]])
            agent.client.send(agent.msg)
            del agent.msg[:]


        elif agent.params2['current_state'] == agent.params2['next_state'] and agent.params2['next_state'] in [food.current_state for food in foods]:
            reward = 1.0

            agent.params2['extrinsic_reward'] = reward

        else:
            reward = -0.01

            agent.params2['extrinsic_reward'] = reward

        if reward != 1.0:
            agent.params2['timesteps_from_last_meal'] += 1
        elif reward == 1.0:
            agent.params2['timesteps_from_last_meal'] = 0
            
        agent.params2['extrinsic_reward'] = reward

        if agent.params['life_span'] == agent.params2['life_timestep']:# and len(agents) > 1:
            if agent in agents:
                remove_agent(self,agent,agents)

