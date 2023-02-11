class Node:
    def __init__(self,state,goal,hfunc = None):
        self.state = state
        self.row_size = len(state)
        self.col_size = len(state[0])
        self.depth = 0
        self.h_val = 0
        self.g_val = 0
        self.goal = goal
        self.blank_location = None
        self.find_blank()
        if(hfunc == 1):
            self.calculate_misplaced()


    def find_blank(self):
        for row in range(len(self.state)):
            for col in range(len(self.state[0])):
                if(self.state[row][col]) == 0:
                    self.blank_location = [row,col]

    def calculate_misplaced(self):
        h_val = 0
        for row in range(self.row_size):
            for col in range(self.col_size):
                if(self.state[row][col] != self.goal[row][col]):
                    h_val+=1
        self.h_val = h_val



    def slide_up(self,hfunc = None):
        row,col = self.blank_location
        self.state[row][col], self.state[row-1][col] = self.state[row-1][col], self.state[row][col]
        self.blank_location = [row-1,col]
        self.depth+=1
        self.g_val+=1
        if(hfunc == 1):
            self.calculate_misplaced()
        
    def slide_down(self,hfunc = None):
        row,col = self.blank_location
        self.state[row][col], self.state[row+1][col] = self.state[row+1][col], self.state[row][col]
        self.blank_location = [row+1,col]
        self.depth+=1
        self.g_val+=1
        if(hfunc == 1):
            self.calculate_misplaced()

    def slide_left(self,hfunc = None):
        row,col = self.blank_location
        self.state[row][col], self.state[row][col-1] = self.state[row][col-1], self.state[row][col]
        self.blank_location = [row,col-1]
        self.depth+=1
        self.g_val+=1
        if(hfunc == 1):
            self.calculate_misplaced()

    def slide_right(self,hfunc = None):
        row,col = self.blank_location
        self.state[row][col], self.state[row][col+1] = self.state[row][col+1], self.state[row][col]
        self.blank_location = [row,col+1]
        self.depth+=1
        self.g_val+=1
        if(hfunc == 1):
            self.calculate_misplaced()

    def goal_test(self):
        return self.state == self.goal
    