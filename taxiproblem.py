from typing import Tuple
from SearchAlgorithms import AEstrela, BuscaProfundidadeIterativa
from Graph import State
import numpy as np

class Taxi(State):

    def __init__(self,op,taxiPoss, pickuplocation, goal,gotPassanger):
        self.taxiPos = taxiPoss
        self.operator = op
        self.actions = ["south","north", "east","west", "pickup","dropoff"]
        self.pickupLocation = pickuplocation
        self.goal = goal
        self.gotPassanger = gotPassanger

        # self.map  =np.array([
        # [' ',' ',' ',' ',' '],
        # [' ',' ',' ',' ',' '],
        # [' ',' ',' ',' ',' '],
        # [' ',' ',' ',' ',' '],
        # [' ',' ',' ',' ',' ']])
        
        self.nogo2 = {
            "3,0" :[3,1],
            "4,0" :[4,1],
            "0,1" :[0,2],
            "1,1" :[1,2],
            "3,2" :[3,3],
            "4,2" :[4,3],
            "3,1" :[3,0],
            "4,1" :[4,0],
            "0,2" :[0,1],
            "1,2" :[1,1],
            "3,3" :[3,2],
            "4,3" :[4,2]
        }

    
    def sucessors(self):
        sucessors = []

        #south
        if self.taxiPos[0] != 4:
            sucessors.append(Taxi(self.actions[0],[self.taxiPos[0]+1,self.taxiPos[1]],self.pickupLocation,self.goal,self.gotPassanger))

        #north
        if self.taxiPos[0] != 0:
            sucessors.append(Taxi(self.actions[1],[self.taxiPos[0]-1,self.taxiPos[1]],self.pickupLocation,self.goal,self.gotPassanger))


        #east
        east = [self.taxiPos[0],self.taxiPos[1]+1]
        x = str(self.taxiPos[0])+","+str(self.taxiPos[1])

        if x in self.nogo2:
            if self.taxiPos[1] != 4 and self.nogo2[x]!= east:
                sucessors.append(Taxi(self.actions[2],[self.taxiPos[0],self.taxiPos[1]+1],self.pickupLocation,self.goal,self.gotPassanger))
        else:
            if self.taxiPos[1] != 4:
                sucessors.append(Taxi(self.actions[2],[self.taxiPos[0],self.taxiPos[1]+1],self.pickupLocation,self.goal,self.gotPassanger))


        #west
        west = [self.taxiPos[0],self.taxiPos[1]-1]
        if x in self.nogo2:
            if self.taxiPos[1] != 0 and self.nogo2[x]!= west:
                sucessors.append(Taxi(self.actions[3],[self.taxiPos[0],self.taxiPos[1]-1],self.pickupLocation,self.goal,self.gotPassanger))
        else:
            if self.taxiPos[1] != 0:
                sucessors.append(Taxi(self.actions[3],[self.taxiPos[0],self.taxiPos[1]-1],self.pickupLocation,self.goal,self.gotPassanger))

        if self.canPickup():
            sucessors.append(Taxi(self.actions[4],[self.taxiPos[0],self.taxiPos[1]],self.pickupLocation,self.goal,True))
        
        return sucessors

    def canPickup(self):
        return self.taxiPos == self.pickupLocation



    def is_goal(self):
        return (self.gotPassanger and self.taxiPos == self.goal)
    
    def description(self):
        return "Problema do taxista"
    
    def cost(self):
        return 1

    def print(self):
        return str(self.operator)
    
    def env(self):
        return str(self.operator) + ";" + str(self.gotPassanger) + ";" + str(self.taxiPos)

    def h(self):
        if self.gotPassanger == True:
            return abs(self.taxiPos[0]-self.goal[0]) + abs(self.taxiPos[1]-self.goal[1])
        
        return abs(self.taxiPos[0] - self.pickupLocation[0]) + abs(self.taxiPos[1] - self.pickupLocation[1])

def main():
    print('Busca em profundidade iterativa')


    # self, op ,taxiPos, pickup, goal,gotPassanger

    pos = [4,4]
    pickup = [0,0]
    goalc = [0,4]


    # taxi 3,6 ,passageiro [0, 8],destino [0, 0]
   #taxi 3,0 ,passageiro [4, 6],destino [0, 8]


    state = Taxi(' ',pos,pickup,goalc,False)
    algorithm = AEstrela()
    result = algorithm.search(state)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()