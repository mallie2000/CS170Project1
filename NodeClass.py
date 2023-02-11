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
        # if(hfunc == 1):
        #     self.calculate_misplaced()
        # if(hfunc == 2):
        #     self.calculate_euclidian()


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

    def calculate_euclidian(self):
        euclidD = 0
        position_of_values_in_goal_state = {0:(2,2),
                                            1:(0,0),
                                            2:(0,1),
                                            3:(0,2),
                                            4:(1,0),
                                            5:(1,1),
                                            6:(1,2),
                                            7:(2,0),
                                            8:(2,1)}
        for row in range(self.row_size):
            for col in range(self.col_size):
                tile_number = self.state[row][col]
                x2,y2 = position_of_values_in_goal_state[tile_number]
                dist_squared = pow((row-x2),2) +pow((col-y2),2) 
                euclidD+= pow(dist_squared,0.5)
        self.h_val = euclidD



    def slide_up(self,hfunc = None):
        row,col = self.blank_location
        self.state[row][col], self.state[row-1][col] = self.state[row-1][col], self.state[row][col]
        self.blank_location = [row-1,col]
        self.depth+=1
        self.g_val+=1
        if(hfunc == 1):
            self.calculate_misplaced()
        if(hfunc == 2):
            self.calculate_euclidian()
        
    def slide_down(self,hfunc = None):
        row,col = self.blank_location
        self.state[row][col], self.state[row+1][col] = self.state[row+1][col], self.state[row][col]
        self.blank_location = [row+1,col]
        self.depth+=1
        self.g_val+=1
        if(hfunc == 1):
            self.calculate_misplaced()
        if(hfunc == 2):
            self.calculate_euclidian()

    def slide_left(self,hfunc = None):
        row,col = self.blank_location
        self.state[row][col], self.state[row][col-1] = self.state[row][col-1], self.state[row][col]
        self.blank_location = [row,col-1]
        self.depth+=1
        self.g_val+=1
        if(hfunc == 1):
            self.calculate_misplaced()
        if(hfunc == 2):
            self.calculate_euclidian()

    def slide_right(self,hfunc = None):
        row,col = self.blank_location
        self.state[row][col], self.state[row][col+1] = self.state[row][col+1], self.state[row][col]
        self.blank_location = [row,col+1]
        self.depth+=1
        self.g_val+=1
        if(hfunc == 1):
            self.calculate_misplaced()
        if(hfunc == 2):
            self.calculate_euclidian()

    def goal_test(self):
        return self.state == self.goal
    