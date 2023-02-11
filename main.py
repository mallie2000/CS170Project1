from searchAlgos import SearchAlgos
from NodeClass import Node

start = list()
goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

print("Welcome to 862214758 8 puzzle solver")
print("Type '1' to use a default puzzle, or '2' to enter your own puzzle")
user_answer = int(input())
if user_answer == 1:
    # start= [[0,2,3],
    #         [1,4,6],
    #         [7,5,8]]
    start= [[4,1,6],
            [7,0,2],
            [3,8,5]]
else:
    print("Enter your puzzle down below, use a 0 to represent the blank")
    for i in range(3):
        input_string = input(f"Enter the values for row {i+1}, use comma separate to values: ")
        input_list =  [int(val) for val in input_string.split(",")]
        start.append(input_list)

node = Node(start,goal)
search = SearchAlgos(node)

result, node = search.uniformCostSearch()
if(result):
    print(f"To solve this problem the search algorithm expanded a total of {search.nodes_expanded} nodes")
    print(f"The maximum number of nodes in the queue at any one time: {search.max_queue_size}")
    print(f"The depth of the goal node was {node.depth}")
else:
    print("NOT FOUND")

