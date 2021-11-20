import numpy as np
import pyOSC3
from constants import *
import re
from specie_parameters import specie_params
from copy import deepcopy

#-Generalizar el numero de dimensiones del estado tal vez con *s (siendo s una lista)
#-todo lo que tiene que ver con incrementos (como numero de steps en episodio) hacerlo en una
# funcion y mirar cual es la mejor funcion de la clase Agent para incorporarlo de tal modo
# que no importa el ambiente, funcione correctamente
#-AGENTE con expected sarsa y donde los refuerzos tienen efecto en acciones
# anteriores a la hecha actualmente
#-AGREGAR: Refuerzo intrinseco basado en novedad



class Agent:
    def __init__(self,env,params,params2,current_state=None,kind_of_food='herbivore',feats=[0]):
        self.params = deepcopy(params)#.copy()
        self.params2 = deepcopy(params2)#.copy()
#        self.params = params.copy()
 #       self.params2 = params2.copy()

        #print('NEW AGENT AGENT')
        #sprint(self.params2)
        #self.params2['env'] = env
        self.params2['env'] = env
        #self.feats = sorted(feats)
        self.params2['feats'] = sorted(feats)
        #self.params2['n_actions'] = n_actions
        #self.params2['specie'] = specie
        #print('self.params2['specie']',self.params2['specie'])
        #print("re.findall('\d+',self.params2['specie'])")
        #print(re.findall('\d+',self.params2['specie']))
        self.params2['freq_zone_idx'] = int(re.findall('\d+',self.params2['specie'])[0]) - 1
        #self.init_individual_timestep = individual_timestep
        #self.params['individual_timestep'] = individual_timestep
        #self.params2['timestep_to_act'] = 0
        #self.max_individual_timestep = individual_timestep + 2#10//env.max_n_agents #int(individual_timestep*0.2)
        #self.min_individual_timestep = 1
        #self.total_individual_timesteps_taken = 0
        #self.params2['life_timestep'] = 0

        #self.params2['life_span'] = np.random.randint(self.min_lifespan,self.max_lifespan)
        #self.params2['timesteps_from_last_meal'] = 0
        #self.params['individual_timestep']
        #self.params2['individual_timesteps_to_be_more_tired'] = np.random.randint(1,self.min_lifespan)#(100//env.max_n_agents)+5)
        #self.params['alpha'] = alpha
        #self.params['epsilon'] = epsilon
        #self.params['om'] = om
        self.set_dims_of_state()
        #self.params2['Qs'] = np.zeros((self.params2['env'].n_states,2))
        self.params2['Qs'] = np.zeros(self.state_dims+[self.params2['n_actions']])
        #self.params2['steps'] = 0
        #self.params2['states_actions'] = []
        #self.params2['steps_prereproduction'] = 0
        #self.params['n_steps_to_reproduce'] = 500#*env.max_n_agents
        #self.params['freq_factor'] = 5
        #self.params2['timesteps_alive'] = 0
        #self.params2['D'] = 0
        #self.params2['K'] = 1
        self.params2['idx'] = self.params2['env'].max_n_agents - 1
        #self.params2['n_times_actions_taken'] = np.zeros((self.params2['env'].n_states,2))
        self.params2['n_times_actions_taken'] = np.zeros(self.state_dims+[self.params2['n_actions']])
        self.params2['state_counter'] = np.zeros(self.state_dims)
        #self.params['max_rf_effect_in_timesteps'] = np.random.randint(1,env.max_n_agents*2)
        #print('self.params['max_rf_effect_in_timesteps']')
        #print(self.params['max_rf_effect_in_timesteps'])
        #self.params2['last_action'] = None
    #    self.params2['current_action'] = None
        self.init_connection_with_supercollider()
        self.params2['current_state'] = current_state
        self.params2['total_current_state'] = np.zeros(len(self.state_dims),dtype=np.int8)
        self.params2['total_next_state'] = np.zeros(len(self.state_dims),dtype=np.int8)
#        print('states[self.params2['freq_zone_idx']][self.params2['current_state']]')
 #       print(states[self.params2['freq_zone_idx']][self.params2['current_state']])   
        self.params2['pan'] = 2*((states[self.params2['freq_zone_idx']][self.params2['current_state']] - min(states[self.params2['freq_zone_idx']])))/(max(states[self.params2['freq_zone_idx']])-min(states[self.params2['freq_zone_idx']])) - 1
        #print('agent.current_state')
        #print(self.params2['current_state'])
        self.params2['next_state'] = self.params2['current_state']

        self.params2['half_life'] = self.params['life_span']//2
        #self.params2['steps_prereproduction'] = np.random.randint(self.params2['half_life'] - self.params2['half_life'],
         #                                                         self.params2['half_life'] + self.params2['half_life'])
        #self.params2['extrinsic_reward'] = 0
        self.params2['gesture_factor'] = np.random.uniform(0.1,1.9)
        #self.params2['intrin_reward'] = 0
        #self.params2['kind_of_food'] = kind_of_food
        
        
        #SONIC CHARACTERISTICS
        #self.params['nHarms'] = 0
    def __repr__(self):
        return f"Agent{self.params2['idx']}"
    
    def is_trying_to_reproduce(self):
        if self.params2['half_life'] - self.params2['half_life']//4 <= \
           self.params2['timesteps_alive']  <= self.params2['half_life'] + self.params2['half_life']//4:
            return True
        return False
    def reproduce(self):
            probability_reproducing = 1/(15*(self.params2['timesteps_from_last_meal']+1))
            #print('probability_reproducing')
            #print(probability_reproducing)
            if np.random.rand() < probability_reproducing:
                return True
            return False
        
    def set_dims_of_state(self):
        self.state_dims = []
        for feat in self.params2['feats']:
            if feat in STATE_DIMS:
                if isinstance(feat,list):
                    for i,dim in enumerate(feat):
                        self.state_dims.append(STATE_DIMS[feat][i])
                else:
                    self.state_dims.append(STATE_DIMS[feat])

    def init_total_current_state(self):
        if 0 in self.feats:
            self.params2['total_current_state'][0] = agent.next_state
        if 1 in agent.feats:
            self.params2['total_current_state'][1] = get_direction_of_nearest_food(self.params2['next_state'],self.food_locs)
        if 2 in agent.feats:
            self.params2['total_current_state'][2] = get_direction_of_most_food(self.params2['next_state'],self.food_locs)
        if 3 in agent.feats:
            self.params2['total_current_state'][3] = None
        
    def init_connection_with_supercollider(self):
        self.client = pyOSC3.OSCClient()
        self.client.connect(('127.0.0.1',57120))
        self.msg = pyOSC3.OSCMessage()
        #self.msg.setAddress(f'/msg{self.params2['env'].n_actions}')
        #print('al crearse',self.params2['env'].n_agents)
        
        self.msg.setAddress(f"/msg{self.params2['idx']}")

    def hyper(self,D):
        #print('D',D)
        #print("self.params2['K']",self.params2['K'])
##        if D < 0:
##            print('agent')
##            print(self)
##            print("self.params2['states_actions']")
##            print(self.params2['states_actions'])
##            print("self.params2['D']")
##            print(self.params2['D'])
##            print("self.params['max_rf_effect_in_timesteps']")
##            print(self.params['max_rf_effect_in_timesteps'])
        return 1/(1 + self.params2['K']*D)
    #MODIFICAR: debido a que  solo cada x numero de pasos se
    #toma una acción, se debe incrementar solo en ese momento        
    def update_vars(self,next_state):
##        print('AGENT ANTES')
##        print(hex(id(specie_params)))
##        print(hex(id(self.params2['states_actions'])))
##        print(specie_params[self.params2['specie']]['nn']['states_actions'])
##        print(self.params2['states_actions'])
        self.params2['states_actions'].append((self.params2['total_current_state'],self.params2['current_action']))
##        print('AGENT DESPUES')
##        print(specie_params[self.params2['specie']]['nn']['states_actions'])
##        print(self.params2['states_actions'])
        
        if self.params['max_rf_effect_in_timesteps'] < len(self.params2['states_actions']):
            self.params2['states_actions'].pop(0)
            
        self.params2['n_times_actions_taken'][tuple(self.params2['total_current_state'])+(self.params2['current_action'],)] += 1
        self.params2['steps'] +=1
        self.params2['D'] +=1
        self.params2['state_counter'][tuple(self.params2['total_current_state'])] +=1
        self.params2['intrin_reward'] = 0
        self.params2['pan'] = 2*((states[self.params2['freq_zone_idx']][next_state] - min(states[self.params2['freq_zone_idx']])))/(max(states[self.params2['freq_zone_idx']])-min(states[self.params2['freq_zone_idx']])) - 1
    def intrinsic_reward(self):
        #print('self.params2['next_state']',self.params2['next_state'])
        reward = 0
        if self.params2['state_counter'][tuple(self.params2['total_next_state'])] < 5:
            reward = 0.01/(self.params2['state_counter'][tuple(self.params2['total_next_state'])] + 1)
##        else:
##            if self.params2['current_action'] != 2:#2 is for rest or stand still
##                reward = -0.01
        #print('state_counter',s_)
        #print(self.params2['state_counter'][s_])
        #print('intrinsic reward')
        #print(reward)
        self.params2['intrin_reward'] = reward
        
    def choose_action(self):
        self.params2['last_action'] = self.params2['current_action']
        p = np.random.rand()
        
        if p < self.params['epsilon']:
            a = np.random.choice(self.params2['env'].n_actions)    
            #return a
        else:
#            print('self.params2['total_current_state']')
 #           print(self.params2['total_current_state'])
  #          print('self.params2['Qs'].shape')
   #         print(self.params2['Qs'].shape)
    #        print('self.params2['Qs'][(self.params2['total_current_state'])]')
         #       print('self.params2['Qs'][(0)]')
      #      print(self.params2['Qs'][(0)])
       #     print('tuple(self.params2['total_current_state'])')
        #    print(tuple(self.params2['total_current_state']))
         #   print(self.params2['Qs'][tuple(self.params2['total_current_state'])])
            if np.all(self.params2['Qs'][tuple(self.params2['total_current_state'])]==0):
                a = np.random.choice(self.params2['env'].n_actions)
            else:
                a = np.argmax(self.params2['Qs'][tuple(self.params2['total_current_state'])])

        self.params2['current_action'] = a
        return a
        
    def expected_sarsa(self,s_):
        next_q = 0
        #print('s_')
       # print(s_)
      #  print('self.params2['Qs'][s_]')
     #   print(self.params2['Qs'][s_])
    #    print('self.params2['env'].n_actions')
   #     print(self.params2['env'].n_actions)
        den = np.sum(self.params2['n_times_actions_taken'][s_])+1
        #print('s_____________',s_)
  #      print('self.params2['n_times_actions_taken'][s_]')
 #       print(self.params2['n_times_actions_taken'][s_])
        
        for a in range(self.params2['env'].n_actions):
#            print('a','s_',a,s_)
            next_q += (self.params2['n_times_actions_taken'][s_+(a,)]/den)*self.params2['Qs'][s_+(a,)]
##        print('self.params2['n_times_actions_taken'][s_,a]')
##        print(self.params2['n_times_actions_taken'][s_,a])
##        print('den')
##        print(den)
##        print('num/den')
##        print(self.params2['n_times_actions_taken'][s_,a]/den)
##        print('self.params2['Qs'][s_,a]')
##        print(self.params2['Qs'][s_,a])
##        print('next_q')
##        print(next_q)
        return next_q
    
    def learn(self):
        a = self.params2['current_action']
        reward = self.params2['extrinsic_reward'] + self.params2['intrin_reward']
        #print('learn reward',reward)
#        if self.params2['D']one:
 #           target = reward
#        else:
            #if self.params2['idx'] == 1 or self.params2['idx'] == 3:
        target = reward + self.params['om']*self.expected_sarsa(tuple(self.params2['total_next_state']))
##            elif self.params2['idx'] == 0 or self.params2['idx'] == 2:
##                target = reward + self.params['om']*np.max(self.Q[s_[0],s_[1]])
##        if self.params2['idx'] == 0 or self.params2['idx'] == 3:
        #print('target',target)
        first = True
        for step in range(len(self.params2['states_actions'])):#self.params2['steps']):
                past_s,past_a = self.params2['states_actions'][step]
                
                h = self.hyper(self.params2['D'] - step)
                #print('h{}'.format(step),h)
                #print(30*'*')
                #print('self.params2['Qs'][past_s,past_a]')
                #print(self.params2['Qs'][past_s,past_a])
##                if first:
##                    print('BEEEEFFOOOOOREEEEE self.params2['Qs'][past_s,past_a]')
##                    print('h',h)
##                    print('self.params['alpha']',self.params['alpha'])
##                    print(self.params2['Qs'][past_s,past_a])
                #print('LEARN')
                #print('tuple(past_s)+(past_a,)')
                #print(tuple(past_s)+(past_a,))
                #print(self.params2['Qs'][tuple(past_s)+(past_a,)])
                self.params2['Qs'][tuple(past_s)+(past_a,)] += h*self.params['alpha']*(target - self.params2['Qs'][tuple(past_s)+(past_a,)])
##                if first:
##                    print('AAAAAAFFFTEEERRRR self.params2['Qs'][past_s,past_a]')
##                    print(self.params2['Qs'][past_s,past_a])
        #print('np.max(self.params2['Qs'])',np.max(self.params2['Qs']))
                #print(self.params2['Qs'][past_s,past_a])
#        elif self.params2['idx'] == 1:
 #           self.Q[s[0],s[1],a] += self.params['alpha']*(target - self.Q[s[0],s[1],a])
  #      else:

   #         self.Q[s[0],s[1],a] += self.params['alpha']*(target - self.Q[s[0],s[1],a])
        #self.params2['extrinsic_reward'] = 0
        #self.params2['intrin_reward'] = 0

    #CORREGIR ptss ntss
    def reset(self,idx):
        self.params2['states_actions'] = []
        self.params2['D'] = 0
        #self.params2['n_times_actions_taken'] = np.zeros((self.params2['env'].n_states,4))
        self.params2['n_times_actions_taken'] = np.zeros(self.state_dims+[self.params2['n_actions']])
        #self.params2['state_counter'] = np.zeros(self.params2['env'].n_states)
        self.params2['steps'] = 0
        #self.done = False
        self.params2['current_state'] = np.random.randint(NSTATES)#np.random.randint(min(self.params2['env'].ptss[f'pts{idx}'],self.params2['env'].ntss[f'nts{idx}']),max(self.params2['env'].ptss[f'pts{idx}'],self.params2['env'].ntss[f'nts{idx}']))














