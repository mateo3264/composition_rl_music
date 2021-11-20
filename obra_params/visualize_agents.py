import numpy as np
import cv2
from PIL import Image
import matplotlib
import matplotlib.animation as animation
import matplotlib.pyplot as plt
#import matplotlib.pyplot as figure
matplotlib.use('Agg')
from os import path

NSTATES = 100
NAGENTS = 2
def draw_env(nstates,foods):
	env = np.zeros((1,NSTATES,3),dtype=np.uint8)
	#draw
	for food in foods:
		#env[0,ptss['pts'+str(i)]] = [0,255,0]
        
                env[0,food.current_state] = [0,255,0]
		#env[0,ntss['nts'+str(i)]] = [0,0,255]
	
	return env

def draw_agents(env,current_poss):
	for cur_pos in current_poss:
		env[0,cur_pos] = [0,255,255]

def show_all(env):
	img = Image.fromarray(env).resize((1200,12),Image.NEAREST)
	cv2.imshow('',np.array(img))
	cv2.waitKey(1)


def send_data(n_agents,n_food):
        with open('pop_agents.csv','r') as file:
                n_Xs = len(file.readlines())
        with open('pop_agents.csv','a') as file:
                file.write(f'{n_Xs},{n_agents}\n')
        with open('pop_food.csv','a') as file:
                file.write(f'{n_Xs},{n_food}\n')

class MatplotVis:
        def __init__(self):
                self.fig = plt.figure()
                self.ax = self.fig.add_subplot(111)
                if not path.exists('pop_agents.csv'):
                        with open('pop_agents.csv','w') as file:
                                print('pop_agents.csv CREATED')
                if not path.exists('pop_food.csv'):
                        with open('pop_food.csv','w') as file:
                                print('pop_food.csv CREATED')
                
        def animate(self,i):
                with open('pop_agents.csv','r') as file:
                        lines = file.readlines()
                        #print('lines')
                        #print(len(lines))
                        #Xs = [x for x in range(len(lines))]
                        Xs = []
                        pop_agents = []
                        for i,line in enumerate(lines):
                                 #print('line',line)
                                 x,pa = line.split(',')
                                 Xs.append(x)
                                 pop_agents.append(pa)
                                 #pop_food.append(pf)
                        self.ax.clear()
                        self.ax.plot(Xs,pop_agents)
                with open('pop_food.csv','r') as file:
                        lines = file.readlines()
                        #print('lines')
                        #print(len(lines))
                        #Xs = [x for x in range(len(lines))]
                        Xs = []
                        pop_food = []
                        for i,line in enumerate(lines):
                                 #print('line',line)
                                 x,pf = line.split(',')
                                 Xs.append(x)
                                 pop_food.append(pa)
                                 #pop_food.append(pf)
                        #self.ax.clear()
                        self.ax.plot(Xs,pop_food)
                        
        def execute(self):
                self.ani = animation.FuncAnimation(self.fig,self.animate,interval=1000)
                plt.show()




if __name__ == '__main__':	
	ptss = [2]
	ntss = [NSTATES - 2]
	current_poss = [np.random.randint(5,NSTATES-5) for agent in range(NAGENTS)]
	env = draw_env(NSTATES,ptss,ntss)
	while True:
		show_all(env)
		for i,cur_pos in enumerate(current_poss):
			cur_pos = cur_pos + np.random.choice([-1,1])
			if cur_pos < 0:
				cur_pos = 0
			elif cur_pos > NSTATES - 1:
				cur_pos = NSTATES - 1
			current_poss[i] = cur_pos
		#print('current_pos',current_pos)
		env = draw_env(NSTATES,ptss,ntss)
		draw_agents(env,current_poss)
		# z = np.zeros((1,NSTATES,3),dtype=np.uint8)
		# z[0,pts] = [0,255,0]
		# z[0,nts] = [0,0,255]
		# z[0,current_pos] = [0,255,255]



                


                        
                



        









