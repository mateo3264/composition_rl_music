import pyOSC3
from constants import *
#Clase que crea oscdefs en supercollider y clients y messages en python
class Creator:
    def __init__(self):
        self.client_creator = pyOSC3.OSCClient()
        self.client_creator.connect(('127.0.0.1',57120))

        self.msg_creator = pyOSC3.OSCMessage()
        self.msg_creator.setAddress('/msg00')
        #n_organisms = 0
        #self.species = ['sin1','sin3','sin4','sin5','sin6','sin7']
        #msgs = {}

    def create_oscdef_organisms(self,max_n_agents,agent):
        #global n_organisms
        #specie  = np.random.choice(self.species)
        specie = agent.params2['specie']
        self.msg_creator.append((f'listener{max_n_agents}',f'listener{max_n_agents} created',f'/msg{max_n_agents}',specie,'freq',states[agent.params2['freq_zone_idx']][agent.params2['current_state']],'amp',0.1,'pan',0,'nHarms',agent.params['nHarms'],'gesture',1.1,0.9,1.1,'times',0.2,0.2))
        self.client_creator.send(self.msg_creator)
        del self.msg_creator[:]
        
        agent.msg.append([agent.params2['idx'],'freq',states[agent.params2['freq_zone_idx']][agent.params2['next_state']],'amp',0.05,'pan',agent.params2['pan'],'nHarms',agent.params['nHarms'],'gesture',[1,1,1,1]])
        
        agent.client.send(agent.msg)
        del agent.msg[:]
#        self.msg_creator.append((f'listener{max_n_agents}',f'listener{max_n_agents} created',f'/msg{max_n_agents}',states[agent.current_state],0.5,agent.pan,agent.nHarms,[1,1]))
#        self.client_creator.send(self.msg_creator)
#        del self.msg_creator[:]
        #n_organisms +=1
        #n_agents +=1
        #return n_agents

    def create_oscdef_food(self,max_n_food,food):
        #global n_organisms
        self.msg_creator.append((f'Flistener{max_n_food}',f'Flistener{max_n_food} created',f'/Fmsg{max_n_food}','freq',food.current_freq_state,'amp',0.005,'pan',food.pan))
        self.client_creator.send(self.msg_creator)
        del self.msg_creator[:]
        #n_organisms +=1
        #n_food +=1
        #return n_food

    def send_to_organism_listeners(self,message,msgs,to_organism=0):
        idx_msg = str(to_organism)
        key = 'msg'+idx_msg
        #if 'msg'+str(to_organism) not in msgs:
##        if key not in msgs:
##            mg = pyOSC3.OSCMessage()
##            #mg.setAddress(f'/msg{to_organism}')
##            mg.setAddress(f'/{key}')
##            msgs[key] = mg
        msgs[key].append(message)
        #print('que?',msgs[key])
        #print(msgs[key][0])
        #print(len(msgs[key]))

        client.send(msgs[key])
##
        
##import numpy as np
##
##for i in range(5):
##    create_oscdef_organisms(msg)
##    send_to_organism_listeners(np.random.randint(100,1600),i)



#send_to_organism_listeners(700,4)






    

