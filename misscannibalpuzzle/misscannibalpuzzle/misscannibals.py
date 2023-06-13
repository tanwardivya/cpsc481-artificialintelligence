from search import *

class MissCannibals(Problem):
    def __init__(self, M=3, C=3, goal=(0, 0, False)):
        initial = (M, C, True)
        self.M = M
        self.C = C
        super().__init__(initial, goal)
    
    def get_possible_actions(self) -> list:
        possible_actions = []
        for i in range(self.M + 1):
            for j in range(self.C + 1):
                if 0 < i < j: #Cannibal is greater then Missionary
                    continue
                if 1 <= i + j <= 2:
                    possible_actions.append((i,j))
        return possible_actions
    
    def is_valid(self, old_state)-> bool:
        if old_state[0] < 0 or old_state[1] < 0 or old_state[0]>=self.M + 1 or old_state[1] >= self.C +1:
            return False
        if old_state[1] > old_state[0] > 0:
            return False
        return True
    @staticmethod
    def move_to_action(move) -> str:
        if move[0] == 0 and move[1] == 1:
            return 'C'
        elif move[0] == 1 and move[1] == 0:
            return 'M'
        elif move[0] == 0 and move[1] == 2:
            return 'CC'
        elif move[0] == 2 and move[1] == 0:
            return 'MM'
        elif move[0] == 1 and move[1] == 1:
            return 'MC'
        return 'UNK'
    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""

        if not self.is_valid(state) or self.goal_test(state):
            return []
        list_of_actions = []
        moves = self.get_possible_actions()
        for move in moves:
            if state[2]:
                sign = -1
            else:
                sign = 1
            new_state_L = (state[0] + move[0]*sign,state[1] + move[1]*sign, not state[2])
            new_state_R = (self.M - new_state_L[0], self.C - new_state_L[1])
            if self.is_valid(new_state_L) and self.is_valid(new_state_R):
                list_of_actions.append(self.move_to_action(move))
        return list_of_actions

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        if state[2]:
            if action == 'M':
                return (state[0]-1, state[1],not state[2])
            elif action == 'MM':
                return (state[0]-2, state[1],not state[2])
            elif action == 'CC':
                return (state[0], state[1]-2,not state[2])
            elif action == 'C':
                return (state[0], state[1]-1,not state[2])
            elif action == 'MC':
                return (state[0]-1, state[1]-1,not state[2])
        else:
            if action == 'M':
                return (state[0]+1, state[1],not state[2])
            elif action == 'MM':
                return (state[0]+2, state[1],not state[2])
            elif action == 'CC':
                return (state[0], state[1]+2,not state[2])
            elif action == 'C':
                return (state[0], state[1]+1,not state[2])
            elif action == 'MC':
                return (state[0]+1, state[1]+1,not state[2])


    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal or checks for state in self.goal if it is a
        list, as specified in the constructor. Override this method if
        checking against a single self.goal is not enough."""
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal

    # YOUR CODE GOES HERE
if __name__ == '__main__':
    mc = MissCannibals(3,3)
    # print(mc.actions((3, 2, True))) # Test your code as you develop! This shoul return ['CC', 'C', 'M']
    path = depth_first_graph_search(mc).solution()
    print(path)
    path = breadth_first_graph_search(mc).solution()
    print(path)
