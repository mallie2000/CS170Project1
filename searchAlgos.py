from NodeClass import Node
import copy as c

class SearchAlgos:
    def __init__(self, node:Node):
        self.node = node
        self.max_queue_size = 0
        self.nodes_expanded = 0
        self.frontier = None
        self.explored = None
    
    def expand(self,node:Node):
        row,col = node.blank_location
        if(row > 0):
            tempNode = c.deepcopy(node)
            tempNode.slide_up()
            if(str(tempNode.state) not in self.explored):
                self.frontier.append(tempNode)
                self.explored[str(tempNode.state)] = 0
            
        if(row < node.row_size-1):
            tempNode = c.deepcopy(node)
            tempNode.slide_down()
            if(str(tempNode.state) not in self.explored):
                self.frontier.append(tempNode)
                self.explored[str(tempNode.state)] = 0

        if(col > 0):
            tempNode = c.deepcopy(node)
            tempNode.slide_left()
            if(str(tempNode.state) not in self.explored):
                self.frontier.append(tempNode)
                self.explored[str(tempNode.state)] = 0

        if(col < node.col_size-1):
            tempNode = c.deepcopy(node)
            tempNode.slide_right()
            if(str(tempNode.state) not in self.explored):
                self.frontier.append(tempNode)
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

