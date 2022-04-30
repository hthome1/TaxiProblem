import gym
from taxiproblem import Taxi
from SearchAlgorithms import AEstrela, BuscaProfundidadeIterativa
from Graph import State
import numpy as np


env = gym.make("Taxi-v3").env
listPoints = [[0,0],[0,4],[4,0],[4,3]]
actions = {"south":0,"north":1, "east":2,"west":3, "pickup":4,"dropoff":5}


repeticoes = 0

while repeticoes < 15:

    state = env.reset()
    env.render()
    taxi_row, taxi_col, pass_idx, dest_idx = env.decode(state)
    pass_idx = listPoints[pass_idx]
    dest_idx = listPoints[dest_idx]
    taxi = [taxi_row,taxi_col]
    state = Taxi("",taxi,pass_idx,dest_idx,False)
    algorithm = AEstrela()
    result = algorithm.search(state)

    path = result.show_path().replace(" ","")
    path_list = path.split(";")
    path_list.append("dropoff")
    path_list.pop(0)


    final_path_list = []
    for e in path_list:
        final_path_list.append(actions[e])

    for a in final_path_list:
        state, reward, done, info = env.step(a)
        env.render()
    if done:
        print("Soube encontrar a solucao correta")
    else:
        print("Não soube encontrar a solução")
        repeticoes = 20
    
    repeticoes +=1 
