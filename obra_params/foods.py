import numpy as np
import pyOSC3
from constants import *

class Food:
    def __init__(self,env,current_state,type='herbivore'):
        self.env = env
        self.current_state = current_state
        self.zone = np.random.randint(len(states))
        self.current_freq_state = states[self.zone][self.current_state]
        #print('self.current_freq_state')
        #print(self.current_freq_state)
        self.pan = 2*((self.current_freq_state - min(states[self.zone])))/(max(states[self.zone])-min(states[self.zone])) - 1
        self.type = type
        self.init_connection_with_supercollider()
        
    def send_msg_to_sc(self):
        #\freq,msg[4],\amp,msg[5],\pan,msg[6],\out,0
        #self.msg.append([self.idx,self.current_freq_state,0.001])
        self.msg.append([self.idx,'freq',self.current_freq_state,'amp',0.001])
        #print('fooood',self.msg)
        self.client.send(self.msg)
        del self.msg[:]
    def init_connection_with_supercollider(self):
        self.client = pyOSC3.OSCClient()
        self.client.connect(('127.0.0.1',57120))
        self.msg = pyOSC3.OSCMessage()
        #print('self.env.max_n_food',self.env.max_n_food)
        self.idx = self.env.max_n_food - 1
        self.msg.setAddress(f'/Fmsg{self.idx}')
            

if __name__ == '__main__':
    f = Food()
    print(f.type)
