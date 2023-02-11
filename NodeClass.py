class Node:
    def __init__(self,state,goal):
        self.state = state
        self.row_size = len(state)
        self.col_size = len(state[0])
        self.depth = 0
        self.h_val = 0
        self.g_val = 0
        self.goal = goal
        self.blank_location = None
        self.find_blank()


    def find_blank(self):
        for row in range(len(self.state)):
            for col in range(len(self.state[0])):
                if(self.state[row][col]) == 0:
                    self.blank_location = [row,col]

    def slide_up(self):
        row,col = self.blank_location
        self.state[row][col], self.state[row-1][col] = self.state[row-1][col], self.state[row][col]
        self.blank_location = [row-1,col]
        self.depth+=1
        self.g_val+=1
        
    def slide_down(self):
        row,col = self.blank_location
        self.state[row][col], self.state[row+1][col] = self.state[row+1][col], self.state[row][col]
        self.blank_location = [row+1,col]
        self.depth+=1
        self.g_val+=1

    def slide_left(self):
        row,col = self.blank_location
        self.state[row][col], self.state[row][col-1] = self.state[row][col-1], self.state[row][col]
        self.blank_location = [row,col-1]
        self.depth+=1
        self.g_val+=1

    def slide_right(self):
        row,col = self.blank_location
        self.state[row][col], self.state[row][col+1] = self.state[row][col+1], self.state[row][col]
        self.blank_location = [row,col+1]
        self.depth+=1
        self.g_val+=1

    def goal_test(self):
        return self.state == self.goal