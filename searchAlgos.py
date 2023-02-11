from NodeClass import Node
import copy as c

class SearchAlgos:
    def __init__(self, node:Node):
        self.node = node
        self.max_queue_size = 0
        self.nodes_expanded = 0
        self.frontier = None
        self.explored = None
    
    def expand(self,node:Node,hfunc = None):
        row,col = node.blank_location
        if(row > 0):
            tempNode = c.deepcopy(node)
            tempNode.slide_up(hfunc)
            if(str(tempNode.state) not in self.explored):
                if(hfunc == None):
                    self.frontier.append(tempNode)
                else:
                    self.frontier.append([tempNode,tempNode.h_val+tempNode.g_val])    
                self.explored[str(tempNode.state)] = 0
            
        if(row < node.row_size-1):
            tempNode = c.deepcopy(node)
            tempNode.slide_down(hfunc)
            if(str(tempNode.state) not in self.explored):
                if(hfunc == None):
                    self.frontier.append(tempNode)
                else:
                    self.frontier.append([tempNode,tempNode.h_val+tempNode.g_val])    
                self.explored[str(tempNode.state)] = 0

        if(col > 0):
            tempNode = c.deepcopy(node)
            tempNode.slide_left(hfunc)
            if(str(tempNode.state) not in self.explored):
                if(hfunc == None):
                    self.frontier.append(tempNode)
                else:
                    self.frontier.append([tempNode,tempNode.h_val+tempNode.g_val])    
                self.explored[str(tempNode.state)] = 0

        if(col < node.col_size-1):
            tempNode = c.deepcopy(node)
            tempNode.slide_right(hfunc)
            if(str(tempNode.state) not in self.explored):
                if(hfunc == None):
                    self.frontier.append(tempNode)
                else:
                    self.frontier.append([tempNode,tempNode.h_val+tempNode.g_val])    
                self.explored[str(tempNode.state)] = 0




    def uniformCostSearch(self):
        self.frontier = list()
        self.explored = dict()
        self.frontier.append(self.node)
        self.explored[str(self.node.state)] = 0
        while(len(self.frontier) != 0):
            self.max_queue_size = max(self.max_queue_size,len(self.frontier))
            node = self.frontier.pop(0)
            if(node.goal_test()):
                print("GOAL!!!")
                return True, node
            print(f"The best node to expand with g(n) = {node.g_val} and h(n) = {node.h_val}  is ")
            for row in node.state:
                for col in row:
                    print(col, end=" ")
                print()
            self.nodes_expanded+=1
            self.expand(node)
        return False, node

    def aStarMisplaced(self):
        self.frontier = list()
        self.explored = dict()
        self.frontier.append([self.node,self.node.h_val])
        self.explored[str(self.node.state)] = 0

        while(len(self.frontier) != 0):
            self.max_queue_size = max(self.max_queue_size,len(self.frontier))
            node = self.frontier.pop(0)[0]
            if(node.goal_test()):
                print("GOAL!!!")
                return True, node
            print(f"The best node to expand with g(n) = {node.g_val} and h(n) = {node.h_val}  is ")
            for row in node.state:
                for col in row:
                    print(col, end=" ")
                print()
            self.nodes_expanded+=1
            self.expand(node,1)
            self.frontier = sorted(self.frontier, key= lambda x: x[1])
        return False, node

start= [[1,0,3],
        [4,2,6],
        [7,5,8]]

goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]
