import gym
import numpy as np
import curses
import keyboard
import random
import time
import math
env=gym.make('CartPole-v0')
observation, reward, done, info=env.reset()
done=False
action=0
reward=0
pop_size=10
cr_rate=0.2
m_rate=1
def sigmoid(x):
  return round(1 / (1 + math.exp(-x)))

def gen_pop():
    pop=[]
    for i in range(pop_size):
        weights=np.random.uniform(size=4) * 2 - 1
        pop.append(weights)

    return pop

def crossover(po):
    pop=[]
    topp=int(cr_rate*len(po))
    top=[po[x][0] for x in range(0,topp)]
    for i in range(0,topp):
        pop.append(top[i])
    j=0
    s_topp=topp+(topp)/2
    for i in range(topp,topp+(topp)/2):
        a=top[j]
        b=top[j+1]
        c=[]
        for k in range(len(a)):
            c.append((a[k]+b[k])/2)
        j=j+2
        pop.append(c)
    j=0

    for i in range(pop_size-(s_topp)):

        weights=np.random.uniform(size=4)*2-1
        pop.append(weights)
    return pop

def mutation(po):
    for i in range(len(po)):
        c=po[i]
        for j in range(len(c)):
            if m_rate>random.randint(0,120):
                c[j]=np.random.uniform()*2-1
                print "Mutated"
    return po

pop=gen_pop()
gen=0
observation=np.zeros(4)
ep_no=0
#print pop
winner=[]
win=0
while True:
    if win==0:
        gen+=1
        i=0
        n_pop=[]
        while i<pop_size:
            if win==1:
                break
            cand=pop[i]
            cand=np.array(cand)
            #print cand,observation
            total_reward=0
            while done==False:

                #weights = np.random.uniform(size=4) * 2 - 1
                action = int(sigmoid(np.matmul(observation, cand)))
                #print(action)
                observation, reward, done, info = env.step(action)
                total_reward+=reward
                env.render()
            n_pop.append([cand,total_reward])
            if total_reward>=195:
                winner=cand
                win=1
                print "DONE:",winner,total_reward,ep_no
                break

            env.reset()
            ep_no+=1
            #print("Fail!")
            done=False
            i+=1

        n_pop=sorted(n_pop,key=lambda x: x[1])
        n_pop=n_pop[::-1]
        best_reward=n_pop[0][1]
        pop=crossover(n_pop)
        pop=mutation(pop)
        #print gen,best_reward,ep_no
    else:
        #print "Episodes:",ep_no
        if done==True:
            env.reset()
            done=False
        action = int(sigmoid(np.matmul(observation, winner)))
        observation, reward, done, info = env.step(action)
        time.sleep(0.05)
        env.render()

