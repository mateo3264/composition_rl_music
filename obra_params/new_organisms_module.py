#Más adelante tener en cuenta caracteristicas de los padres
#def add_new_agent(parent_loc,ptss,ntss,msgs,agents,n_agents,)

from constants import *
import numpy as np
import pyOSC3
from agents import Agent
from foods import *
from perception_functions import get_direction_of_nearest_food
from specie_parameters import create_specie
#Recibe parent que da señal de reproducción asexual
#Recibe env para modificar ptss,ntss,n_agents

def feats_of_next_generation(father_feats):
    child_feats = father_feats.copy()
    if np.random.rand() < 0.3 and len(father_feats) > 1:
        idx_of_feat_to_remove = np.random.choice(len(child_feats))
        child_feats.remove(child_feats[idx_of_feat_to_remove])
    if np.random.rand() < 0.3 and len(father_feats) < 3:
        new_feat = np.random.randint(len(STATE_DIMS))
        while new_feat in father_feats:
            new_feat = np.random.randint(len(STATE_DIMS))
        child_feats.append(new_feat)
    return child_feats
    
#def add_new_agent(env,msgs,clients,agents):
def which_specie(p_dist):
    return np.random.choice(SPECIES,p=p_dist)
#TAL VEZ CORREGIR QUE NO MUESTRA TODAS LAS ESPECIES SOLAS
class SpawnOrganisms:
    def __init__(self):
        self.idx = -1
        self.schedule_idx = 0
        self.schedule = [0,20_000,30_000,40_000,50_000,60_000,70_000,80_000,90_000]
        self.n_species = len(SPECIES)
        self.idxs_species_spawned = []
        self.changed = False
        self.some_species = []
        
    def change(self,global_timesteps):
        if self.schedule[self.schedule_idx+1] <= global_timesteps\
           and global_timesteps != 0 and global_timesteps < 80_000:#self.idx != -1:
            if self.schedule[self.schedule_idx+2] <= global_timesteps:
                self.schedule_idx += 1
                self.changed = False
            if not self.changed:
                self.changed = True
                possible_idx = np.random.randint(self.n_species)
                while possible_idx in self.idxs_species_spawned:#== self.idx:
                    possible_idx = np.random.randint(self.n_species)
                self.idx = possible_idx
                self.idxs_species_spawned.append(self.idx)
        elif self.idx == -1:
            idx = np.random.randint(self.n_species)
            return SPECIES[idx]
        return SPECIES[self.idx]
            

spawn_organisms = SpawnOrganisms()

def add_new_agent(creator,env,agents,global_timesteps,idx=None):
    specie = spawn_organisms.change(global_timesteps)#organism_creation_schedule(global_timesteps)#np.array([1,0,0,0,1,0])/2#np.ones(len(SPECIES))/len(SPECIES)
    #specie = which_specie(p_d)#'spe6'#np.random.choice(SPECIES)
    #print('NEW SPECIE',specie)
    
    env.add_agent()
    if idx is not None:
        params = agents[idx].params
        specie = agents[idx].params2['specie']
        _,params2 = create_specie(specie,params)
        #,agents[idx].params2
        #individual_timestep = np.random.randint(-10 + agents[idx].init_individual_timestep,\
                               #agents[idx].init_individual_timestep + 2)#np.random.randint(20//env.max_n_agents,50//env.max_n_agents)#//env.max_n_agents)#5//len(agents),10//len(agents))
        #print('INDI TIMESTEP',individual_timestep)
        #if individual_timestep < 1:
         #   individual_timestep = 1
        #elif individual_timestep > MAX_INDIVIDUAL_TIMESTEP:
            #individual_timestep = MAX_INDIVIDUAL_TIMESTEP
        #misma localización que el padre?
        initial_state = np.random.randint(-2 + agents[idx].params2['current_state'],
                                          agents[idx].params2['current_state'] + 2)#np.random.randint(NSTATES)#np.random.randint(min(env.ptss['pts'+idx_pts],env.ntss['nts'+idx_nts]),max(env.ptss['pts'+idx_pts],env.ntss['nts'+idx_nts]))
        if initial_state < 0:
            initial_state = 0
        elif initial_state > NSTATES - 1:
            initial_state = NSTATES - 1
        #agents[idx].steps_prereproduction = 0
        agents[idx].msg.append([agents[idx].params2['idx'],'rateOfChange',1,
                                      'se',1,'gesture',1,1,'times',1])
        agents[idx].client.send(agents[idx].msg)
        del agents[idx].msg[:]
        father_feats = agents[idx].params2['feats']
        child_feats = feats_of_next_generation(father_feats)
        specie = agents[idx].params2['specie']
        print('Child',specie)
        
        
    else:
        params,params2 = create_specie(specie)
        print('Not Child')
        #print("params2['states_actions']")
        #print(params2['states_actions'])
        #min_individual_timestep = np.random.randint(50,1000)
        #max_individual_timestep = min_individual_timestep + np.random.randint(50,1000)
        #individual_timestep = np.random.randint(min_individual_timestep,max_individual_timestep)
        initial_state = np.random.randint(NSTATES//2)
        child_feats = [1]
    #if specie == 'spe1':
    print('SPEEECIEEE',specie)
    env.species_population[int(specie[-1])-1] +=1 
    agent = Agent(env,params,params2,current_state=initial_state,feats=child_feats)
    if agent.params2['inherit_Qs']:
        print('entro.....')
        if idx is not None:
            if child_feats == father_feats:
                print('HEREDO cerebro')
                agent.params2['Qs'] = agents[idx].params2['Qs']
        else:
            pass
            
            
    print('New agent',agent)
#    print('D')
#    print(agent.params2['D'])
#    print('max_rf_effect')
#    print(agent.params['max_rf_effect_in_timesteps'])
#    print("agent.params2['states_actions']")
#    print(agent.params2['states_actions'])
#    print("agent.params['individual_timestep']")
#    print(agent.params['individual_timestep'])

##    if specie == 'spe3' or specie == 'spe4':
##        agent.min_lifespan = 40
##        agent.max_lifespan = 60
##        agent.individual_timestep = 5
##    if idx is not None:
##        nHarms = np.random.randint(-2 + agents[idx].nHarms,agents[idx].nHarms + 7)
##        if nHarms < 0:
##            nHarms  = 0
##        agent.nHarms = nHarms
    agents.append(agent)#50 es arbitrario

#    print('CHILD FEATS',child_feats)
    creator.create_oscdef_organisms(env.max_n_agents-1,agent)
    
    for feat in agent.params2['feats']:
        if feat not in env.feats_dict:
            env.feats_dict[feat] = []    
        env.feats_dict[feat].append(agent)
        
def add_new_food(creator,env,foods):
    env.add_food()
    #it = np.random.randint(NSTATES)#np.random.randint(60//len(agents),120//len(agents))

    #misma localización que el padre?
    initial_state = np.random.randint(NSTATES)#np.random.randint(min(env.ptss['pts'+idx_pts],env.ntss['nts'+idx_nts]),max(env.ptss['pts'+idx_pts],env.ntss['nts'+idx_nts]))
    f = Food(env,current_state=initial_state)
    foods.append(f)#50 es arbitrario
    env.food_locs.append(initial_state)
    #env.food_locs.append(initial_state)
    env.global_poss_food[initial_state] = 1
    #env.foods.append(f)
    creator.create_oscdef_food(env.max_n_food - 1,f)
    #print('env.foods',env.foods)
    #return f
    
def remove_food(env,foods,agent):
    env.del_food()
    
    idx_of_food_to_remove = None
    for idx,food in enumerate(foods):
        if food.current_state == agent.params2['next_state']:
            env.food_locs.remove(food.current_state)
                    #print(foods)
            del food.msg[:]
            food.msg.append([food.idx,'freq',2666.666,'amp',0.0])
            food.client.send(food.msg)
                    #del food
                    #print(foods)
            idx_of_food_to_remove = idx
            #print('agent.params')
            #print(agent.params['individual_timestep'])
            agent.params['individual_timestep'] -= int(agent.params['individual_timestep']*0.4)
            foods.remove(foods[idx_of_food_to_remove])
            #self.n_food -=1
            break

def remove_agent(env,agent,agents):
    env.del_agent()

    del agent.msg[:]

    agent.msg.append([agent.params2['idx'],'dead','freq',states[agent.params2['freq_zone_idx']][agent.params2['next_state']],'amp',0.0,'t_ga',0,'gesture',0,0,0,'times',0.1,0.1])
    agent.client.send(agent.msg)
    
    agents.remove(agent)

